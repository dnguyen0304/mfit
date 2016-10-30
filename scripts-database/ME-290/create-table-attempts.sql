DROP TABLE IF EXISTS attempts;

CREATE TABLE attempts (
	id					serial					PRIMARY KEY,
	users_id			int			NOT NULL	REFERENCES users (id),
	habits_groups_id	int			NOT NULL	REFERENCES habits_groups (id),
	started_on			timestamp,
	ends_on				timestamp,
	created_on			timestamp	NOT NULL	DEFAULT CURRENT_TIMESTAMP,
	created_by			int			NOT NULL,
	updated_on			timestamp,
	updated_by			int
);
