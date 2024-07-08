-- HARD LEVEL PROBLEMS
-- 2 Problems from Novelle & 1 Problem from Knight

-- Problem 1: List seniors who have a total monthly income of more than Php 100,000 from all their income sources.
SELECT Name, SUM(MonthlyIncome) AS TotalIncome
FROM senior AS S, income as I
WHERE S.ReferenceCode = I.ReferenceCode
GROUP BY Name
HAVING SUM(MonthlyIncome) > 100000
ORDER BY TotalIncome DESC;

-- Problem 2: List the names of SCs and the total number of dependents who are not working, where the senior has more than two such dependents.
SELECT Name, COUNT(DepID) AS NonWorkingDependents
FROM senior AS S, dependent AS D
WHERE S.ReferenceCode = D.ReferenceCode AND DepIsWorking = '1'
GROUP BY Name
HAVING COUNT(DepID) >= 3;

-- Problem 3: Count bloodtype by sex and total.
SELECT BloodType, COUNT(CASE WHEN SexAtBirth = 'Male' THEN 1 END) AS MaleCount, COUNT(CASE WHEN SexAtBirth = 'Female' THEN 1 END) AS FemaleCount, COUNT(*) AS TotalCount
FROM senior
GROUP BY BloodType;