Introduction
------------
This document adheres to the specifications outlined in [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

Source Control
--------------
### Commit Messages
- Issue IDs **must** be included.
```
# YES
git commit --message "PROJECT-1: foo"

# No
git commit --message "foo"
```

Database
--------
### Configuration
- The OS timezone **may** be "UTC".
- The database timezone **must** be "UTC".

### Naming Convention
- In general, lowercase_delimited_by_underscores **should** be used.
- Tables **must** be named with the plural form of their entity.
- Primary keys **must** be named `id`.
- Foreign keys **must** be named `<table_name>_id`.
```
-- YES
CREATE TABLE parents (
    id          serial              PRIMARY KEY,
    children_id int     NOT NULL    REFERENCES children (id)
);
```
- Tables describing one-to-many relationships **should** be named `<parent_table>_<child_table>`.
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

# Python
### Package Hierarchy
```
          Clients
API -----------------------
      Lambda Handlers
          |     |
    Services Views
     |        |
Repositories  |
           |  |
          Models
           |
          Interface Definitions
```

### General
- Import statements **should** be sorted to enforce import order.
- Intra-package import statements **should** use the explicit relative import form.
- Packages **must** have a `__all__` index in `__init__.py`.
- `__all__` indices **should** be sorted alphabetically.
- Modules **could** have a `__all__` index.

### Models
- New models **should** be added to the package index (i.e. `__init__.py`).

### Resources
- *How to Create a New Resource*
    - For singleton resources, in the `views` package, define a new `<resource_name>.py` module.
    - For singleton resources, in the package index (`views/__init__.py`), add a corresponding reference.
    - In the `resources` package, define a new `<resource_name>.py` module.
    - In the package index (`resources/__init__.py`), add a corresponding reference.
    - In the API index (`mfit/__init__.py`), add a corresponding reference.
    - For singleton resources, create a corresponding collection resource.
    - For collection resources, in the root resource's nested `subresources` object (`resources/root.py`), add a corresponding reference.
    - For sub-resources, in the parent resource's view's nested `subresources` object, add a corresponding reference.

### Endpoints
- Resource `id` URL variables **must** be named `id`.
```
# YES
/foo/<int:id>

# No
/foo/<int:foo_id>
```
- For sub-resources, parent resource `id` URL variables **must** be named `<resource_name>_id`.
```
# YES
/foo/<int:foo_id>/bar/<int:id>

# No
/foo/<int:id>
/foo/<int:id>/bar/<int:bar_id>
```