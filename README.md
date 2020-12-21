# How To:

```sh
$ git clone https://github.com/alexlesan/quizl_game.git
$ cd quizl_game
$ python -m venv venv
```
Activate Environment

    For Windows: 
        $ venv\scripts\activate
    For Linux: 
        $ source venv/bin/activate

Continue with installing requirements and starting the server
The database is already migrated so no need to run migrations for now.

Rename the <code>.env.example</code> file to <code>.env</code> and update all constants values with right values.
```sh
$ pip install -r requirements.txt
$ python manage.py runserver
```