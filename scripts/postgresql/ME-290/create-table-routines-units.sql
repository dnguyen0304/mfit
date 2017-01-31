DROP TABLE IF EXISTS routines_units;

CREATE TABLE routines_units (
	id			smallserial				PRIMARY KEY,
	name		varchar(16)	NOT NULL	UNIQUE,
	created_on	timestamp	NOT NULL	DEFAULT CURRENT_TIMESTAMP,
	created_by	int			NOT NULL,
	updated_on	timestamp,
	updated_by	int
);

INSERT INTO routines_units (
	name,
	created_by
)
VALUES
	('liters', -1),
	('repetitions', -1),
	('seconds', -1);
