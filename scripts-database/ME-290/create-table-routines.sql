DROP TABLE IF EXISTS routines;

CREATE TABLE routines (
	id					serial					PRIMARY KEY,
	habits_groups_id	int			NOT NULL	REFERENCES habits_groups (id),
	habits_id			int			NOT NULL	REFERENCES habits (id),
	sets				smallint	NOT NULL,
	value				smallint	NOT NULL,
	routines_units_id	smallint	NOT NULL	REFERENCES routines_units (id),
	sort_order			smallint	NOT NULL	DEFAULT 1,
	created_on			timestamp	NOT NULL	DEFAULT CURRENT_TIMESTAMP,
	created_by			int			NOT NULL,
	updated_on			timestamp,
	updated_by			int
);
