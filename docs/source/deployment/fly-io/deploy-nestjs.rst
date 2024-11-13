Deploy NestJS
=============

.. title:: NestJS Deployment Guide for Fly.io
.. meta::
    :description: Learn how to deploy NestJS projects on Fly.io  
    :keywords: nest.js on fly.io, nest.js fly.io cloud, nest.js fly.io deployment, fly.io cloud tools, deploy, ci-cd, deployment  

This page explains how to deploy a `NestJS <../../technologies/nestjs/index.html>`__ project on `Fly.io <./index.html>`__, the popular deployment platform for developers. 

.. include::  /_templates/components/banner-top.rst

Framework Overview
------------------

NestJS is a progressive Node.js framework built with TypeScript that combines elements of Object-Oriented Programming (OOP), Functional Programming (FP), and Functional Reactive Programming (FRP). 
It implements a modular architecture pattern, heavily inspired by Angular, making it ideal for building scalable server-side applications with enterprise-grade architectural patterns.

Pre-Deployment Configuration
----------------------------

Required Dependencies
*********************

..	code-block:: json
    
    {
        "dependencies": {
            "@nestjs/common": "^10.0.0",
            "@nestjs/core": "^10.0.0",
            "@nestjs/platform-express": "^10.0.0",
            "@nestjs/config": "^3.0.0",
            "@nestjs/swagger": "^7.0.0",
            "class-transformer": "^0.5.1",
            "class-validator": "^0.14.0",
            "helmet": "^7.0.0",
            "compression": "^1.7.4",
            "winston": "^3.9.0"
        }
    }

Production Configuration Structure
**********************************

..	code-block:: typescript

    // config/production.config.ts
    export default () => ({
        port: parseInt(process.env.PORT, 10) || 3000,
        database: {
            url: process.env.DATABASE_URL,
            type: 'postgres',
            ssl: {
            rejectUnauthorized: false
            }
        },
        cors: {
            origin: process.env.ALLOWED_ORIGINS?.split(',') || [],
            credentials: true
        },
        swagger: {
            enabled: false
        }
    });

Container Configuration
-----------------------

Dockerfile Implementation
*************************

..	code-block:: dockerfile

    # Stage 1: Development
    FROM node:18-slim AS development

    WORKDIR /usr/src/app

    COPY package*.json ./
    COPY tsconfig*.json ./

    RUN npm install

    COPY . .

    RUN npm run build

    # Stage 2: Production
    FROM node:18-slim AS production

    ARG NODE_ENV=production
    ENV NODE_ENV=${NODE_ENV}

    WORKDIR /usr/src/app

    COPY package*.json ./

    RUN npm install --only=production

    COPY --from=development /usr/src/app/dist ./dist

    EXPOSE 3000

    CMD ["node", "dist/main"]


Docker Compose (Development)
****************************

..	code-block:: yaml

    version: '3.8'
    services:
    api:
        build:
        context: .
        target: development
        volumes:
        - .:/usr/src/app
        - /usr/src/app/node_modules
        ports:
        - "3000:3000"
        environment:
        - NODE_ENV=development


Fly.io Platform Configuration
-----------------------------

fly.toml
********

..	code-block:: toml 

    app = "your-nestjs-app"
    primary_region = "dfw"

    [build]
        dockerfile = "Dockerfile"

    [env]
        NODE_ENV = "production"
        PORT = "3000"

    [http_service]
        internal_port = 3000
        force_https = true
        auto_stop_machines = true
        auto_start_machines = true
        min_machines_running = 1
        processes = ["app"]

    [[vm]]
        cpu_kind = "shared"
        cpus = 1
        memory_mb = 512

    [metrics]
        port = 9091
        path = "/metrics"

Service Layer Implementation
----------------------------

Database Service Configuration
******************************

..	code-block:: typescript

    // database/database.service.ts
    import { Injectable } from '@nestjs/common';
    import { TypeOrmModuleOptions } from '@nestjs/typeorm';
    import { ConfigService } from '@nestjs/config';

    @Injectable()
    export class DatabaseConfigService {
        constructor(private configService: ConfigService) {}

        getTypeOrmConfig(): TypeOrmModuleOptions {
            return {
            type: 'postgres',
            url: this.configService.get<string>('database.url'),
            ssl: this.configService.get<boolean>('database.ssl'),
            autoLoadEntities: true,
            synchronize: false,
            logging: ['error', 'warn'],
            poolSize: 5,
            maxQueryExecutionTime: 1000,
            };
        }
    }

Logger Service Implementation
*****************************

