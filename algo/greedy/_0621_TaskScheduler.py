class Solution:
    
    # ==========================================================
    # Sort in every round (only array) [30%]
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        counter = [x[1] for x in counter.items()]
        counter.sort()
        time = 0
        print("start:", counter)
        
        # Outer loop (as long as largest is still not 0)
        while len(counter) > 0 and counter[-1] > 0:
            # Inner loop 
            # (1) Choose n+1 tasks starting from the largest occurance 
            # (2) Sort
            for i in range(n+1): 
                # All tasks are done because the largest is done already
                if counter[-1] == 0:
                    break
                # No task can be done in this timeslot (idle)
                if -1 - i < -len(counter) or counter[-1 - i] <= 0:
                    time += 1
                    continue
                counter[-1 - i] -= 1
                time += 1
                #print(time, i, counter)
            #print("sort:", counter)
            counter.sort()
        return time
            
    # ==========================================================
    # Heapify in every round [TLE]
    def leastInterval2(self, tasks: List[str], n: int) -> int:
        
        def getNextTask(idx):
            doneNum = 0
            #print(heapCounter)
            # for tupleTask in heapCounter:   #traversal doesn't guarentee the order
            
            while heapCounter:
                #print("loop")
                maxCountTask = heapq.heappop(heapCounter)
                task = maxCountTask[1][0]
                #print(task, counter[task])
                
                if counter[task] == 0:
                    doneNum += 1
                elif counter[task] > 0: 
                    if task not in taskToLastUse:
                        return task
                    if task in taskToLastUse and taskToLastUse[task] < idx - n: 
                        return task
                    
            #print("doneNum:", doneNum)
            if doneNum == len(counter):
                return None #done
            else:
                return -1   #idle 
            
        counter = collections.Counter(tasks)
        print(counter)

        heapCounter = [(-x[1], x) for x in counter.items()]
        heapq.heapify(heapCounter)
        
        taskToLastUse = {}
        taskSchedule = []
        
        idx = 0
        while True:
            nextTask = getNextTask(idx)
            
            #print("nextTask:", nextTask, counter)
            if not nextTask:
                return idx
            if nextTask != -1:
                counter[nextTask] -= 1
                taskToLastUse[nextTask] = idx
            
            heapCounter = [(-x[1], x) for x in counter.items()]
            heapq.heapify(heapCounter)
            taskSchedule.append(nextTask)
                #print(taskSchedule)
        
            idx += 1 
    
    # ==========================================================
    
    # Sort in every round [TLE]
    def leastInterval1(self, tasks: List[str], n: int) -> int:
        def getNextTask(idx):
            doneNum = 0
            for tup in sortedCounter:
                task = tup[0]
                #print(task, counter[task])
                if counter[task] == 0:
                    doneNum += 1
                elif counter[task] > 0: 
                    if task not in taskToLastUse:
                        return task
                    if task in taskToLastUse and taskToLastUse[task] < idx - n: 
                        return task
            #print("doneNum:", doneNum)
            if doneNum == len(counter):
                return None #done
            else:
                return -1   #idle 
            
        counter = collections.Counter(tasks)        
        taskToLastUse = {}
        taskSchedule = []
        sortedCounter = sorted(counter.items(), key = lambda x: -x[1]) 
        
        idx = 0
        while True:
            nextTask = getNextTask(idx)
            sortedCounter = sorted(counter.items(), key = lambda x: -x[1]) #sort every time...
            #print(nextTask, counter)
            if not nextTask:
                return idx
            if nextTask != -1:
                counter[nextTask] -= 1
                taskToLastUse[nextTask] = idx
                # tastSchedule.popleft()
                taskSchedule.append(nextTask)    
            idx += 1 
        