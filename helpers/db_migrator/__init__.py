# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
License: MIT
"""

import os, sys, json
from pprint import pp

from django.db import connections

from helpers.util import *

DB_DRIVER_SQLITE = False
DB_DRIVER_MYSQL  = False
DB_DRIVER_PGSQL  = False

try:
    import sqlite3
    DB_DRIVER_SQLITE = True
except:
    pass 

try:
    import mysql.connector
    DB_DRIVER_MYSQL = True
except:
    pass 

try:
    import psycopg2
    from psycopg2.extras import DictCursor
    DB_DRIVER_PGSQL = True
except:
    pass 

class DatabaseMigrator:
    def __init__(self, source_db, target_db):
        self.source_db = source_db
        self.target_db = target_db
        self.source_conn = None
        self.target_conn = None

        self.source_engine = None
        self.target_engine = None

    def connect(self):
        self.source_conn, self.source_engine = self.get_connection(self.source_db)
        self.target_conn, self.target_engine = self.get_connection(self.target_db)
        return self.source_conn, self.source_engine, self.target_conn, self.target_engine

    def close(self):
        if self.source_conn:
            self.source_conn.close()
        if self.target_conn:
            self.target_conn.close()

    def get_connection(self, db_json):
        try:
            db_config = {key.lower(): value for key, value in db_json.items()}
            db_name   = db_config['name'] 

            print( ' > DB ['+db_name+'] ' + str( db_config ) )
            engine = db_config['driver']
            if 'sqlite' in engine:
                return sqlite3.connect(db_config['name']), engine
            elif 'mysql' in engine:
                return mysql.connector.connect(
                    database=db_config['name'],
                    user=db_config['user'],
                    password=db_config['pass'],
                    host=db_config['host'],
                    port=db_config['port']
                ), engine
            elif 'postgresql' in engine:
                return psycopg2.connect(
                    dbname=db_config['name'],
                    user=db_config['user'],
                    password=db_config['pass'],
                    host=db_config['host'],
                    port=db_config['port']
                ), engine
            else:
                raise ValueError(f"Unsupported database engine: {engine}")
        except Exception as e:
            print(f"Failed to connect to database: {str(e)}")
            return None, None

    def get_tables(self, conn, engine):
        cursor = conn.cursor()
        if 'sqlite' in engine:
            print('> Fetch Tables (SQLite)')
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        elif 'mysql' in engine:
            print('> Fetch Tables (MySql)')
            cursor.execute("SHOW TABLES")
        else:  # PostgreSQL
            print('> Fetch Tables (PostgreSQL)')
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        
        #tables = [row[0] for row in cursor.fetchall()]
        tables = []
        for row in cursor.fetchall():
            tables.append( row[0] )

        print( ' > Tables: ' + str( len( tables )) )

        cursor.close()
        return tables

    def get_table_schema(self, conn, table_name):
        cursor = conn.cursor()
        if isinstance(conn, sqlite3.Connection):
            cursor.execute(f"PRAGMA table_info({table_name})")
            schema = [(row[1], row[2], row[3], 'YES' if row[5] else 'NO') for row in cursor.fetchall()]
        elif isinstance(conn, mysql.connector.connection.MySQLConnection):
            cursor.execute(f"DESCRIBE {table_name}")
            schema = [(row[0], row[1], None, row[2]) for row in cursor.fetchall()]
        else:  # PostgreSQL
            cursor.execute(f"""
                SELECT column_name, data_type, character_maximum_length, is_nullable
                FROM information_schema.columns
                WHERE table_name = %s
                ORDER BY ordinal_position
            """, (table_name,))
            schema = cursor.fetchall()
        cursor.close()
        return schema

    def compare_schemas(self, source_tables, target_tables):
        identical_tables = {}
        for src_table in source_tables:
            for dest_table in target_tables:
                source_schema = self.get_table_schema(self.source_conn, src_table)
                target_schema = self.get_table_schema(self.target_conn, dest_table)

                if source_schema == target_schema:
                    identical_tables[src_table] = dest_table
        return identical_tables

    def migrate_tables(self, identical_tables, batch_size):
        for src_table in identical_tables:
            dest_table = identical_tables[src_table]
            print(f" > Migrating '{src_table}' -> {dest_table} ")
            
            # Get total count
            source_cursor = self.source_conn.cursor()
            source_cursor.execute(f"SELECT COUNT(*) FROM {src_table}")
            total_count = source_cursor.fetchone()[0]
            source_cursor.close()

            # Migrate in batches
            offset = 0
            while offset < total_count:
                source_cursor = self.source_conn.cursor(dictionary=True)
                source_cursor.execute(f"SELECT * FROM {src_table} LIMIT %s OFFSET %s", (batch_size, offset))
                rows = source_cursor.fetchall()

                if not rows:
                    break

                columns = list(rows[0].keys())
                placeholders = ','.join(['%s'] * len(columns))
                insert_query = f"INSERT INTO {dest_table} ({','.join(columns)}) VALUES ({placeholders})"

                try:
                    
                    print(' SQL (insert): ' + insert_query )

                    target_cursor = self.target_conn.cursor()
                    target_cursor.executemany(insert_query, [tuple(row.values()) for row in rows])
                    self.target_conn.commit()

                    print(f"Migrated {len(rows)} records from offset {offset}")
                except Exception as e:
                    print('    |- (error): ' + str( e ))  

                offset += batch_size

                source_cursor.close()
                target_cursor.close()

            print(f"Finished migrating table '{src_table}'")
          
    

