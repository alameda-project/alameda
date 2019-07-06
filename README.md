# alameda_api

![Build Status](https://travis-ci.com/matagus/alameda_api.svg)

## Overview

A very simple project managent tool built with Django & Bulma.io & Turbolinks, made in order to learn some of the new
Django 2.x features and specially Django Channels :)

Here are some screenshots:

![](https://github.com/matagus/alameda_api/raw/master/alameda_api/static/screenshots/stories-1.png)

![](https://github.com/matagus/alameda_api/raw/master/alameda_api/static/screenshots/stories-2.png)

![](https://github.com/matagus/alameda_api/raw/master/alameda_api/static/screenshots/stories-4.png)

![](https://github.com/matagus/alameda_api/raw/master/alameda_api/static/screenshots/epics-1.png)

![](https://github.com/matagus/alameda_api/raw/master/alameda_api/static/screenshots/sprints-1.png)

## Installation

1. Create a python 3.7.x virtual environment
2. Activate it
3. Install local requirements: `pip install -r requirements/local.txt`
4. Configure a rabbitmq server with the following credentials / setup: user=guest password=guest host=localhost port=5672 virtual host=/alameda_api.
5. Run: `honcho -f Procfile.local start`
7. Open your browser at `http://localhost:8000`.

## Deploying to heroku:

1. Install the heroku client: https://devcenter.heroku.com/articles/heroku-cli
2. Login using your credentials
3. Add the git remote: `git remote add heroku https://git.heroku.com/alameda_api-tool.git`
4. Profit!

Every time you want to deploy a new branch just do:

    git push heroku <branch-name>:master

To deploy master just do:

    git push heroku master

## Links

 * [Django-based web interface](https://alameda_api.alameda.dev/)
 * [API](https://alameda_api.alameda.dev/api/v1/)
 * [Admin](https://alameda_api.alameda.dev/admin/)


## Contribute

PRs accepted.

## License

[MPL](https://www.mozilla.org/en-US/MPL/)
