Log Analysis Project:

In this project students utilize sql to get data from a database consisting of several tables and data which must be aggregated into something which can be reported upon.  The objective is to help students improve upon their sql skills as well as get an introductory lesson in DB-api and python code.  The code provided uses views to help improve upon the performance of the sql queries.

Requirements:

• Python 3.5.3 - https://www.python.org/download/releases/3.0/
• VirtualBox - https://www.virtualbox.org/
• psycopg2 - http://initd.org/psycopg/
• Vagrant - https://www.vagrantup.com/
• Postgresql 9.6 - https://www.postgresql.org/
• VM Config File - https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip
• News Database Download link - https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip


Setting up VM after installing Virtual box, Vagrant, and downloading VM Config (pulled from Udacity:https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0 ):

Start the virtual machine
From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

Starting the Ubuntu Linux installation with `vagrant up`

When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!

Logging into the Linux VM with `vagrant ssh`.


Running the program:

• First load the 'news' data:
	psql -d news -f newsdata.sql

• Then Connect to the database
	psql -d news

• Create the views listed below

• Run the python code:
	python loganalysis.py


Views to Create:

--Requests View:
CREATE VIEW requests AS
SELECT
	time::date AS Day
	,COUNT(*)
FROM log
GROUP BY 
	time::date
ORDER BY 
time::date;

--Errors View:
CREATE VIEW errors AS
SELECT 
	time::date AS day
	,COUNT(*)
FROM log
WHERE 
	status != '200 OK'
GROUP BY 
	time::date
ORDER BY 
time::date;


--Error Rate View:
CREATE VIEW error_rate AS
SELECT 
	requests.day
	,errors.count::float / requests.count::float * 100 AS errorPercent
FROM requests
JOIN errors ON requests.day = errors.day;



