class Solution {
    public int lastStoneWeight(int[] stones) {
        Queue<Integer> q = new PriorityQueue<>((x, y) -> y - x);
        for(int e: stones){
            q.add(e);          
        }
        while(q.size() > 1){
            int m1 = q.poll();
            int m2 = q.poll();
            if(m1 - m2 > 0){
                q.add(m1 - m2);
            }
        }
        return q.size() > 0 ? q.peek() : 0;  
    }
}