class Solution:

    # Traverse 2D matrix (60%)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0 :
            return 0
        
        m, n = len(grid), len(grid[0])
        nextGrid = [x[:] for x in grid]
        
        #Traverse
        count = 0
        isChange = True 
        
        while(isChange):
            isChange = False 
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        if i-1 >= 0 and nextGrid[i-1][j] == 1:
                            nextGrid[i-1][j] = 2
                            isChange = True
                        if i+1 < m and nextGrid[i+1][j] == 1:
                            nextGrid[i+1][j] = 2
                            isChange = True
                        if j-1 >= 0 and nextGrid[i][j-1] == 1:
                            nextGrid[i][j-1] = 2
                            isChange = True
                        if j+1 < n and nextGrid[i][j+1] == 1:
                            nextGrid[i][j+1] = 2
                            isChange = True
                            
            grid = [x[:] for x in nextGrid] 
            count += 1 
        
        if self.checkAllRotten(grid): 
            return count-1
        return -1
    
    def checkAllRotten(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return False
        return True
    
# ============================        
# Java Implementation
# ============================
# class Solution {
#     public int orangesRotting(int[][] grid) {
#         int m = grid.length;
#         int n = grid[0].length;
#         if (m == 0 || n == 0){
#             return 0;
#         }
        
#         int[][] nextGrid = new int[m][n];
#         for(int i = 0; i < m; i++){
#             System.arraycopy(grid[i], 0, nextGrid[i], 0, n);    
#         }
        
#         int count = 0;
#         boolean isChange = true;
        
#         while(isChange){
#             isChange = false;
#             // print(grid);
#             // System.out.println();
            
#             for(int i = 0; i < m; i++){
#                 for(int j = 0; j < n; j++){
#                     if(grid[i][j] == 2){
#                         if (i-1 >= 0 && nextGrid[i-1][j] == 1){
#                             nextGrid[i-1][j] = 2;
#                             isChange = true;
#                         }
#                         if (i+1 < m && nextGrid[i+1][j] == 1){
#                             nextGrid[i+1][j] = 2;
#                             isChange = true;
#                         }
#                         if (j-1 >= 0 && nextGrid[i][j-1] == 1){
#                             nextGrid[i][j-1] = 2;
#                             isChange = true;
#                         }
#                         if (j+1 < n && nextGrid[i][j+1] == 1){
#                             nextGrid[i][j+1] = 2;
#                             isChange = true;
#                         }
#                     }
#                 }
#             }
#             for(int i = 0; i < m; i++){
#                 System.arraycopy(nextGrid[i], 0, grid[i], 0, n);    
#             }   
#             count++; 
#         }
#         if(checkAllRotten(grid)){
#             return count - 1;
#         }
#         return -1; 
#     }
#     public void print(int[][] grid){
#         int m = grid.length;
#         int n = grid[0].length;
#         for(int i = 0; i < m; i++){
#             for(int j = 0; j < n; j++){
#                 System.out.print(grid[i][j] + " ");
#             }
#             System.out.println();
#         }
#     }
#     public boolean checkAllRotten(int[][] grid){
#         int m = grid.length;
#         int n = grid[0].length;        
#         for(int i = 0; i < m; i++){
#             for(int j = 0; j < n; j++){
#                 if(grid[i][j] == 1){
#                     return false;
#                 }
#             }
#         }
#         return true;
#     }
# }
        