ALTER TABLE habits_groups RENAME TO habit_groups;
ALTER SEQUENCE habits_groups_id_seq RENAME TO habit_groups_id_seq;
ALTER TABLE attempts RENAME COLUMN habits_groups_id TO habit_groups_id;
ALTER TABLE attempts RENAME CONSTRAINT attempts_habits_groups_id_fkey TO attempts_habit_groups_id_fkey;
ALTER TABLE routines RENAME COLUMN habits_groups_id TO habit_groups_id;
ALTER TABLE routines RENAME CONSTRAINT routines_habits_groups_id_fkey TO routines_habit_groups_id_fkey;
