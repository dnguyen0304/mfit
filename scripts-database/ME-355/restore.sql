--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.5
-- Dumped by pg_dump version 9.5.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: attempts; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE attempts (
    id integer NOT NULL,
    users_id integer NOT NULL,
    habit_groups_id integer NOT NULL,
    starts_at timestamp with time zone,
    ends_at timestamp with time zone,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    created_by integer NOT NULL,
    updated_at timestamp with time zone,
    updated_by integer
);


--
-- Name: attempts_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE attempts_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: attempts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE attempts_id_seq OWNED BY attempts.id;


--
-- Name: attempts_logs; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE attempts_logs (
    id integer NOT NULL,
    attempts_id integer NOT NULL,
    habits_id integer NOT NULL,
    sets_remaining smallint NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    created_by integer NOT NULL,
    updated_at timestamp with time zone,
    updated_by integer
);


--
-- Name: attempts_logs_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE attempts_logs_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: attempts_logs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE attempts_logs_id_seq OWNED BY attempts_logs.id;


--
-- Name: habit_groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE habit_groups (
    id integer NOT NULL,
    name character varying(32) NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    created_by integer NOT NULL,
    updated_at timestamp with time zone,
    updated_by integer
);


--
-- Name: habit_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE habit_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: habit_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE habit_groups_id_seq OWNED BY habit_groups.id;


--
-- Name: habits; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE habits (
    id integer NOT NULL,
    name character varying(32) NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    created_by integer NOT NULL,
    updated_at timestamp with time zone,
    updated_by integer
);


--
-- Name: habits_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE habits_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: habits_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE habits_id_seq OWNED BY habits.id;


--
-- Name: routines; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE routines (
    id integer NOT NULL,
    habit_groups_id integer NOT NULL,
    habits_id integer NOT NULL,
    sets smallint NOT NULL,
    value smallint NOT NULL,
    routines_units_id smallint NOT NULL,
    sort_order smallint DEFAULT 1 NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    created_by integer NOT NULL,
    updated_at timestamp with time zone,
    updated_by integer
);


--
-- Name: routines_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE routines_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: routines_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE routines_id_seq OWNED BY routines.id;


--
-- Name: routines_units; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE routines_units (
    id smallint NOT NULL,
    name character varying(16) NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    created_by integer NOT NULL,
    updated_at timestamp with time zone,
    updated_by integer
);


--
-- Name: routines_units_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE routines_units_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: routines_units_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE routines_units_id_seq OWNED BY routines_units.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE users (
    id integer NOT NULL,
    email_address character varying(64) NOT NULL,
    first_name character varying(32) NOT NULL,
    last_name character varying(32) NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    created_by integer NOT NULL,
    updated_at timestamp with time zone,
    updated_by integer
);


