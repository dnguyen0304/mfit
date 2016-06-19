DROP TABLE IF EXISTS users_workouts_logs;

CREATE TABLE users_workouts_logs (
	user_workout_log_id		serial						PRIMARY KEY,
	user_workout_id			int							REFERENCES users_workouts (user_workout_id),
	daily_quota				smallint	NOT NULL,
	weekly_quota			smallint	NOT NULL,
	created_on				timestamp	NOT NULL		DEFAULT CURRENT_TIMESTAMP,
	created_by				int			NOT NULL,
	updated_on				timestamp,
	updated_by				int
);
