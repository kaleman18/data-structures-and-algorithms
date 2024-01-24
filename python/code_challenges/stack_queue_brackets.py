from data_structures.queue import Queue


def multi_bracket_validation(str):
    
    stack = []

    #dictionary of true values
    lookup = {")":"(","}":"{","]":"["}

    # loop through the string
    for i in str:
        # if the index of the string matches one of the values in the lookup dictionary then append the string index
        if i in lookup.values():
            stack.append(i)
        # check if the stack returns true and the key of lookup matches 
        elif stack and lookup[i] == stack[-1]:
            stack.pop()
        else:
            return False
    
    if stack == []:
        return True
    else:
        return False


    
