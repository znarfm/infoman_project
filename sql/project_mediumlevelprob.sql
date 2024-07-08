-- MEDIUM LEVEL PROBLEMS
-- 2 Problems from Novelle & Knight

-- Problem 1: List dependents under 18 years of age.
SELECT DepID, ReferenceCode, DepName, DepBirthdate, DATEDIFF(CURDATE(), DepBirthdate) / 365 AS Age
FROM dependent
WHERE DATEDIFF(CURDATE(), DepBirthdate) / 365 < 18;

-- Problem 2: Display the maximum number of SCs with each civil status.
SELECT CivilStatus, COUNT(*) AS StatusCount
FROM senior
GROUP BY CivilStatus;

-- Problem 3: Calculate the total income for each source type earned by SCs. 
-- Display also the minimum and maximum monthly income of the SCs.
SELECT SourceOfIncome, SUM(MonthlyIncome) AS TotalIncome, MAX(MonthlyIncome) AS MaxMonthlyIncome, MIN(MonthlyIncome) AS MinMonthlyIncome
FROM income
GROUP BY SourceOfIncome;

-- Problem 4: List SCs who have no spouse.
SELECT S.ReferenceCode, S.Name
FROM senior AS S
WHERE S.ReferenceCode IN (SELECT DISTINCT D.ReferenceCode FROM dependent AS D WHERE D.ReferenceCode = S.ReferenceCode)
AND (S.SpouseName IS NULL OR S.SpouseName = '');
