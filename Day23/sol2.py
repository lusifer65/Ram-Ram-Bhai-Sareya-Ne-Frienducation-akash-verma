class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,jobs,n):
        
        result_count, total_profit = 0, 0

        jobs = sorted(jobs, key=lambda x: x.profit, reverse=True)
        result = [0 for _ in range(n)]
        slot_occupied = [False for _ in range(n)]
    
        for i in range(n):
            for j in range(min(n, jobs[i].deadline)-1, -1, -1):
                if not slot_occupied[j]:
                    result[j] = i
                    slot_occupied[j] = True
                    break
    
        for i in range(n):
            if slot_occupied[i]:
                total_profit += jobs[result[i]].profit
                result_count += 1
    
        final_result = [result_count, total_profit]
        return final_result
