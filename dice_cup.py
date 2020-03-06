import sys 

for i in sys.stdin:
    # Split the input and convert it to integer
    NM = i.split()
    N = int(NM[0])
    M = int(NM[1])

sum_counter = {}
# Iterate through all combination of 2 dices
for n_value in range(1, N+1):
    for m_value in range(1, M+1):
    
        sum_values = n_value + m_value

        # Track how many times a sum appears 
        if sum_values in sum_counter:
            sum_counter[sum_values] += 1
        else:
            sum_counter[sum_values] = 1

# Check if sum_counter is empty 
if sum_counter:
    # Find the max times a particular sum appears
    max_val = max(sum_counter.values())
    for key, val in sum_counter.items():
        if val == max_val:
            # Print the most likely outcome for the sum
            print(key)
else:
    print(0)