# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built-in functions.

def set_range(a,b,c):
    maxf = max(a,b,c)
    minif = min(a,b,c)
    range = maxf - minif
    return range
print (set_range(1,4,4))
