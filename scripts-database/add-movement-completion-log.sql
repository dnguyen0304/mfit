CREATE OR REPLACE FUNCTION pg_temp.addMovementCompletion (
	userEmailAddress varchar(64),
	movementName varchar(32)
)
RETURNS void AS
$$
BEGIN
	INSERT INTO users_workouts_movements (
		user_workout_id,
		movement_id,
		sets_remaining,
		days_remaining,
		created_by
	)
	(
		WITH cte AS (
			-- Get the last log from today for the specified movement.
			SELECT
				users_workouts_movements.movement_id,
				MAX(users_workouts_movements.created_on) AS created_on
			FROM users_workouts_movements
			INNER JOIN users_workouts ON users_workouts.user_workout_id = users_workouts_movements.user_workout_id
			INNER JOIN users ON users.user_id = users_workouts.user_id
			INNER JOIN movements ON movements.movement_id = users_workouts_movements.movement_id
			WHERE
				users_workouts.ends_on > CURRENT_TIMESTAMP AND
				users.email_address = userEmailAddress AND
				movements.name = movementName AND
				users_workouts_movements.created_on > CURRENT_DATE
			GROUP BY users_workouts_movements.movement_id
		)
		SELECT
			users_workouts_movements.user_workout_id,
			users_workouts_movements.movement_id,
			users_workouts_movements.sets_remaining - 1 AS sets_remaining,
			date_part('day', age(users_workouts.ends_on, CURRENT_TIMESTAMP)) AS days_remaining,
			users_workouts.user_id AS created_by
		FROM users_workouts_movements
		INNER JOIN cte ON
			cte.movement_id = users_workouts_movements.movement_id AND
			cte.created_on = users_workouts_movements.created_on
		INNER JOIN users_workouts ON users_workouts.user_workout_id = users_workouts_movements.user_workout_id
		INNER JOIN users ON users.user_id = users_workouts.user_id
		WHERE
			users_workouts.ends_on > CURRENT_TIMESTAMP AND
			users.email_address = userEmailAddress
	);
END
$$
LANGUAGE plpgsql;
