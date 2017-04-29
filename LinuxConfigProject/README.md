# Linux Config Project
A Udacity Fullstack Nanodegree project to demonstrate how to configure a Ubuntu server
that serves a WSGI Application through an Apache web server.



| Info |
| ---------- | -------------------------------------------------- |
| IP Address | 54.215.248.244                                     |
| URL        | ec2-54-215-248-244.us-west-1.compute.amazonaws.com |


### Resources
  * [AWS EC2](https://aws.amazon.com/ec2/)
  * [Ubuntu](https://www.ubuntu.com/server)
  * [Flask](http://flask.pocoo.org/)
  * [Postgres](https://www.postgresql.org/)
  * [Apache](https://httpd.apache.org/)


### Summary
I used a single [AWS EC2](https://aws.amazon.com/ec2/) instance with Ubuntu 16.04.2 installed. The biggest problem that I encountered wasn't setting up the server with the grader user and the firewall, it was setting up the wsgi application. I started by reading the Flask documentation on [mod_wsgi](http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/) which made this alot simpler but I ran into a problem trying to setup Googles SignIn API.   

#### Notes
The website will only work correctly if you visit through the URL because the Google API will throw an error if you try to login in via the IP Address
