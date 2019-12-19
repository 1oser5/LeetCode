SELECT Name AS Employee
FROM Employee e1
WHERE Salary > (SELECT Salary FROM Employee WHERE Id = e1.ManagerId)