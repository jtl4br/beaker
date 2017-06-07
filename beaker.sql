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
-- Name: experiments; Type: TABLE; Schema: public; Owner: yoogchu
--

CREATE TABLE experiments (
    id integer NOT NULL,
    name text NOT NULL,
    product text NOT NULL,
    start_date date NOT NULL,
    end_date date NOT NULL,
    active boolean NOT NULL
);


ALTER TABLE experiments OWNER TO yoogchu;

--
-- Name: experiments_id_seq; Type: SEQUENCE; Schema: public; Owner: yoogchu
--

CREATE SEQUENCE experiments_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE experiments_id_seq OWNER TO yoogchu;

--
-- Name: experiments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yoogchu
--

ALTER SEQUENCE experiments_id_seq OWNED BY experiments.id;


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
-- Data for Name: experiments; Type: TABLE DATA; Schema: public; Owner: yoogchu
--

COPY experiments (id, name, product, start_date, end_date, active) FROM stdin;
1	01	gold	2017-06-06	2017-06-07	t
2	02	gold	2017-06-06	2017-06-07	t
3	03	silver	2017-06-05	2017-06-07	f
4	04	platinum	2017-06-06	2017-06-07	t
5	05	gold	2017-06-04	2017-06-05	t
6	06	silver	2017-06-04	2017-06-05	t
7	07	platinum	2017-06-04	2017-06-05	t
8	08	silver	2017-06-04	2017-06-05	t
9	09	platinum	2017-06-04	2017-06-05	t
10	010	silver	2017-06-04	2017-06-05	t
11	011	platinum	2017-06-04	2017-06-05	t
12	012	silver	2017-06-04	2017-06-05	t
13	013	gold	2017-06-04	2017-06-05	f
14	014	platinum	2017-06-04	2017-06-05	t
15	015	platinum	2017-06-04	2017-06-05	t
16	016	gold	2017-06-04	2017-06-05	f
17	017	gold	2017-06-04	2017-06-05	f
18	018	platinum	2017-06-04	2017-06-05	t
19	019	gold	2017-06-04	2017-06-05	f
\.


--
-- Name: experiments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yoogchu
--

SELECT pg_catalog.setval('experiments_id_seq', 19, true);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: yoogchu
--

COPY users (id, username, password) FROM stdin;
1	asdf	asdf
\.


--
-- Name: experiments experiments_pkey; Type: CONSTRAINT; Schema: public; Owner: yoogchu
--

ALTER TABLE ONLY experiments
    ADD CONSTRAINT experiments_pkey PRIMARY KEY (name);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: yoogchu
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (username);


--
-- PostgreSQL database dump complete
--

