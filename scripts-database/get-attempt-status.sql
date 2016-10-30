CREATE OR REPLACE FUNCTION pg_temp.getAttemptStatus (
	usersEmailAddress varchar(64)
)
RETURNS TABLE (
	"date"			date,
	habits_name		varchar(32),
	sets_completed	smallint,
	sets_missed		smallint
) AS
$$
BEGIN
	RETURN QUERY
	WITH last_logs_by_day AS (
		SELECT
			MAX(attempts_logs.created_on) AS created_on,
			attempts_logs.habits_id
		FROM attempts_logs
		INNER JOIN attempts ON attempts.id = attempts_logs.attempts_id
		INNER JOIN users ON users.id = attempts.users_id
		WHERE
			attempts.starts_at <= CURRENT_TIMESTAMP AND
			attempts.ends_at > CURRENT_TIMESTAMP AND
			users.email_address = usersEmailAddress
		GROUP BY
			CAST(attempts_logs.created_on AS date),
			attempts_logs.habits_id
	)
		SELECT
			CAST(attempts_logs.created_on AS date),
			habits.name,
			routines.sets - attempts_logs.sets_remaining,
			attempts_logs.sets_remaining
		FROM attempts_logs
		INNER JOIN last_logs_by_day ON
			last_logs_by_day.created_on = attempts_logs.created_on AND
			last_logs_by_day.habits_id = attempts_logs.habits_id
		INNER JOIN attempts ON attempts.id = attempts_logs.attempts_id
		INNER JOIN routines ON routines.habits_id = attempts_logs.habits_id
		INNER JOIN habits ON habits.id = attempts_logs.habits_id
		ORDER BY
			CAST(attempts_logs.created_on AS date),
			routines.sort_order ASC;
END
$$
LANGUAGE plpgsql;
