def norm(v, p=2):
    # Step 1: Initialize a variable to store the sum
    total_sum = 0
    
    # Step 2: Loop through each element in the vector v
    for x in v:
        # Step 3: Compute the absolute value of the element and raise it to the power of p
        powered_value = abs(x) ** p
        
        # Step 4: Add the powered value to the total sum
        total_sum += powered_value
    
    # Step 5: Compute the p-th root of the total sum
    p_norm_value = total_sum ** p
    
    # Step 6: Return the computed p-norm value
    return p_norm_value

# Example usage:
v = [4, 3, 8, 9]

# Euclidean norm (default p=2)
euclidean_norm = norm(v)
print(f"Euclidean norm: {euclidean_norm}")  # Output: 5.0
