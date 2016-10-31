DO $$
DECLARE
	countBefore integer;
	countAfter integer;
	currentDatetime	timestamp with time zone;
BEGIN
	currentDatetime := CURRENT_TIMESTAMP AT TIME ZONE 'localtime';

	countBefore := (
		SELECT COUNT(*)
		FROM attempts_logs
	);

	INSERT INTO attempts_logs (
		attempts_id,
		habits_id,
		sets_remaining,
		created_by
	)
	(
		SELECT
			attempts.id,
			routines.habits_id,
			routines.sets,
			-1
		FROM attempts
		INNER JOIN routines ON routines.habit_groups_id = attempts.habit_groups_id
		WHERE
			attempts.starts_at <= currentDatetime AND
			attempts.ends_at > currentDatetime
	);

	countAfter := (
		SELECT COUNT(*)
		FROM attempts_logs
	);

	RAISE INFO '% record(s) were inserted SUCCESSFULLY.', countAfter - countBefore;
END $$
LANGUAGE plpgsql;
