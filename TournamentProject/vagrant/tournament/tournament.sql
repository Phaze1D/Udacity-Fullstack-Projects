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

/*
* Creates the match results table
* Many to Many relationship between players and matches tables
*/
CREATE TABLE IF NOT EXISTS matches (
  id      SERIAL    PRIMARY KEY,
  winner  INTEGER   NOT NULL,
  loser   INTEGER   NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
          CONSTRAINT matches_winner_fkey FOREIGN KEY (winner)
            REFERENCES players ( id ) MATCH SIMPLE
            ON UPDATE NO ACTION ON DELETE CASCADE,
          CONSTRAINT matches_loser_fkey FOREIGN KEY (loser)
            REFERENCES players ( id ) MATCH SIMPLE
            ON UPDATE NO ACTION ON DELETE CASCADE
);

/* Creates the standings view */
CREATE VIEW standings AS
  SELECT
    players.id,
    players.name,
    COALESCE(SUM(CASE WHEN matches.winner = players.id THEN 1 ELSE 0 END), 0) AS wins, -- Case Statement converts boolean into 1 or 0
    COUNT(matches.id) AS matches
  FROM players LEFT JOIN matches
    ON matches.winner = players.id OR matches.loser = players.id
  GROUP BY players.id, players.name
  ORDER BY wins DESC
