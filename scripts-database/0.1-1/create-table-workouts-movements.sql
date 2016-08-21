DROP TABLE IF EXISTS workouts_movements;

CREATE TABLE workouts_movements (
	workout_movement_id			serial						PRIMARY KEY,
	workout_id					int							REFERENCES workouts (workout_id),
	movement_id					int							REFERENCES movements (movement_id),
	sort_order					smallint		NOT NULL	DEFAULT 1,
	sets						smallint		NOT NULL,
	value						smallint		NOT NULL,
	workout_movement_unit_id	smallint					REFERENCES workouts_movements_units (workout_movement_unit_id),
	created_on					timestamp		NOT NULL	DEFAULT CURRENT_TIMESTAMP,
	created_by					int				NOT NULL,
	updated_on					timestamp,
	updated_by					int
);
