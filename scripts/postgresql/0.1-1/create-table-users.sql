DROP TABLE IF EXISTS users;

CREATE TABLE users (
	user_id			serial						PRIMARY KEY,
	email_address	varchar(64)		NOT NULL	UNIQUE,
	first_name		varchar(32)		NOT NULL,
	last_name		varchar(32)		NOT NULL,
	created_on		timestamp		NOT NULL	DEFAULT CURRENT_TIMESTAMP,
	created_by		int				NOT NULL,
	updated_on		timestamp,
	updated_by		int
);
