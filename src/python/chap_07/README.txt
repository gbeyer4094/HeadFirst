I had to use a completely different way to access the database because I'm using mysql 8.33 instead of 2.*.

CREATE USER 'vsearch' IDENTIFIED BY 'vsearchpassword';
GRANT ALL PRIVILEGES on vsearchlogDB.* TO 'vsearch' WITH GRANT OPTION;
FLUSH PRIVILEGES;

In mysql:
mysql> use vsearchlogdb
Database changed
mysql> create table log (
    -> id int auto_increment primary key,
    -> ts timestamp default current_timestamp,
    -> phrase varchar(128) not null,
    -> letters varchar(32) not null,
    -> ip varchar(16) not null,
    -> browser_string varchar(256) not null,
    -> results varchar(64) not null);
Query OK, 0 rows affected (0.02 sec)

In IDLE:
Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dbconfig = {'host':'127.0.0.1',
	    'user':'vsearch',
	    'password':'vsearchpassword',
	    'database':'vsearchlogdb',}
>>> import mysql.connector
>>> conn = mysql.connector.connect(**dbconfig)
>>> cursor = conn.cursor()
>>> _SQL = """show tables"""
>>> cursor.execute(_SQL)
>>> res = cursor.fetchall()
>>> res
[('log',)]
>>>

>>> _SQL = """describe log"""
>>> cursor.execute(_SQL)
>>> res = cursor.fetchall()
>>> res
[('id', 'int', 'NO', 'PRI', None, 'auto_increment'), ('ts', 'timestamp', 'YES', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED'), ('phrase', 'varchar(128)', 'NO', '', None, ''), ('letters', 'varchar(32)', 'NO', '', None, ''), ('ip', 'varchar(16)', 'NO', '', None, ''), ('browser_string', 'varchar(256)', 'NO', '', None, ''), ('results', 'varchar(64)', 'NO', '', None, '')]
>>> for row in res:
	print(row)


('id', 'int', 'NO', 'PRI', None, 'auto_increment')
('ts', 'timestamp', 'YES', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED')
('phrase', 'varchar(128)', 'NO', '', None, '')
('letters', 'varchar(32)', 'NO', '', None, '')
('ip', 'varchar(16)', 'NO', '', None, '')
('browser_string', 'varchar(256)', 'NO', '', None, '')
('results', 'varchar(64)', 'NO', '', None, '')

>>> _SQL = """insert into log
(phrase, letters, ip, browser_string, results)
values
('hitch-hiker', 'aeiou', '127.0.0.1', 'Firefox', "{'e', 'i'}")
"""
>>> cursor.execute(_SQL)
>>> conn.commit()
>>> _SQL="""select * from log"""
>>> cursor.execute(_SQL)
>>> for row in cursor.fetchall():
	print(row)


(1, datetime.datetime(2023, 7, 10, 17, 11, 51), 'hitch-hiker', 'aeiou', '127.0.0.1', 'Firefox', "{'e', 'i'}")

>>> cursor.close()
True
>>> conn.close()
>>>

I had to add a PATH for C:\Program Files\MySQL\MySQL Server 8.0\bin in order to get mqsql to work

[1] - C:\Users\gbeye\IdeaProjects\HeadFirst\src\python\chap_05\webapp

I ended up running the vsearch4web.py from a command prompt to get the database to work properly.
I opened the command prompt from the directory detailed above [1].
the database is now available using: mysql -u vsearch -p vsearchlogdb  the password is vsearchpassword.

