# RedditPublicModLog

Disclaimer:
The code is trash, I'm not a dev, I'm a network admin.

This project uses the private RSS feed( available here : https://old.reddit.com/prefs/feeds/, take the JSON one next to "moderation log" under "moderation listing") of a reddit user to display the moderation logs of the subbreddits they're a part of.

This project used python, php. and mysqli, DataTables.

It consist of 4 files:

- dbtablesetup.py: Create the database and the table required, change YOUR_USER_HERE and YOUR_PASSWORD to your database user and password.
- jsonparser.py: Parse the what we got from the reddit link, extract the ID of the moderation action, the date, mod, action, details and calls functions in dbfowarder.py.
- dbfowarder.py: consist of two functions, one to check if the entry is not already stored into the database, and one that insert it into the database, change YOUR_USER_HERE and YOUR_PASSWORD to your database user and password.
- index.php: Do I really need to explain this one ? The actual web page where the data from the database is displayed, change YOUR_USER_HERE and YOUR_PASSWORD to your database user and password.

Installation:

-Install a database (I used MariaDB)
-Install a webserver, php, mysqli
-Put the 3 .py files wherever you want, change YOUR_USER_HERE and YOUR_PASSWORD to your database user and password in dbtablesetup.py and dbfowarder.py
-Run dbtablesetup
-Put the content of "web"  in /var/www/html
-Change YOUR_USER_HERE and YOUR_PASSWORD to your database user and password in index.php.
-setup a crontab for jsonparser.py, the delay between each execution depends on how frequently you want your database to be updated.
-go to your webpage and it's done.

