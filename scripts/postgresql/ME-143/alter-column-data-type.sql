DO $$
DECLARE
	sql		text;
	record_	record;
BEGIN
	sql := 'ALTER TABLE %I
			ALTER COLUMN %I
			SET DATA TYPE timestamp with time zone;';

	RAISE INFO 'The process is starting.';

	FOR record_ IN
		SELECT
			table_name,
			column_name
		FROM information_schema.columns
		WHERE
			table_schema = 'public' AND
			data_type = 'timestamp without time zone'
	LOOP
		RAISE INFO 'The migration for the "%" table is starting.', record_.table_name;
		EXECUTE format(sql, record_.table_name, record_.column_name);
		RAISE INFO 'The migration for the "%" table completed SUCCESSFULLY.', record_.table_name;
	END LOOP;

	RAISE INFO 'The process is stopping.';
END $$
LANGUAGE plpgsql;
