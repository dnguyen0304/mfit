DROP TABLE IF EXISTS workouts_movements_units;

CREATE TABLE workouts_movements_units (
	workout_movement_unit_id	smallserial					PRIMARY KEY,
	name						varchar(16)		NOT NULL	UNIQUE,
	created_on					timestamp		NOT NULL	DEFAULT CURRENT_TIMESTAMP,
	created_by					int				NOT NULL,
	updated_on					timestamp,
	updated_by					int
);
