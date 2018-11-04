
CREATE VIEW error_rate AS
SELECT 
	requests.day
	,errors.count::float / requests.count::float * 100 AS errorPercent
FROM requests
JOIN errors ON requests.day = errors.day;
