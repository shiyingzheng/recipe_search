# Cookin - A Powerful Recipe Search Tool

## Setup

- Install python3

- Install postgres (psql) and related packages
        >sudo apt-get install postgresql
        >sudo apt-get install python-psycopg2
        >sudo apt-get install libpq-dev

- Install Heroku CLI (Heroku toolbelt)
        >wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh

- Install required packages
        >pip3 install requirements.txt

[add other steps that I might have forgotten here]

- Now that you have postgres, create your local database, user, password. Make sure your user has the correct permissions to the new database.

- You will then need to make your own .env file according to the .env.sample.
The .env file stores environment variables necessary for the app to run locally, such as the name of the database.
On Heroku you can set the env vars at the app's settings page.


## Developing

To run the app locally:

- collects static files
        >python3 manage.py collectstatic

- run app
        >heroku local


### Style:

Set up your editor to use:

- 4-space tabs.
- No trailing whitespace.
- One trailing newline at the end of the file.

Keep lines < 80 characters.


## Version Control

Please do not commit directly to the master branch, unless it's absolutely necessary and ok to do so.

Start a feature branch and do enough testing. When you're done, submit a pull request on github.


## Deploying

Let me talk about this later...

To open the app deployed on Heroku:
        >heroku open

To open and search the logs of the deployed app:
        >heroku addons:open papertrail

To experiment in the deployed app's environment in a python shell:
        >heroku run python3 manage.py shell


## Notes

Since we're on a free account the deployed app can only run 18 hours per day.

If it is idling Heroku will shut down the only Dyno (the worker process) that we've got.

When you visit the page Dyno will restart.

I think for our purpose 18 hours per day and one Dyno is enough, but we'll see.

