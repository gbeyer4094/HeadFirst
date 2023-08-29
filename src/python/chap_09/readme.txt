from DBcm import UseDatabase
dbconfig = { 'host':'127.0.0.1', 'user':'vsearch', 'password':'vsearchpassword','database':'vsearchlogdb'}
with UseDatabase(dbconfig) as cursor:
    _SQL = """show tables"""
    cursor.execute(_SQL)
    data = cursor.fetchall()


Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from DBcm import UseDatabase
>>> dbconfig = {'host':'127.0.0.1',
KeyboardInterrupt
>>> dbconfig = { 'host':'127.0.0.1', 'user':'vsearch', 'password':'vsearchpassword','database':'vsearchlogdb'}
>>> with UseDatabase(dbconfig) as cursor:
...     _SQL = """show tables"""
...     cursor.execute(_SQL)
...     data = cursor.fetchall()
...
>>> data
[('log',)]
>>>
