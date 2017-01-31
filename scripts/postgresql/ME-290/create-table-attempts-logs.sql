DROP TABLE IF EXISTS attempts_logs;

CREATE TABLE attempts_logs (
	id				serial					PRIMARY KEY,
	attempts_id		int			NOT NULL	REFERENCES attempts (id),
	habits_id		int			NOT NULL	REFERENCES habits (id),
	sets_remaining	smallint	NOT NULL,
	created_on		timestamp	NOT NULL	DEFAULT CURRENT_TIMESTAMP,
	created_by		int			NOT NULL,
	updated_on		timestamp,
	updated_by		int
);
