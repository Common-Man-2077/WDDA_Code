SELECT DISTINCT title,date,nature_source,keywords,MAX(citations) AS max_citation
FROM bigquery-public-data.breathe.nature
WHERE citations IS NOT NULL AND EXTRACT(YEAR FROM date) = 2016
GROUP BY title,date,nature_source,keywords
ORDER BY LENGTH(max_citation) DESC,max_citation DESC
LIMIT 2000;

SELECT DISTINCT title,date,nature_source,keywords,MAX(citations) AS max_citation
FROM bigquery-public-data.breathe.nature
WHERE citations IS NOT NULL AND EXTRACT(YEAR FROM date) = 2017
GROUP BY title,date,nature_source,keywords
ORDER BY LENGTH(max_citation) DESC,max_citation DESC
LIMIT 2000;

SELECT DISTINCT title,date,nature_source,keywords,MAX(citations) AS max_citation
FROM bigquery-public-data.breathe.nature
WHERE citations IS NOT NULL AND EXTRACT(YEAR FROM date) = 2018
GROUP BY title,date,nature_source,keywords
ORDER BY LENGTH(max_citation) DESC,max_citation DESC
LIMIT 2000;

SELECT DISTINCT title,date,nature_source,keywords,MAX(citations) AS max_citation
FROM bigquery-public-data.breathe.nature
WHERE citations IS NOT NULL AND EXTRACT(YEAR FROM date) = 2019
GROUP BY title,date,nature_source,keywords
ORDER BY LENGTH(max_citation) DESC,max_citation DESC
LIMIT 2000;

SELECT DISTINCT title,date,nature_source,keywords,MAX(citations) AS max_citation
FROM bigquery-public-data.breathe.nature
WHERE citations IS NOT NULL AND EXTRACT(YEAR FROM date) = 2020
GROUP BY title,date,nature_source,keywords
ORDER BY LENGTH(max_citation) DESC,max_citation DESC
LIMIT 2000;