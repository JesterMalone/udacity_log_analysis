
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