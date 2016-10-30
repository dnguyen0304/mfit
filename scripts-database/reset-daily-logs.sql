DO $$
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
			workouts_movements.sets,
			date_part('day', age(users_workouts.ends_on, CURRENT_TIMESTAMP)),
			-1
		FROM users_workouts
		INNER JOIN workouts_movements ON workouts_movements.workout_id = users_workouts.workout_id
		WHERE users_workouts.ends_on > CURRENT_TIMESTAMP
	);

	countAfter := (
		SELECT COUNT(*)
		FROM users_workouts_movements
	);

	RAISE INFO '% record(s) were inserted SUCCESSFULLY.', countAfter - countBefore;
END $$
LANGUAGE plpgsql;
