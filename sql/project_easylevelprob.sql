-- EASY LEVEL PROBLEMS
-- 2 Problems from Knight and 1 Problem from Novelle

-- Problem 1: Display all records of SCs not born in Manila City and Taguig City.
SELECT *
FROM senior
WHERE BirthPlace NOT LIKE 'Manila' AND BirthPlace NOT LIKE 'Taguig';

-- Problem 2: List dependents under 18 years of age.
SELECT DepID, ReferenceCode, DepName, DepBirthdate, DATEDIFF(CURDATE(), DepBirthdate) / 365 AS Age
FROM dependent
WHERE DATEDIFF(CURDATE(), DepBirthdate) / 365 < 18;

-- Problem 3: Compute SC's age (considering leap years)
SELECT ReferenceCode, Name, Birthdate, FLOOR(DATEDIFF(CURDATE(), Birthdate) / 365.25) AS Age
FROM senior;