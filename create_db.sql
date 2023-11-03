CREATE TABLE IF NOT EXISTS history(
   id_history SERIAL,
   analyze_date TIMESTAMP WITH TIME ZONE,
   validated BOOLEAN,
   PRIMARY KEY(id_history)
);

CREATE TABLE IF NOT EXISTS film(
   id_film SERIAL,
   title VARCHAR,
   stars_journalist VARCHAR(50),
   stars_spectators VARCHAR(50),
   release_date DATE,
   reference INT,
   id_history INT,
   PRIMARY KEY(id_film),
   FOREIGN KEY(id_history) REFERENCES history(id_history)
);

CREATE TABLE IF NOT EXISTS spectator_critics(
   id_spectator_critics SERIAL,
   text VARCHAR,
   stars VARCHAR(50),
   publication_date DATE,
   id_history INT,
   id_film INT NOT NULL,
   PRIMARY KEY(id_spectator_critics),
   FOREIGN KEY(id_history) REFERENCES history(id_history),
   FOREIGN KEY(id_film) REFERENCES film(id_film)
);

CREATE TABLE IF NOT EXISTS model_bert_bmus(
   id_bert SERIAL,
   five_stars VARCHAR(50),
   four_stars VARCHAR(50),
   three_stars VARCHAR(50),
   two_stars VARCHAR(50),
   one_stars VARCHAR(50),
   id_history INT,
   id_spectator_critics INT NOT NULL,
   PRIMARY KEY(id_bert),
   UNIQUE(id_spectator_critics),
   FOREIGN KEY(id_history) REFERENCES history(id_history),
   FOREIGN KEY(id_spectator_critics) REFERENCES spectator_critics(id_spectator_critics)
);

CREATE TABLE IF NOT EXISTS journalist_critics(
   id_journalist_critics SERIAL,
   text VARCHAR,
   stars VARCHAR(50),
   id_film INT NOT NULL,
   PRIMARY KEY(id_journalist_critics),
   FOREIGN KEY(id_film) REFERENCES film(id_film)
);

CREATE TABLE IF NOT EXISTS model_distilbert_bmcss(
   id_distilbert SERIAL,
   positive VARCHAR(50),
   negative VARCHAR(50),
   neutral VARCHAR(50),
   id_history INT,
   id_spectator_critics INT NOT NULL,
   PRIMARY KEY(id_distilbert),
   UNIQUE(id_spectator_critics),
   FOREIGN KEY(id_history) REFERENCES history(id_history),
   FOREIGN KEY(id_spectator_critics) REFERENCES spectator_critics(id_spectator_critics)
);
