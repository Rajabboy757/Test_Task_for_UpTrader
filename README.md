# Test_Task_for_UpTrader

To run this project please follow the steps below:

1.clone this repo

2.create the virtual environment and create **_.env_** file for environment variables<br>
(you can fill the variables by yourself)

3.install the required packages in requirements.txt

4.create the database in your PgAdmin and connect it with project or just use sqlite3

5.makemigrations and migrate

6.create superuser and **_python manage.py runserver_** <br>
then add menu items by this **_python .\manage.py create_menu_items_** management command <br>
(This command will work if your db is new or id in menu table starts from 1, else there will be a conflict)

7.open http://127.0.0.1:8000/menu/1 in your browser to check the menu



