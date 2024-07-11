-- MEDIUM LEVEL PROBLEMS
-- 2 Problems from Novelle & Knight

-- Problem 1: Count the SCs suffering from each illness (concerndetails)
SELECT ConcernType, ConcernDetails, COUNT(*) AS NumberOfSeniors
FROM healthconcern
GROUP BY ConcernType, ConcernDetails
ORDER BY NumberOfSeniors DESC;

-- Problem 2: Display the maximum number of SCs with each civil status.
SELECT CivilStatus, COUNT(*) AS StatusCount
FROM senior
GROUP BY CivilStatus;

-- Problem 3: Calculate the total income for each source type earned by SCs. 
-- Display also the minimum and maximum monthly income of the SCs.
SELECT SourceOfIncome, SUM(MonthlyIncome) AS TotalIncome, MAX(MonthlyIncome) AS MaxMonthlyIncome, MIN(MonthlyIncome) AS MinMonthlyIncome
FROM income
GROUP BY SourceOfIncome;

-- Problem 4: List all SCs who have no spouse, but has someone dependent to them.
SELECT S.ReferenceCode, S.Name
FROM senior AS S
WHERE S.ReferenceCode IN (SELECT DISTINCT D.ReferenceCode FROM dependent AS D WHERE D.ReferenceCode = S.ReferenceCode)
AND (S.SpouseName IS NULL OR S.SpouseName = '');
