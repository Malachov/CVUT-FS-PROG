# How to web app

## Flask

Flask is a python framework that allows you to create web app backend. You can create an API - expose some functionality on defined endpoints. Web application can have own frontend that uses that API, or you can send static HTML that browser can dispaly directly.

Flask alternatives are for example Django or Fast-api

[Flask dokumentace](https://flask.palletsprojects.com)

### Jinja

If you just want to serve static HTML pages, you can use templates and generate content via python with Jinja library.

### Run Flask app locally

## Deployment

If you just want to try it out, next steps are not necessary.

Deployment means bring an application to production, so users can use it.

## WSGI - Gunicorn

If you want to deploy Flask app, you need an interface se web server can run python application. Such a interface is WSGI - Web Server Gateway Interface. One concrete implementation is Gunicorn

[Gunicorn dokumentace](https://gunicorn.org/)

## Proxy server

Gunicorn is recomended to be used behind the proxy. You can use NGINX that case.

[NGINX dokumentace](https://www.nginx.com/)