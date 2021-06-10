# Alpaca_Bot
Alpaca bot is a new project working on developing bots which work
with the Alpaca API to make stock trades.
# Set Up
In order to setup this project, first create and then activate your venv:
```shell
python -m venv venv
source venv/bin/activate
```
Then run:
```shell
pip install -r requirements.txt
```
Next, we need to set up the database so run:
```shell
python manage.py makemigrations
python manage.py makemigrations bot_v1
python manage.py migrate
```
Now we will create a superuser to make development go more smoothly:
```shell
python manage.py createsuperuser
```
Finally, run:
```shell
python manage.py runserver
```
Now, if you have set up the project properly you can navigate to the
link provided by django in your terminal and if you add the path
/test/ to said link you should be greeted with a page saying 
'Hello, world'.

I order to be able to access the Alpaca API, we create a config file:
```shell
mkdir config
touch config/alpaca_config.py
```

Now in alpaca_config.py we add the API key and SECRET key for our account:
```python
API_KEY = "Your API key here"
SECRET_KEY = "Your secret key here"
```
# Contributing
Contributions are welcome on this repo in the forms of issues and 
pull requests.