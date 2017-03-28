# Tournament Project
This is the Tournament Results Project for Udacity's Fullstack Nanodegree. It is meant to show my SQL skills by creating
a PostgreSQL database. The database consist of 3 tables (players, matches, match_results). The match_results is a 
junction table of the players and matches tables. 

## Requirements
Tournament requires [Python 2.7](https://www.python.org/), [Vagrant](https://www.vagrantup.com/) and 
[VirtualBox](https://www.virtualbox.org/wiki/VirtualBox)

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
