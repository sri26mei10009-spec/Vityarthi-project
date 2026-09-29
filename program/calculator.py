from program.constants import SLAB_1_LIMIT, SLAB_2_LIMIT, RATE_1, RATE_2, RATE_3

def calculate_bill(units):
    """
    Calculates the electricity bill based on consumption slabs.
    Uses a list to store the cost incurred in each slab.
    """
    costs = [] 
    
    if units <= SLAB_1_LIMIT:
        costs.append(units * RATE_1)
        
    elif units <= SLAB_2_LIMIT:
        costs.append(SLAB_1_LIMIT * RATE_1)
        costs.append((units - SLAB_1_LIMIT) * RATE_2)
        
    else:
        costs.append(SLAB_1_LIMIT * RATE_1)
        costs.append((SLAB_2_LIMIT - SLAB_1_LIMIT) * RATE_2)
        costs.append((units - SLAB_2_LIMIT) * RATE_3)
        
    total_bill = sum(costs)
    return total_bill, costs
