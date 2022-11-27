#!/bin/bash

set -e
set -u


function create_user_and_database() {
    test_db=test_$POSTGRES_DB
    psql -v ON_ERROR_STOP=1 --username postgres <<-EOSQL
        CREATE USER "$POSTGRES_USER" ENCRYPTED PASSWORD "$POSTGRES_PASSWORD";
        CREATE DATABASE $test_db;
        GRANT ALL PRIVILEGES ON DATABASE $test_db TO "$POSTGRES_USER";
EOSQL
}

echo "Create database"
create_user_and_database
echo "Multiple databases created"
