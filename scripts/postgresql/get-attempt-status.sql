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
DECLARE
	currentDatetime	timestamp with time zone;
BEGIN
	currentDatetime := CURRENT_TIMESTAMP AT TIME ZONE 'localtime';

	RETURN QUERY
	WITH
		my_attempts_logs AS (
			SELECT
				attempts_logs.*,
				attempts_logs.created_at AT TIME ZONE 'localtime' AS local_created_at
			FROM attempts_logs
			INNER JOIN attempts ON attempts.id = attempts_logs.attempts_id
			INNER JOIN users ON users.id = attempts.users_id
			WHERE
				attempts.starts_at <= currentDatetime AND
				attempts.ends_at > currentDatetime AND
				users.email_address = usersEmailAddress
		),
		last_logs_by_day AS (
			SELECT
				MAX(my_attempts_logs.created_at) AS created_at,
				my_attempts_logs.habits_id
			FROM my_attempts_logs
			GROUP BY
				CAST(my_attempts_logs.local_created_at AS date),
				my_attempts_logs.habits_id
		)
	SELECT
		CAST(my_attempts_logs.local_created_at AS date) AS created_at,
		habits.name,
		routines.sets - my_attempts_logs.sets_remaining,
		my_attempts_logs.sets_remaining
	FROM my_attempts_logs
	INNER JOIN last_logs_by_day ON
		last_logs_by_day.created_at = my_attempts_logs.created_at AND
		last_logs_by_day.habits_id = my_attempts_logs.habits_id
	INNER JOIN routines ON routines.habits_id = my_attempts_logs.habits_id
	INNER JOIN habits ON habits.id = my_attempts_logs.habits_id
	ORDER BY
		CAST(my_attempts_logs.local_created_at AS date),
		routines.sort_order ASC;
END
$$
LANGUAGE plpgsql;
