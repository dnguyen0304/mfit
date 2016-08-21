DROP TABLE IF EXISTS users_workouts_movements;

CREATE TABLE users_workouts_movements (
	user_workout_movement_id	serial						PRIMARY KEY,
	user_workout_id				int							REFERENCES users_workouts (user_workout_id),
	movement_id					int							REFERENCES movements (movement_id),
	sets_remaining				smallint	NOT NULL,
	days_remaining				smallint	NOT NULL,
	created_on					timestamp	NOT NULL		DEFAULT CURRENT_TIMESTAMP,
	created_by					int			NOT NULL,
	updated_on					timestamp,
	updated_by					int
);
