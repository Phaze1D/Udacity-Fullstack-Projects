# Catalog Project

Project for [Udacity Fullstack Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) that implements a simple catalog and items page. This project is mostly focuses on the backend implementation using the [Flask Framework](http://flask.pocoo.org/) and [SqlAlchemy ORM](https://www.sqlalchemy.org/). It also utilizes [Google's Sign In API](https://developers.google.com/identity/sign-in/web/server-side-flow) on both the backend and the frontend to maximize user security


### Getting Started
This project uses vagrant to install all dependencies but you have to have virtualbox install to run the vagrant file. After installing vagrant and virtualbox run theses commands inside this directory and open your browers to `localhost:8080`
```
$ vagrant up
$ vagrant ssh  
```

### Catalogs Routes
```
/catalogs                     GET
/catalog                      GET
/catalog                      POST
/catalog/<id>/edit            GET
/catalog/<id>/update          POST
/catalog/<id>                 GET
/api/catalogs                 GET
/api/catalog/<id>             GET
```

### Items Routes
```
/items                        GET
/item                         GET
/catalog/<catalog_id>/item    GET
/item                         POST
/item/<id>/edit               GET
/item/<id>/update             POST
/item/<id>                    GET
/item/<id>/delete             GET
/item/<id>/delete             POST
/api/items                    GET
/api/item/<id>                GET
```
