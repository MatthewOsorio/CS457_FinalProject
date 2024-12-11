--
-- PostgreSQL database dump
--

-- Dumped from database version 16.4
-- Dumped by pg_dump version 17.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: anime; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.anime (
    id bigint NOT NULL,
    title text NOT NULL,
    start_date date NOT NULL,
    genres text[],
    demographic character varying(30),
    studio_id uuid,
    img_id uuid
);


ALTER TABLE public.anime OWNER TO postgres;

--
-- Name: authors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.authors (
    id bigint NOT NULL,
    f_name character varying(50),
    l_name character varying(50)
);


ALTER TABLE public.authors OWNER TO postgres;

--
-- Name: images; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.images (
    id uuid NOT NULL,
    url character varying(75)
);


ALTER TABLE public.images OWNER TO postgres;

--
-- Name: manga; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.manga (
    id bigint NOT NULL,
    title text NOT NULL,
    start_date date NOT NULL,
    genres text[],
    demographic character varying(30),
    author_id bigint,
    img_id uuid
);


ALTER TABLE public.manga OWNER TO postgres;

--
-- Name: studios; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.studios (
    id uuid,
    name character varying(50) NOT NULL
);


ALTER TABLE public.studios OWNER TO postgres;

--
-- Name: user_anime; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_anime (
    user_id uuid NOT NULL,
    anime_id bigint NOT NULL
);


ALTER TABLE public.user_anime OWNER TO postgres;

--
-- Name: user_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_info (
    id uuid,
    f_name character varying(30),
    l_name character varying(30),
    email character varying(50) NOT NULL,
    password character varying(50)
);


ALTER TABLE public.user_info OWNER TO postgres;

--
-- Name: user_manga; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_manga (
    user_id uuid NOT NULL,
    manga_id bigint NOT NULL
);


ALTER TABLE public.user_manga OWNER TO postgres;

--
-- Name: anime anime_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.anime
    ADD CONSTRAINT anime_pkey PRIMARY KEY (id, title, start_date);


--
-- Name: authors authors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authors
    ADD CONSTRAINT authors_pkey PRIMARY KEY (id);


--
-- Name: authors authors_unique_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authors
    ADD CONSTRAINT authors_unique_key UNIQUE (id, f_name, l_name);


--
-- Name: images images_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.images
    ADD CONSTRAINT images_pkey PRIMARY KEY (id);


--
-- Name: manga manga_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.manga
    ADD CONSTRAINT manga_pkey PRIMARY KEY (id, title, start_date);


--
-- Name: studios studios_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.studios
    ADD CONSTRAINT studios_pkey PRIMARY KEY (name);


--
-- Name: anime unique_anime_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.anime
    ADD CONSTRAINT unique_anime_id UNIQUE (id);


--
-- Name: manga unique_manga_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.manga
    ADD CONSTRAINT unique_manga_id UNIQUE (id);


--
-- Name: studios unique_studio_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.studios
    ADD CONSTRAINT unique_studio_id UNIQUE (id);


--
-- Name: images url_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.images
    ADD CONSTRAINT url_key UNIQUE (url);


--
-- Name: user_anime user_anime_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_anime
    ADD CONSTRAINT user_anime_pkey PRIMARY KEY (user_id, anime_id);


--
-- Name: user_info user_info_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_info
    ADD CONSTRAINT user_info_id_key UNIQUE (id);


--
-- Name: user_info user_info_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_info
    ADD CONSTRAINT user_info_pkey PRIMARY KEY (email);


--
-- Name: user_manga user_manga_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_manga
    ADD CONSTRAINT user_manga_pkey PRIMARY KEY (user_id, manga_id);


--
-- Name: anime anime_img_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.anime
    ADD CONSTRAINT anime_img_id_fkey FOREIGN KEY (img_id) REFERENCES public.images(id);


--
-- Name: anime anime_studio_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.anime
    ADD CONSTRAINT anime_studio_id_fkey FOREIGN KEY (studio_id) REFERENCES public.studios(id);


--
-- Name: manga fk_author_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.manga
    ADD CONSTRAINT fk_author_id FOREIGN KEY (author_id) REFERENCES public.authors(id);


--
-- Name: manga manga_img_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.manga
    ADD CONSTRAINT manga_img_id_fkey FOREIGN KEY (img_id) REFERENCES public.images(id);


--
-- Name: user_anime user_anime_anime_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_anime
    ADD CONSTRAINT user_anime_anime_id_fkey FOREIGN KEY (anime_id) REFERENCES public.anime(id);


--
-- Name: user_anime user_anime_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_anime
    ADD CONSTRAINT user_anime_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.user_info(id);


--
-- Name: user_manga user_manga_manga_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_manga
    ADD CONSTRAINT user_manga_manga_id_fkey FOREIGN KEY (manga_id) REFERENCES public.manga(id);


--
-- Name: user_manga user_manga_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_manga
    ADD CONSTRAINT user_manga_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.user_info(id);


--
-- PostgreSQL database dump complete
--

