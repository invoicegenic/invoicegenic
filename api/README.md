# Dependencies

- python: >= 3.7
- python-dotenv
- flask
- flask-sqlalchemy

## Optional Tools for Development

- autopep8
- pylint

# Setup

> ❗️ This setup assumes that you already have installed the `python3` in your own computer. If you haven't, please install the `python3` before continue.

> ℹ️ All of these commands below are for use in MacOS and Linux. If you use Windows, please make a PR to add more setup details as I don't own Windows devices.

## Preparation

Before we jump into the code, we should create a python virtual environment (`venv`) so this API project will have its own environment.

```bash
$ cd your_cloned_project/api

# Create virtual environment called venv
$ python3 -m venv venv

# Activate your venv
$ source venv/bin/activate
```

If no errors occured after you run the last command from the above, your terminal will prepend `(venv)` at the beginning of the input line, something like...

```bash
(venv) user@host api $
```

... which means you have successfully activated the virtual environment. Now let's install the packages we need to run this API project.

```bash
(venv) $ pip install python-dotenv flask flask-sqlalchemy

# Run the below command if you also want to install the optional dev packages
(venv) $ pip install autopep8 pylint
```

## Configuring Flask

_This step is purely optional_. If you need to configure Flask environment and options e.g change the dev server port, just copy and paste the `.flaskenv.sample` and rename the duplicate one into `.flaskenv`. Open that file and uncomment those lines that you want to use.

For example, if you want to change the dev server port from 5000 to 8088:

```
# .flaskenv

# Change from this...
#FLASK_RUN_PORT=5000

# ...to this
FLASK_RUN_PORT=8088
```

## Run API Dev Server

```bash
(venv) $ ./dev-run
```
