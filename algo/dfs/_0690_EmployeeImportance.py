"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        if id <= 0: 
            return 0
        
        targets = [id]
        emp = {employee.id:employee for employee in employees}  #dict
        importance = 0
        while targets:
            curId = targets.pop()
            index = 0 
            
            # Sol1: For loop
            # for i in range(len(employees)):
            #     if employees[i].id == curId:
            #         index = i
            
            # Sol2: Map
            curEmployee = emp[curId]
            importance += curEmployee.importance
            targets.extend(curEmployee.subordinates)
        
        return importance