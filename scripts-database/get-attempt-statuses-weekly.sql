CREATE OR REPLACE FUNCTION pg_temp.getAttemptStatusesWeekly (
	userEmailAddress varchar(64)
)
RETURNS TABLE (
	workout			varchar(32),
	"date"			date,
	movement		varchar(32),
	sets_completed	smallint,
	sets_missed		smallint
) AS
$$
BEGIN
RETURN QUERY
WITH last_logs_by_day AS (
	SELECT
		MAX(users_workouts_movements.created_on) AS created_on,
		users_workouts_movements.movement_id
	FROM users_workouts_movements
	INNER JOIN users_workouts ON users_workouts.user_workout_id = users_workouts_movements.user_workout_id
	INNER JOIN users ON users.user_id = users_workouts.user_id
	WHERE
		users_workouts.ends_on > CURRENT_TIMESTAMP AND
		users.email_address = userEmailAddress
	GROUP BY
		CAST(users_workouts_movements.created_on AS date),
		users_workouts_movements.movement_id
)
	SELECT
		workouts.name,
		CAST(users_workouts_movements.created_on AS date),
		movements.name,
		workouts_movements.sets - users_workouts_movements.sets_remaining,
		users_workouts_movements.sets_remaining
	FROM users_workouts_movements
	INNER JOIN last_logs_by_day ON
		last_logs_by_day.created_on = users_workouts_movements.created_on AND
		last_logs_by_day.movement_id = users_workouts_movements.movement_id
	INNER JOIN users_workouts ON users_workouts.user_workout_id = users_workouts_movements.user_workout_id
	INNER JOIN workouts_movements ON
		workouts_movements.workout_id = users_workouts.workout_id AND
		workouts_movements.movement_id = users_workouts_movements.movement_id
	INNER JOIN workouts ON workouts.workout_id = users_workouts.workout_id
	INNER JOIN movements ON movements.movement_id = users_workouts_movements.movement_id
	ORDER BY
		CAST(users_workouts_movements.created_on AS date),
		workouts_movements.sort_order ASC;
END
$$
LANGUAGE plpgsql;
