Log Analysis Project:

Questions:

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top
	
2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

Requirements:

• Python 3.5.3
• psycopg2
• Postgresql 9.6


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



