# Linux Config Project
> Udacity Fullstack Nanodegree Project 7

This project was to demonstrate how to configure a Ubuntu server that serves a WSGI Application through an Apache web server. The web app that the server is serving can be found in this [repo](../ItemCatalog/)



| Info |					|
| ---------- | -------------------------------------------------- |
| IP Address | 13.59.112.16                                    |
| URL        | [http://13.59.112.16.xip.io/](http://13.59.112.16.xip.io/catalogs)|



## Development
I used a single [AWS EC2](https://aws.amazon.com/ec2/) instance with Ubuntu 16.04.2 installed. The biggest problem that I encountered wasn't setting up the server with the grader user and the firewall, it was setting up the wsgi application. I started by reading the Flask documentation on [mod_wsgi](http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/) which made this alot simpler but I ran into a problem trying to setup Google's SignIn API.

## Dependencies
  * [AWS EC2](https://aws.amazon.com/ec2/)
  * [Ubuntu](https://www.ubuntu.com/server)
  * [Flask](http://flask.pocoo.org/)
  * [Postgres](https://www.postgresql.org/)
  * [Apache](https://httpd.apache.org/)

#### Notes
The website will only work correctly if you visit through the URL because the Google API will throw an error if you try to login in via the IP Address
