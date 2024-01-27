class Solution:    
    
    def fractionalknapsack(self,W,Items,n):
        
        curr_weight = 0
        curr_value = 0  
    
       
        Items = sorted(Items, key = lambda x: (x.value/x.weight), reverse= True)
    
        
        for i in range(n):
            
            
            if curr_weight+Items[i].weight <= W: 
                curr_weight += Items[i].weight
                curr_value += Items[i].value
                
            
            else:
                accomodate = W-curr_weight 
                value_added = Items[i].value *(accomodate/Items[i].weight)
                curr_value += value_added
                break 
            
         
        return curr_value