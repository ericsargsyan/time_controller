### Time Controller project is using
<a href="https://www.postgresql.org"><img height="64px" src="https://raw.github.com/MaccaTech/PostgresPrefs/master/PostgreSQL/Images/elephant.png"></a>
<a href="https://www.postgresql.org"><img height="40px" src="https://raw.github.com/MaccaTech/PostgresPrefs/master/PostgreSQL/Images/logo.png"></a>
### So before running server you should configure database yourself.
#### <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black">
After installing PostgreSQL and PgAdmin open terminal and type

```psql
sudo -u postgres psql
postgres=# create database mydb;
postgres=# create user myuser with encrypted password 'mypass';
postgres=# grant all privileges on database mydb to myuser;
```
#### <img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white">
It requires you to create while installing the app.

### After creating appropriate database open django settings and change database

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'userpassword',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
```
#### Don't forget to install psycopg2 in your enviroment
```terminal
pip install psycopg2-binary
```


# time_controller
Report in BI Server!

![Screenshot 2021-07-02 203816](https://user-images.githubusercontent.com/72858955/124305752-8c377280-db76-11eb-9131-754f15c63588.png)

