import os, json, uuid
from django.core.management.base import BaseCommand
from django.conf import settings
from apps.helpers.db_migrator import *

DIR_TMP = os.path.join(settings.BASE_DIR, 'tmp')

class Command(BaseCommand):
    help = 'Compare schemas and migrate data between two databases'

    def add_arguments(self, parser):
        parser.add_argument('source_db', type=str, help='Source database name')
        parser.add_argument('target_db', type=str, help='Target database name')
        parser.add_argument('--migrate', action='store_true', help='Perform migration for suggested tables')
        parser.add_argument('--batch-size', type=int, default=1000, help='Batch size for processing records')

    def handle(self, *args, **options):
        source_db = options['source_db']
        target_db = options['target_db']
        perform_migration = options['migrate']
        batch_size = options['batch_size']

        migrator = DatabaseMigrator(source_db, target_db)
        source_conn, source_engine, target_conn, target_engine = migrator.connect()

        if not source_conn:
            self.stdout.write(self.style.ERROR("Failed to connect to SOURCE DB. Aborting."))
            return

        if not target_conn:
            self.stdout.write(self.style.ERROR("Failed to connect to TARGET DB. Aborting."))
            return

        source_tables = migrator.get_tables(migrator.source_conn, source_engine)
        target_tables = migrator.get_tables(migrator.target_conn, target_engine)

        print(' > SRC  Tables: ' + str(source_tables) )
        print(' > DEST Tables: ' + str(target_tables) )

        identical_tables = migrator.compare_schemas(source_tables, target_tables)

        if len( identical_tables.keys() ) == 0:
            self.stdout.write(self.style.WARNING("No identical tables found between the databases."))
        else:
            self.stdout.write(self.style.SUCCESS("Identical tables that can be migrated:"))
            for src_table in identical_tables.keys():
                dest_table = identical_tables[src_table]
                self.stdout.write(f"- {src_table} -> {dest_table}")

            if perform_migration:
                migrator.migrate_tables(identical_tables, batch_size)

        migrator.close()
