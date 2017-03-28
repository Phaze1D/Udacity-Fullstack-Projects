/* Connect to vagrant database before dropping the tournament database */
\c vagrant
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

\c tournament;

/* Creates the players table */
CREATE TABLE IF NOT EXISTS players (
  id      SERIAL      PRIMARY KEY,
  name    VARCHAR(45) NOT NULL,
  created TIMESTAMP   NOT NULL      DEFAULT CURRENT_TIMESTAMP
);

/* Creates the matches table */
CREATE TABLE IF NOT EXISTS matches (
  id      SERIAL    PRIMARY KEY,
  round   INTEGER   NOT NULL,
  created TIMESTAMP NOT NULL      DEFAULT CURRENT_TIMESTAMP
);

/*
* Creates the match results table
* Many to Many relationship between players and matches tables
*/
CREATE TABLE IF NOT EXISTS match_results (
  PRIMARY KEY (player_id, match_id),
  player_id INTEGER NOT NULL,
  match_id  INTEGER NOT NULL,
  won       BOOLEAN NOT NULL,
            CONSTRAINT match_results_player_id_fkey FOREIGN KEY (player_id)
              REFERENCES players ( id ) MATCH SIMPLE
              ON UPDATE NO ACTION ON DELETE CASCADE,
            CONSTRAINT match_results_match_id_fkey FOREIGN KEY (match_id)
              REFERENCES matches ( id ) MATCH SIMPLE
              ON UPDATE NO ACTION ON DELETE CASCADE
);

/* Creates the standings view */
CREATE VIEW standings AS
  SELECT
      players.id,
      players.name,
      COALESCE(SUM(CASE WHEN match_results.won THEN 1 ELSE 0 END), 0) AS wins, -- Case Statement converts boolean into 1 or 0
      COUNT(match_results.match_id) AS matches
  FROM players LEFT JOIN match_results
      ON match_results.player_id = players.id
  GROUP BY players.id, players.name
  ORDER BY wins DESC



-- This section includes matches that can result in a tie as well as a win or lose

-- CREATE TABLE IF NOT EXISTS match_results (
--   player_id integer NOT NULL,
--   match_id integer NOT NULL,
--   points integer NOT NULL CHECK (points >= 0 and points <= 2),
--   PRIMARY KEY (player_id, match_id),
--   CONSTRAINT match_results_player_id_fkey FOREIGN KEY (player_id)
--     REFERENCES players ( id ) MATCH SIMPLE
--     ON UPDATE NO ACTION ON DELETE CASCADE,
--   CONSTRAINT match_results_match_id_fkey FOREIGN KEY (match_id)
--     REFERENCES matches ( id ) MATCH SIMPLE
--     ON UPDATE NO ACTION ON DELETE CASCADE
-- );
--
--
-- CREATE VIEW standings AS
--   SELECT
--       players.id,
--       players.name,
--       COALESCE(SUM(CASE WHEN match_results.points=2 THEN 1 ELSE 0 END), 0) AS wins,
--       COALESCE(SUM(CASE WHEN match_results.points=1 THEN 1 ELSE 0 END), 0) AS ties,
--       COALESCE(SUM(CASE WHEN match_results.points=0 THEN 1 ELSE 0 END), 0) AS loses,
--       COALESCE(SUM(match_results.points, 0) AS points,
--       COUNT(match_results.match_id) AS matches
--   FROM players LEFT JOIN match_results
--       ON match_results.player_id = players.id
--   GROUP BY players.id, players.name
--   ORDER BY points DESC