..	code-block:: typescript

    // logger/logger.service.ts
    import { Injectable, LoggerService } from '@nestjs/common';
    import * as winston from 'winston';

    @Injectable()
    export class CustomLogger implements LoggerService {
    private logger: winston.Logger;

    constructor() {
        this.logger = winston.createLogger({
        level: 'info',
        format: winston.format.combine(
            winston.format.timestamp(),
            winston.format.json()
        ),
        transports: [
            new winston.transports.Console({
            format: winston.format.simple(),
            }),
        ],
        });
    }

    log(message: string) {
        this.logger.info(message);
    }

    error(message: string, trace: string) {
        this.logger.error(message, { trace });
    }

    warn(message: string) {
        this.logger.warn(message);
    }
    }


Health Monitoring Implementation
--------------------------------

Health Check Module
*******************

..	code-block:: typescript
    
    // health/health.module.ts
    import { Module } from '@nestjs/common';
    import { TerminusModule } from '@nestjs/terminus';
    import { HealthController } from './health.controller';

    @Module({
    imports: [TerminusModule],
    controllers: [HealthController],
    })
    export class HealthModule {}

Health Controller
*****************

..	code-block:: typescript

    // health/health.controller.ts
    import { Controller, Get } from '@nestjs/common';
    import { HealthCheck, HealthCheckService } from '@nestjs/terminus';

    @Controller('health')
    export class HealthController {
        constructor(private health: HealthCheckService) {}

        @Get()
        @HealthCheck()
        check() {
            return this.health.check([]);
        }
    }

Deployment Process
------------------

1. Environment Configuration
****************************

..	code-block:: bash 

    # Configure production secrets
    fly secrets set DATABASE_URL="postgresql://..."
    fly secrets set JWT_SECRET="your-secret"
    fly secrets set ALLOWED_ORIGINS="https://your-domain.com"


2. Database Setup
*****************

..	code-block:: bash 

    # Create Postgres instance
    fly postgres create

    # Attach to application
    fly postgres attach <database-name>

    # Run migrations
    fly ssh console -C "npm run migration:run"

3. Deployment Execution
***********************

..	code-block:: bash 

    # Initial deployment
    fly launch

    # Subsequent deployments
    fly deploy

Security Implementation
-----------------------

Security Middleware Configuration
*********************************

..	code-block:: typescript

    // security/security.middleware.ts
    import { Injectable, NestMiddleware } from '@nestjs/common';
    import { Request, Response, NextFunction } from 'express';
    import * as helmet from 'helmet';
    import * as compression from 'compression';

    @Injectable()
    export class SecurityMiddleware implements NestMiddleware {
        use(req: Request, res: Response, next: NextFunction) {
            helmet()(req, res, () => {
            compression()(req, res, next);
            });
        }
    }

Performance Optimization
------------------------

1. Server Configuration
***********************

..	code-block:: typescript

    // main.ts
    async function bootstrap() {
        const app = await NestFactory.create(AppModule, {
            logger: new CustomLogger(),
        });

        app.enableCors(app.get(ConfigService).get('cors'));
        app.use(helmet());
        app.use(compression());
        
        await app.listen(process.env.PORT || 3000);
    }


2. Response Caching
*******************

..	code-block:: typescript


    // cache/cache.module.ts
    import { CacheModule } from '@nestjs/cache-manager';
    import { redisStore } from 'cache-manager-redis-store';

    @Module({
        imports: [
            CacheModule.registerAsync({
            useFactory: () => ({
                store: redisStore,
                url: process.env.REDIS_URL,
                ttl: 60 * 60, // 1 hour
            }),
            }),
        ],
    })
    export class CustomCacheModule {}

Monitoring and Logging
----------------------

Prometheus Metrics
******************

..	code-block:: typescript

    // metrics/metrics.service.ts
    import { Injectable } from '@nestjs/common';
    import { Registry, collectDefaultMetrics } from 'prom-client';

    @Injectable()
    export class MetricsService {
        private readonly registry: Registry;

        constructor() {
            this.registry = new Registry();
            collectDefaultMetrics({ register: this.registry });
        }

        async getMetrics(): Promise<string> {
            return this.registry.metrics();
        }
    }

Troubleshooting Guide
---------------------

1. **Connection Timeouts**
   - Review database connection pool settings
   - Check network configuration
   - Verify firewall rules

2. **Memory Leaks**
   - Monitor garbage collection
   - Review subscription cleanup
   - Check for memory-intensive operations

3. **Performance Degradation**
   - Review database query performance
   - Check cache hit rates
   - Monitor event loop lag
   - Analyze N+1 query patterns

This guide provides a comprehensive approach to deploying NestJS applications on Fly.io with a focus on production-ready configurations and best practices.

.. include::  /_templates/components/footer-links.rst