--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE users_id_seq OWNED BY users.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY attempts ALTER COLUMN id SET DEFAULT nextval('attempts_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY attempts_logs ALTER COLUMN id SET DEFAULT nextval('attempts_logs_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY habit_groups ALTER COLUMN id SET DEFAULT nextval('habit_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY habits ALTER COLUMN id SET DEFAULT nextval('habits_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY routines ALTER COLUMN id SET DEFAULT nextval('routines_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY routines_units ALTER COLUMN id SET DEFAULT nextval('routines_units_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY users ALTER COLUMN id SET DEFAULT nextval('users_id_seq'::regclass);


--
-- Name: attempts_logs_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY attempts_logs
    ADD CONSTRAINT attempts_logs_pkey PRIMARY KEY (id);


--
-- Name: attempts_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY attempts
    ADD CONSTRAINT attempts_pkey PRIMARY KEY (id);


--
-- Name: habits_groups_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY habit_groups
    ADD CONSTRAINT habits_groups_name_key UNIQUE (name);


--
-- Name: habits_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY habit_groups
    ADD CONSTRAINT habits_groups_pkey PRIMARY KEY (id);


--
-- Name: habits_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY habits
    ADD CONSTRAINT habits_name_key UNIQUE (name);


--
-- Name: habits_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY habits
    ADD CONSTRAINT habits_pkey PRIMARY KEY (id);


--
-- Name: routines_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY routines
    ADD CONSTRAINT routines_pkey PRIMARY KEY (id);


--
-- Name: routines_units_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY routines_units
    ADD CONSTRAINT routines_units_name_key UNIQUE (name);


--
-- Name: routines_units_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY routines_units
    ADD CONSTRAINT routines_units_pkey PRIMARY KEY (id);


--
-- Name: users_email_address_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_email_address_key UNIQUE (email_address);


--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: attempts_habit_groups_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY attempts
    ADD CONSTRAINT attempts_habit_groups_id_fkey FOREIGN KEY (habit_groups_id) REFERENCES habit_groups(id);


--
-- Name: attempts_logs_attempts_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY attempts_logs
    ADD CONSTRAINT attempts_logs_attempts_id_fkey FOREIGN KEY (attempts_id) REFERENCES attempts(id);


--
-- Name: attempts_logs_habits_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY attempts_logs
    ADD CONSTRAINT attempts_logs_habits_id_fkey FOREIGN KEY (habits_id) REFERENCES habits(id);


--
-- Name: attempts_users_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY attempts
    ADD CONSTRAINT attempts_users_id_fkey FOREIGN KEY (users_id) REFERENCES users(id);


--
-- Name: routines_habit_groups_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY routines
    ADD CONSTRAINT routines_habit_groups_id_fkey FOREIGN KEY (habit_groups_id) REFERENCES habit_groups(id);


--
-- Name: routines_habits_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY routines
    ADD CONSTRAINT routines_habits_id_fkey FOREIGN KEY (habits_id) REFERENCES habits(id);


--
-- Name: routines_routines_units_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY routines
    ADD CONSTRAINT routines_routines_units_id_fkey FOREIGN KEY (routines_units_id) REFERENCES routines_units(id);


--
-- Name: public; Type: ACL; Schema: -; Owner: -
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- Name: attempts; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE attempts FROM PUBLIC;
REVOKE ALL ON TABLE attempts FROM duyn_su;
GRANT ALL ON TABLE attempts TO duyn_su;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE attempts TO mfit;


--
-- Name: attempts_id_seq; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON SEQUENCE attempts_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE attempts_id_seq FROM duyn_su;
GRANT ALL ON SEQUENCE attempts_id_seq TO duyn_su;
GRANT USAGE ON SEQUENCE attempts_id_seq TO mfit;


--
-- Name: attempts_logs; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE attempts_logs FROM PUBLIC;
REVOKE ALL ON TABLE attempts_logs FROM duyn_su;
GRANT ALL ON TABLE attempts_logs TO duyn_su;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE attempts_logs TO mfit;


--
-- Name: attempts_logs_id_seq; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON SEQUENCE attempts_logs_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE attempts_logs_id_seq FROM duyn_su;
GRANT ALL ON SEQUENCE attempts_logs_id_seq TO duyn_su;
GRANT USAGE ON SEQUENCE attempts_logs_id_seq TO mfit;


--
-- Name: habit_groups; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE habit_groups FROM PUBLIC;
REVOKE ALL ON TABLE habit_groups FROM duyn_su;
GRANT ALL ON TABLE habit_groups TO duyn_su;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE habit_groups TO mfit;


--
-- Name: habit_groups_id_seq; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON SEQUENCE habit_groups_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE habit_groups_id_seq FROM duyn_su;
GRANT ALL ON SEQUENCE habit_groups_id_seq TO duyn_su;
GRANT USAGE ON SEQUENCE habit_groups_id_seq TO mfit;


--
-- Name: habits; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE habits FROM PUBLIC;
REVOKE ALL ON TABLE habits FROM duyn_su;
GRANT ALL ON TABLE habits TO duyn_su;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE habits TO mfit;


--
-- Name: habits_id_seq; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON SEQUENCE habits_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE habits_id_seq FROM duyn_su;
GRANT ALL ON SEQUENCE habits_id_seq TO duyn_su;
GRANT USAGE ON SEQUENCE habits_id_seq TO mfit;


--
-- Name: routines; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE routines FROM PUBLIC;
REVOKE ALL ON TABLE routines FROM duyn_su;
GRANT ALL ON TABLE routines TO duyn_su;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE routines TO mfit;


--
-- Name: routines_id_seq; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON SEQUENCE routines_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE routines_id_seq FROM duyn_su;
GRANT ALL ON SEQUENCE routines_id_seq TO duyn_su;
GRANT USAGE ON SEQUENCE routines_id_seq TO mfit;


--
-- Name: routines_units; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE routines_units FROM PUBLIC;
REVOKE ALL ON TABLE routines_units FROM duyn_su;
GRANT ALL ON TABLE routines_units TO duyn_su;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE routines_units TO mfit;


--
-- Name: routines_units_id_seq; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON SEQUENCE routines_units_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE routines_units_id_seq FROM duyn_su;
GRANT ALL ON SEQUENCE routines_units_id_seq TO duyn_su;
GRANT USAGE ON SEQUENCE routines_units_id_seq TO mfit;


--
-- Name: users; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE users FROM PUBLIC;
REVOKE ALL ON TABLE users FROM duyn_su;
GRANT ALL ON TABLE users TO duyn_su;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE users TO mfit;


--
-- Name: users_id_seq; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON SEQUENCE users_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE users_id_seq FROM duyn_su;
GRANT ALL ON SEQUENCE users_id_seq TO duyn_su;
GRANT USAGE ON SEQUENCE users_id_seq TO mfit;


--
-- PostgreSQL database dump complete
--

