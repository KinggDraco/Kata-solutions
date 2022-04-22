#Objective: Sort names by the first character in the last name using a lambda function. 

def sort_name(names):
    names.sort(key=lambda x: x.split(" ")[1])
    return names
