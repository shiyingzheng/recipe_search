# Cookin - A Powerful Recipe Search Tool

## Setup

- Install python3

- Install postgres (psql) and related packages

        sudo apt-get install postgresql
        sudo apt-get install python-psycopg2
        sudo apt-get install libpq-dev

- Install Heroku CLI (Heroku toolbelt)

        wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh

- Install required packages

        pip3 install -r requirements.txt

- Now that you have postgres, create your local database, user, password. Make sure your user has the correct permissions to the new database.

- You will then need to make your own .env file according to the .env.sample.
The .env file stores environment variables necessary for the app to run locally, such as the name of the database.
On Heroku you can set the env vars at the app's settings page.


## Developing

To make migrations, do

    python manage.py makemigrations
    python manage.py migrate

You may run the interactive shell like this

    python3 manage.py shell

To run the app locally using heroku:

- collects static files

        python3 manage.py collectstatic

- run app

        heroku local


## Debugging

You can try both of the following for debugging when `heroku local` fails to boot worker

        python3 manage.py runserver
        web: gunicorn cookin.wsgi

To open and search the logs of the deployed app:

        heroku addons:open papertrail


### Style:

Set up your editor to use:

- 4-space tabs.
- No trailing whitespace.
- One trailing newline at the end of the file.

Keep lines < 80 characters.

Look at the existing file names and field names and follow naming conventions for clarity.


## Version Control

Please do not commit directly to the master branch, unless it's absolutely necessary and ok to do so.

Start a feature branch and do enough testing. When you're done, submit a pull request on github.

Use the following command to make a new branch:

        git checkout -b [new-branch-name]

To see the differences between the current branch you are on and origin/master, do:

        git diff origin/master

To merge changes in master to your current branch, do:

        git pull
        git merge master

When you're done committing all your changes, push the changes to your branch remotely:

        git push origin [branch-name]

Then you can go to github and submit a merge request by pressing the button

To view difference between two branches, do:

        git diff [branch1] [branch2]

For example, you can do:

        git diff origin/master origin/[my-branch]


## Deploying

Just use Heroku's deploy page and click the Github tab.

Run the following if you have made migrations, otherwise your tables won't exist:

        heroku run python manage.py syncdb

To open the app deployed on Heroku:

        heroku open

To open and search the logs of the deployed app:

        heroku addons:open papertrail

To experiment in the deployed app's environment in a python shell:

        heroku run python3 manage.py shell

If you ever need to reset the database...(hopefully not)

        heroku pg:reset postgres
        heroku run python manage.py syncdb


## Notes

Since we're on a free account the deployed app can only run 18 hours per day.

If it is idling Heroku will shut down the only Dyno (the worker process) that we've got.

When you visit the page Dyno will restart.

I think for our purpose 18 hours per day and one Dyno is enough, but we'll see.

