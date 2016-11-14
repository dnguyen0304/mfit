Introduction
------------
This document adheres to the specifications outlined in [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

Database
--------
### Configuration
- The OS timezone **may** be "UTC".
- The database timezone **must** be "UTC".

### Naming Convention
- In general, lowercase_delimited_by_underscores **should** be used.
- Tables **must** be named with the plural form of their entity.
- Primary keys **must** be named "id".
- Foreign keys **must** be named <table_name> + "_id".
```
-- YES
CREATE TABLE parents (
    id          serial              PRIMARY KEY,
    children_id int     NOT NULL    REFERENCES children (id)
);
```
- Tables describing one-to-many relationships **should** be named <parent_table>_<child_table>.
- Tables describing many-to-many relationships **must** start a new naming convention hierarchy.
```
/* There are sibling A entities in the siblings_a table.
 * There are sibling B entities in the siblings_b table.
 */

-- YES
CREATE TABLE foo (
    id              serial              PRIMARY KEY,
    siblings_a_id   int     NOT NULL    REFERENCES siblings_a (id),
    siblings_b_id   int     NOT NULL    REFERENCES siblings_b (id),
);

-- No
CREATE TABLE siblings_a_siblings_b (
    id              serial              PRIMARY KEY,
    siblings_a_id   int     NOT NULL    REFERENCES siblings_a (id),
    siblings_b_id   int     NOT NULL    REFERENCES siblings_b (id),
);
```
- Tables with adjectives in their name **must** use the singular form of those adjectives.
```
/* The first table implies groups specifically for parent entities.
 * The second table implies a one-to-many relationship between parent entities
 * in the parents table and group entities in the parents_groups table.
 */

-- YES
CREATE TABLE parent_groups (
    id  serial  PRIMARY KEY
);

-- No
CREATE TABLE parents_groups (
    id  serial  PRIMARY KEY
);
```
- Hungarian notation **must not** be used.
```
-- YES
CREATE TABLE foo (
    created_at      timestamp with time zone    NOT NULL    DEFAULT CURRENT_TIMESTAMP
);

-- No
CREATE TABLE foo (
    created_date    timestamp with time zone    NOT NULL    DEFAULT CURRENT_TIMESTAMP
);
```

### Creating New Tables
- Tables **must** have a primary key.
- Primary keys **should** be surrogate keys.
```
-- YES
CREATE TABLE users (
    id              serial                  PRIMARY KEY,
    email_address   varchar(64) NOT NULL    UNIQUE
);

-- No
CREATE TABLE users (
    email_address   varchar(64)             PRIMARY KEY
);
```
- Tables **must** include metadata fields.
```
-- YES
CREATE TABLE users (
    id              serial                                  PRIMARY KEY,
    email_address   varchar(64)                 NOT NULL    UNIQUE
    created_at      timestamp with time zone    NOT NULL    DEFAULT CURRENT_TIMESTAMP,
    created_by      int                         NOT NULL,
    updated_at      timestamp with time zone,
    updated_by      int
);

-- No
CREATE TABLE users (
    id              serial                  PRIMARY KEY,
    email_address   varchar(64) NOT NULL    UNIQUE
);
```
- Column constraints **should** trend towards being restrictive.
- Data type constraints **should** trend towards being more relaxed.
- Datetime (data types that store both date and time) columns **must** include the time zone.