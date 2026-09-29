from program.constants import SLAB_1, SLAB_2, RATE_1, RATE_2, RATE_3

def calculate_bill(units):
    costs = [] 
    if units <= SLAB_1:
        costs.append(units * RATE_1)
        
    elif units <= SLAB_2:
        costs.append(SLAB_1 * RATE_1)
        costs.append((units - SLAB_1) * RATE_2)
        
    else:
        costs.append(SLAB_1 * RATE_1)
        costs.append((SLAB_2 - SLAB_1) * RATE_2)
        costs.append((units - SLAB_2) * RATE_3)
        
    total_bill = sum(costs)
    return total_bill, costs
