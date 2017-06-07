--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.3
-- Dumped by pg_dump version 9.6.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: users; Type: TABLE; Schema: public; Owner: yoogchu
--

CREATE TABLE users (
    id integer NOT NULL,
    username text NOT NULL,
    password text NOT NULL
);


ALTER TABLE users OWNER TO yoogchu;

--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: yoogchu
--

COPY users (id, username, password) FROM stdin;
1	asdf	asdf
\.


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: yoogchu
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (username);


--
-- PostgreSQL database dump complete
--

