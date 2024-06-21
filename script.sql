DELETE FROM TestTable Where NumberField = 4;

INSERT INTO TestTable (NumberField)
VALUES (3);

UPDATE TestTable
SET NumberField = 4
WHERE NumberField = 3;

SELECT * FROM TestTable;

SELECT * FROM TestTable WHERE BooleanField = True;

SELECT TextField FROM TestTable;