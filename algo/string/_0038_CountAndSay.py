class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 0:
            return 0
        
        string = "1"
        if n == 1:
            return string

        for i in range(2, n+1):
            count = 1
            nextStringArr = []
            
            # i==2
            if i==2:
                nextStringArr.append(str(count))
                nextStringArr.append(string)
                string = ''.join(nextStringArr)
                #print("i:", i, " -- ", string)
                continue
                
            # i>=3
            for j in range(1, len(string)):
                if j != len(string)-1:  #not last one
                    if string[j-1] == string[j]: 
                        count += 1
                    else:
                        nextStringArr.append(str(count))   
                        nextStringArr.append(string[j-1])
                        count = 1
                else:                   #last one 
                    if string[j-1] == string[j]: 
                        count += 1
                        nextStringArr.append(str(count))   
                        nextStringArr.append(string[j])
                        count = 1
                    else:
                        nextStringArr.append(str(count))   
                        nextStringArr.append(string[j-1])
                        count = 1
                        nextStringArr.append(str(1))   
                        nextStringArr.append(string[j])

            string = ''.join(nextStringArr)
            #print("i:", i, " -- ", string)
        return string 