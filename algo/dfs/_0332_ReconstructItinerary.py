# https://medium.com/@ryanyang1221/leetcode-challenge-reconstruct-itinerary-6-28-b56cf6e2d73a

class Solution:
    
    # Backtracking (construct the graph first) [11%, 128 ms]
    # Handling the duplicates by removing the edges in the graph !! (neighter counter nor set is needed)
    
    def findItinerary(self, tickets):
        print("[2] Construct the graph first")
        
        # Construct the graph first
        graph = defaultdict(list)
        for flight in tickets:
            graph[flight[0]].append(flight[1])
            
        def dfs(currentItinerary, totalStops):
            startCity = currentItinerary[-1]
            if len(currentItinerary) == totalStops:
                return currentItinerary
            destinations = sorted(graph[startCity])  #Because we made the graph, we don't need another func to handle
            
            for dst in destinations:
                graph[startCity].remove(dst)
                currentItinerary.append(dst)
                result = dfs(currentItinerary, totalStops)
                if result:
                    return result
                currentItinerary.pop()
                graph[startCity].append(dst)
            return []
                
        return dfs(['JFK'], len(tickets) + 1)
    
    #====================================================

    # Backtracking + counter (can handle duplicated ticket) [5%, 376 ms]

    # Pass test case: 
    # [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],
    # ["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
    # Note: 2 tickets for ["TIA","ANU"]
    
    def findItinerary1(self, tickets: List[List[str]]) -> List[str]:
        print("[1] Can handle duplicated tickets (counter)")
        if not tickets:
            return []
        
        #used = set()
        used = defaultdict(int)   ## Use counter instead of set to handle duplicated tickets
        
        # Count the tickets before DFS
        for ticket in tickets:   
            used[tuple(ticket)] += 1
            
        itinerary = ["JFK"]
        self.dfs(tickets, itinerary, used)
        return itinerary
        
    def dfs(self, tickets, itinerary, used):
        if len(itinerary) == len(tickets) + 1:
            return True 
        curAirport = itinerary[-1]
        foundTickets = self.findTicketsBySrc(tickets, curAirport, used)
        #print(curAirport, foundTickets)
        
        for ticket in foundTickets:
            if used[tuple(ticket)] == 0:  ## Use counter instead of set to handle duplicated tickets
            # if tuple(ticket) in used:
                continue

            itinerary.append(ticket[1])  
            used[tuple(ticket)] -= 1      ## Use counter instead of set to handle duplicated tickets
            #used.add(tuple(ticket)) 
            
            if self.dfs(tickets, itinerary, used):
                return True 
            
            itinerary.pop()
            used[tuple(ticket)] += 1      ## Use counter instead of set to handle duplicated tickets
            #used.remove(tuple(ticket))
        return False

    def findTicketsBySrc(self, tickets, src, used):
        buffer = []
        for ticket in tickets:
            if ticket[0] == src:
                buffer.append(ticket)
        if len(buffer) == 1:
            return buffer
        else:
            buffer = sorted(buffer, key=lambda x: x[1])
            return buffer
        
    #====================================================

    # Backtracking + set (can handle unique ticket only) 
    
    # Pass test case: 
    # [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    def findItinerary0(self, tickets: List[List[str]]) -> List[str]:
        print("[0] Can't handle duplicated tickets (set)")
        if not tickets:
            return []
        
        used = set()    ##Set can't handle duplicated ticket
            
        itinerary = ["JFK"]
        self.dfs0(tickets, itinerary, used)
        return itinerary
        
    def dfs0(self, tickets, itinerary, used):
        if len(itinerary) == len(tickets) + 1:
            return True 
        
        curAirport = itinerary[-1]
        foundTickets = self.findTicketsBySrc0(tickets, curAirport, used)
        #print(curAirport, foundTickets)
        
        for ticket in foundTickets:
            if tuple(ticket) in used:   ##Set can't handle duplicated ticket
                continue

            itinerary.append(ticket[1]) 
            used.add(tuple(ticket))     ##Set can't handle duplicated ticket
            
            #print(">> ", itinerary)
            
            if self.dfs0(tickets, itinerary, used):
                return True 
            itinerary.pop()
            used.remove(tuple(ticket))  ##Set can't handle duplicated ticket 
        return False
            
    def findTicketsBySrc0(self, tickets, src, used):
        buffer = []
        for ticket in tickets:
            if ticket[0] == src:
                buffer.append(ticket)
        if len(buffer) == 1:
            return buffer
        else:
            buffer = sorted(buffer, key=lambda x: x[1])
            return buffer
            
