#!/bin/bash

set -e
set -u


function create_user_and_database() {
    psql -v ON_ERROR_STOP=1 --username postgres <<-EOSQL
        CREATE USER "$POSTGRES_USER" ENCRYPTED PASSWORD "$POSTGRES_PASSWORD";
        CREATE DATABASE "$POSTGRES_DB";
        GRANT ALL PRIVILEGES ON DATABASE "$POSTGRES_DB" TO "$POSTGRES_USER";
EOSQL
}

echo "Create database"
create_user_and_database
echo "Multiple databases created"
