# Tournament Project
> Udacity Fullstack Nanodegree Project 4

This project is a TDD (Test Driven development) where I was given a test file, and I had to create a PostgreSQL database and raw SQL queries that passed all the required tests. The queries that I had to create were INSERT, UPDATE, DELETE, JOIN, SELECT. The database consists of 2 tables (players, matches) and 1 view (standings). The tests can be found in the  [tournament_test.py](vagrant/tournament/tournament_test.py) file.

## Database Structure

```sql

CREATE TABLE IF NOT EXISTS players (
  id      SERIAL      PRIMARY KEY,
  name    VARCHAR(45) NOT NULL,
  created TIMESTAMP   NOT NULL      DEFAULT CURRENT_TIMESTAMP
);

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

```

## Installation
Create a VM and install all the python requirements by running
```sh
$ vagrant up
```

Connect to the newly created VM and create the database by running
```sh
$ vagrant ssh
$ cd /vagrant/tournament
$ psql

vagrant=> \i tournament.sql
```

Then you can run the tournament test by entering this command
```sh
$ python tournament_test.py
```


### Dependencies
* [Python 2.7](https://www.python.org/)
* [Vagrant](https://www.vagrantup.com/)
* [VirtualBox](https://www.virtualbox.org/wiki/VirtualBox)
