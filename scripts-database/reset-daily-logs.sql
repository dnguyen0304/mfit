DO $$
DECLARE
	countBefore integer;
	countAfter integer;
BEGIN
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
		INNER JOIN routines ON routines.habits_groups_id = attempts.habits_groups_id
		WHERE
			attempts.starts_at <= CURRENT_TIMESTAMP AND
			attempts.ends_at > CURRENT_TIMESTAMP
	);

	countAfter := (
		SELECT COUNT(*)
		FROM attempts_logs
	);

	RAISE INFO '% record(s) were inserted SUCCESSFULLY.', countAfter - countBefore;
END $$
LANGUAGE plpgsql;
