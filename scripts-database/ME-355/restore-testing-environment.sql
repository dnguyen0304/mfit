/* pg_dump --username duyn_su --dbname=mfit_dev_2 --host=localhost --port=5432 --no-owner --schema-only --file=restore.sql */

CREATE DATABASE mfit_testing_1;
CREATE ROLE mfit_testing WITH LOGIN PASSWORD '';

\connect mfit_testing_1;
\i restore.sql

REVOKE SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public FROM mfit;
REVOKE USAGE ON ALL SEQUENCES IN SCHEMA public FROM mfit;

GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO mfit_testing;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO mfit_testing;

INSERT INTO routines_units (
	name,
	created_by
)
VALUES
	('liters', -1),
	('repetitions', -1),
	('seconds', -1);
