SELECT id, movie, description, rating
FROM cinema
WHERE
description <> 'boring'
AND
id & 1
ORDER BY rating DESC;