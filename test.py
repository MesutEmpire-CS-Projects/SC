
# new code
def rarest_age(d):
    # Count the frequency of each age using a dictionary
    age_freq = {}
    for age in d.values():
        if age in age_freq:
            age_freq[age] += 1
        else:
            age_freq[age] = 1
    
    # Find the rarest age(s) (i.e. the age(s) that occur least frequently)
    rarest_ages = []
    min_freq = float('inf')
    for age, freq in age_freq.items():
        if freq < min_freq:
            rarest_ages = [age]
            min_freq = freq
        elif freq == min_freq:
            rarest_ages.append(age)
    
    # Return one of the rarest ages (if there are ties)
    return rarest_ages[0]

# new code block
def range(list_of_lists):
    if not list_of_lists:
        return 0
    
    min_val = max_val = list_of_lists[0][0]
    for lst in list_of_lists:
        for val in lst:
            if val < min_val:
                min_val = val
            elif val > max_val:
                max_val = val
    
    return max_val - min_val + 1

