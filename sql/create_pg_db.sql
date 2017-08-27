CREATE DATABASE pytest;

\connect pytest

CREATE USER pytester PASSWORD 'asdf';

CREATE SCHEMA data;

CREATE TABLE data.sample_data (
  id SERIAL PRIMARY KEY,
  sha256 VARCHAR NOT NULL
) WITHOUT OIDS;

GRANT USAGE ON SCHEMA data TO pytester;

GRANT ALL ON data.sample_data TO pytester;
