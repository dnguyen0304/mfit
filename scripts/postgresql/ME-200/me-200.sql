DO $$
DECLARE
	sql			text;
	table_name	regclass;
BEGIN
	sql := 'ALTER TABLE %I RENAME COLUMN %I TO %I;';

	RAISE INFO 'The process is starting.';

	FOR table_name IN
		SELECT table_name
		FROM information_schema.tables
		WHERE table_schema = 'public'
	LOOP
		RAISE INFO 'The migration for the "%" table is starting.', table_name;
		EXECUTE format(sql, table_name, 'created_on', 'created_at');
		EXECUTE format(sql, table_name, 'updated_on', 'updated_at');
		RAISE INFO 'The migration for the "%" table completed SUCCESSFULLY.', table_name;
	END LOOP;

	RAISE INFO 'The process is stopping.';
END $$
LANGUAGE plpgsql;
