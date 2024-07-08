-- EASY LEVEL PROBLEMS
-- 2 Problems from Knight and 1 Problem from Novelle

-- Problem 1: Display all records of SCs not born in Manila City and Taguig City.
SELECT *
FROM senior
WHERE BirthPlace NOT LIKE 'Manila' AND BirthPlace NOT LIKE 'Taguig';

-- Problem 2: Count the SCs suffering from each illness(concerndetails)
SELECT ConcernType, ConcernDetails, COUNT(*) AS NumberOfSeniors
FROM healthconcern
GROUP BY ConcernType, ConcernDetails
ORDER BY NumberOfSeniors DESC;

-- Problem 3: Compute SC's age (considering leap years)
SELECT ReferenceCode, Name, Birthdate, FLOOR(DATEDIFF(CURDATE(), Birthdate) / 365.25) AS Age
FROM senior;