nested_dict = { 'dictA': {'key_1': 'value_1'},
                'dictB': {'key_2': 'value_2'}}
print(nested_dict)
#Q1-print the elements of nested dictionary.A-giving key and value
#in nested dict and printing elements 
for i,v in nested_dict.items():
    print(v)
#Q2-Add element to a Nested Dictionary,A-giving key in square brackets and assigning the value
nested_dict['dictC'] =  {'key_3': 'value_3'}
print(nested_dict) 
#Q3-Add another dictionary. A- Same as Q2
nested_dict['key'] = { ('value1,value2')}
print(nested_dict)
#Q4-Delete elements from a Nested Dictionary. A- using popitem to remove the last element
nested_dict.popitem()
print(nested_dict)
#Q5-Add a new dictionary  in the nested dictionary , A- same as Q2 
nested_dict['key_2'] = { ('value3,value4')}
print(nested_dict)
#Q6-Add a key {'set1': Set1 } whose value is a set and {'set2': Set2 } and print the intersection of Set1 and Set2
#A - First giving the nested dictionary the set dictionaries
nested_dict['set1'] = {(1, 2, 3)}
nested_dict['set2'] = {(1, 2, 3)}
print(nested_dict)
#then transforming the values to set
set_3 = set(nested_dict['set1'])
set_4 = set(nested_dict['set2'])
#then intersecting the values and printing it
intersection = set_3.intersection(set_4)
print(intersection)
#adding the intersected value as a dictionary
nested_dict['intersec'] = intersection
#printing the nested dictionary
print(nested_dict)
