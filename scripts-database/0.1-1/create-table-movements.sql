DROP TABLE IF EXISTS movements;

CREATE TABLE movements (
	movement_id		serial						PRIMARY KEY,
	name			varchar(32)		NOT NULL	UNIQUE,
	created_on		timestamp		NOT NULL	DEFAULT CURRENT_TIMESTAMP,
	created_by		int				NOT NULL,
	updated_on		timestamp,
	updated_by		int
);
