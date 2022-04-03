# Album API &middot; [![Build Status](https://secure.travis-ci.org/TwP/inifile.png)](http://travis-ci.org/TwP/inifile) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/your/your-project/blob/master/LICENSE) [![Docker](https://img.shields.io/docker/automated/jrottenberg/ffmpeg.svg?maxAge=2592000)]()
=======

Python Flask application to store musical albums.

Description
-----------
The example flask app connects to a mysql db and redis instance to manage an album resource.

## Installing / Getting started

Here's a brief intro about what a developer must do in order to start developing
the project further:

```shell
mkdir albumservice
cd albumservice/
git clone https://github.com/VictorVelasquez90/albums_api.git
cd albums_api/
```

Add an app.ini file inside the albums_api directory and add data to reflect your mysql and redis environments

### Example File Format

A typical INI file might look like this:

    [mysql]
    db_user = root
    db_pass = change_to_refect_password
    db_host = db
    db_name = albums_api

    [redis]
    redis_host = cache
    redis_port = 6379
    redis_db = 0

### Add necessary environment variables

```sh
export DEBUG=True
export FLASK_SECRET_KEY=sifrxtwetsfwelug345sd
export FLASK_ENV=development
export DATABASE_PASS=change_to_refect_password
```
see: https://google.github.io/styleguide/shell.xml#Constants_and_Environment_Variable_Names

### Execute using docker compose:

```sh
docker compose build
docker compose up -d
```

### Otherwise, for the standalone web service:

```shell
pip install -r requirements.txt
python setup.py
```

Visit [http://localhost/api/album](http://localhost/api/album)