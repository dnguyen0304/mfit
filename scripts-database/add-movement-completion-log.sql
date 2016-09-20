-- Log a movement set
INSERT INTO users_workouts_movements (
    user_workout_id,
    movement_id,
    sets_remaining,
    days_remaining,
    created_by
)
(
	WITH cte AS (
		SELECT
			users_workouts_movements.movement_id,
			MAX(users_workouts_movements.created_on) AS created_on
		FROM users_workouts_movements
		INNER JOIN users_workouts ON users_workouts.user_workout_id = users_workouts_movements.user_workout_id
		INNER JOIN users ON users.user_id = users_workouts.user_id
		INNER JOIN workouts ON workouts.workout_id = users_workouts.workout_id
		INNER JOIN movements ON movements.movement_id = users_workouts_movements.movement_id
		WHERE
			users.email_address = '' AND
			users_workouts.ends_on > CURRENT_TIMESTAMP AND
			workouts.name = '' AND
			movements.name = ''
		GROUP BY users_workouts_movements.movement_id
	)
    SELECT
        users_workouts_movements.user_workout_id,
        users_workouts_movements.movement_id,
        users_workouts_movements.sets_remaining - 1 AS sets_remaining,
		date_part('day', age(users_workouts.ends_on, CURRENT_TIMESTAMP)) AS days_remaining,
		users.user_id AS created_by
    FROM users_workouts_movements
	INNER JOIN cte ON
		cte.movement_id = users_workouts_movements.movement_id AND
		cte.created_on = users_workouts_movements.created_on
	INNER JOIN users_workouts ON users_workouts.user_workout_id = users_workouts_movements.user_workout_id
	INNER JOIN users ON users.user_id = users_workouts.user_id
	INNER JOIN workouts ON workouts.workout_id = users_workouts.workout_id
	WHERE
		users.email_address = '' AND
		users_workouts.ends_on > CURRENT_TIMESTAMP AND
		workouts.name = ''
);
