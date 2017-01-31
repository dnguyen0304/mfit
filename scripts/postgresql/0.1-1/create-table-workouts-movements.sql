DROP TABLE IF EXISTS workouts_movements;

CREATE TABLE workouts_movements (
	workout_movement_id			serial						PRIMARY KEY,
	workout_id					int				NOT NULL	REFERENCES workouts (workout_id),
	movement_id					int				NOT NULL	REFERENCES movements (movement_id),
	sets						smallint		NOT NULL,
	value						smallint		NOT NULL,
	workout_movement_unit_id	smallint		NOT NULL	REFERENCES workouts_movements_units (workout_movement_unit_id),
	sort_order					smallint		NOT NULL	DEFAULT 1,
	created_on					timestamp		NOT NULL	DEFAULT CURRENT_TIMESTAMP,
	created_by					int				NOT NULL,
	updated_on					timestamp,
	updated_by					int
);
