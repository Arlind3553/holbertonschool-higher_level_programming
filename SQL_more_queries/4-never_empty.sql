-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
CREATE id_not_null NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256),
	PRIMARY KEY (id)
	);
