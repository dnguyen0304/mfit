CREATE OR REPLACE FUNCTION pg_temp.getAttemptStatuses(
	userEmailAddress varchar(64)
)
RETURNS TABLE (
	workout_name	varchar(32),
	movement_name	varchar(32),
	sets_remaining	smallint,
	value			smallint,
	unit			varchar(16),
	days_remaining	double precision
) AS
$$
BEGIN
	RETURN QUERY
	WITH cte AS (
		-- Get the last log from today for each movement.
		SELECT
			users_workouts_movements.movement_id,
			MAX(users_workouts_movements.created_on) AS created_on
		FROM users_workouts_movements
		INNER JOIN users_workouts ON users_workouts.user_workout_id = users_workouts_movements.user_workout_id
		INNER JOIN users ON users.user_id = users_workouts.user_id
		WHERE
			users_workouts.ends_on > CURRENT_TIMESTAMP AND
			users.email_address = userEmailAddress AND
			users_workouts_movements.created_on > CURRENT_DATE
		GROUP BY users_workouts_movements.movement_id
	)
	SELECT
		workouts.name AS workout_name,
		movements.name AS movement_name,
		users_workouts_movements.sets_remaining,
		workouts_movements.value,
		workouts_movements_units.name AS unit,
		date_part('day', age(users_workouts.ends_on, CURRENT_TIMESTAMP)) AS days_remaining
	FROM users_workouts_movements
	INNER JOIN cte ON
		cte.movement_id = users_workouts_movements.movement_id AND
		cte.created_on = users_workouts_movements.created_on
	INNER JOIN users_workouts ON users_workouts.user_workout_id = users_workouts_movements.user_workout_id
	INNER JOIN workouts_movements ON
		workouts_movements.workout_id = users_workouts.workout_id AND
		workouts_movements.movement_id = users_workouts_movements.movement_id
	INNER JOIN workouts_movements_units ON workouts_movements_units.workout_movement_unit_id = workouts_movements.workout_movement_unit_id
	INNER JOIN workouts ON workouts.workout_id = users_workouts.workout_id
	INNER JOIN movements ON movements.movement_id = users_workouts_movements.movement_id
	ORDER BY workouts_movements.sort_order ASC;
END
$$
LANGUAGE plpgsql;
