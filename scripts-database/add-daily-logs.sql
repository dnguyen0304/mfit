CREATE OR REPLACE FUNCTION pg_temp.addDailyLogs(
	userEmailAddress varchar(64)
)
RETURNS smallint AS
$$
DECLARE
	countBefore integer;
	countAfter integer;
BEGIN
	countBefore := (
		SELECT COUNT(*)
		FROM users_workouts_movements
	);

	INSERT INTO users_workouts_movements (
		user_workout_id,
		movement_id,
		sets_remaining,
		days_remaining,
		created_by
	)
	(
		SELECT
			users_workouts.user_workout_id,
			workouts_movements.movement_id,
			workouts_movements.sets AS sets_remaining,
			date_part('day', age(users_workouts.ends_on, CURRENT_TIMESTAMP)) AS days_remaining,
			users.user_id AS created_by
		FROM users_workouts
		INNER JOIN workouts_movements ON workouts_movements.workout_id = users_workouts.workout_id
		INNER JOIN users ON users.user_id = users_workouts.user_id
		WHERE
			users_workouts.ends_on > CURRENT_TIMESTAMP AND
			users.email_address = userEmailAddress
	);

	countAfter := (
		SELECT COUNT(*)
		FROM users_workouts_movements
	);

	RETURN countAfter - countBefore;
END
$$
LANGUAGE plpgsql;
