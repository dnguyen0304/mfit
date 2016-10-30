CREATE OR REPLACE FUNCTION pg_temp.getActiveRoutine (
	usersEmailAddress varchar(64)
)
RETURNS TABLE (
	habits_name	varchar(32),
	sets		smallint,
	value		smallint,
	unit		varchar(16)
) AS
$$
BEGIN
	RETURN QUERY
	SELECT
		habits.name,
		routines.sets,
		routines.value,
		routines_units.name
	FROM routines
	INNER JOIN habits ON habits.id = routines.habits_id
	INNER JOIN routines_units ON routines_units.id = routines.routines_units_id
	INNER JOIN attempts ON attempts.habits_groups_id = routines.habits_groups_id
	INNER JOIN users ON users.id = attempts.users_id
	WHERE
		users.email_address = userEmailAddress AND
		attempts.starts_at <= CURRENT_TIMESTAMP AND
		attempts.ends_at > CURRENT_TIMESTAMP
	ORDER BY routines.sort_order ASC;
END
$$
LANGUAGE plpgsql;
