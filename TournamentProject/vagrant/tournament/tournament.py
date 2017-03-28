#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import traceback
from functools import partial


def connectionSafe(safe_func, database_name="tournament"):
    """Connect to the PostgreSQL database.

    Args:
        safe_func (func): a function with params db, cursor that
            runs sql statements on the database
        database_name: the database to connect to

    Returns:
        The sql results from the safe_func or None 
    """

    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        results = safe_func(db, cursor)
        db.close()
        return results
    except:
        print(traceback.format_exc())


def deleteMatches():
    """Remove all the match records from the database."""
    connectionSafe(__deleteMatchesSafe)


def deletePlayers():
    """Remove all the player records from the database."""
    connectionSafe(__deletePlayersSafe)


def countPlayers():
    """Returns the number of players currently registered."""
    return connectionSafe(__countPlayersSafe)


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    connectionSafe(partial(__registerPlayerSafe, name))


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    return connectionSafe(__playerStandingsSafe)


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    connectionSafe(partial(__reportMatchSafe, winner, loser))


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    results = [standings[i][:2] + standings[i + 1][:2]
               for i in xrange(0, len(standings), 2)]
    return results


# Safe functions are meant to be past as args to connectionSafe methods

def __deleteMatchesSafe(db, cursor):
    """Truncates the matches table safely

    This function should only be run within the connectionSafe function
    to catch any connection errors or database errors

    Args:
        db: the db connection
        cursor: the db cursor
    """
    cursor.execute("TRUNCATE matches CASCADE")
    db.commit()


def __deletePlayersSafe(db, cursor):
    """Truncates the players table safely

    This function should only be run within the connectionSafe function
    to catch any connection errors or database errors

    Args:
        db: the db connection
        cursor: the db cursor
    """
    cursor.execute("TRUNCATE players CASCADE")
    db.commit()


def __countPlayersSafe(db, cursor):
    """Counts the players that have been registered

    This function should only be run within the connectionSafe function
    to catch any connection errors or database errors

    Args:
        db: the db connection
        cursor: the db cursor

    Return:
        int: number of players in the players table
    """
    cursor.execute("SELECT COUNT(*) FROM players")
    return cursor.fetchone()[0]


def __registerPlayerSafe(name, db, cursor):
    """Registers a single player

    This function should only be run within the connectionSafe function
    to catch any connection errors or database errors

    Args:
        name: the name of the player
        db: the db connection
        cursor: the db cursor
    """
    sql = "INSERT INTO players (name) VALUES (%s)"
    params = (name, )
    cursor.execute(sql, params)
    db.commit()


def __playerStandingsSafe(db, cursor):
    """Gets the standings from the standings view

    This function should only be run within the connectionSafe function
    to catch any connection errors or database errors

    Args:
        db: the db connection
        cursor: the db cursor

    Return:
        A list of tuples, each of which contains (id, name, wins, matches)
    """
    cursor.execute("SELECT * FROM standings")
    return cursor.fetchall()


def __reportMatchSafe(winner, loser, db, cursor):
    """Registers a single match

    This function should only be run within the connectionSafe function
    to catch any connection errors or database errors

    Args:
        winner:  the id number of the player who won
        loser:  the id number of the player who lost
        db: the db connection
        cursor: the db cursor
    """
    sql = "INSERT INTO matches (winner, loser) VALUES (%s,%s)"
    params = (winner, loser)
    cursor.execute(sql, params)
    db.commit()
