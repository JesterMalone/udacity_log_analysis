
CREATE VIEW requests AS 
SELECT
	time::date AS Day
	,COUNT(*)
FROM log
GROUP BY 
	time::date
ORDER BY 
time::date;