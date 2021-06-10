nested_dict = { 'dictA': {'key_1': 'value_1'},
                'dictB': {'key_2': 'value_2'}}
print(nested_dict)
for i,v in nested_dict.items():
    print(v)
nested_dict['dictC'] =  {'key_3': 'value_3'}
print(nested_dict) 
nested_dict['key'] = { ('value1,value2')}
print(nested_dict)
nested_dict['key_2'] = { ('value3,value4')}
nested_dict.popitem()
print(nested_dict)
nested_dict['set1'] = {(1, 2, 3)}
nested_dict['set2'] = {(1, 2, 3)}
print(nested_dict)
set_3 = set(nested_dict['set1'])
set_4 = set(nested_dict['set2'])
intersection = set_3.intersection(set_4)
print(intersection)
nested_dict['intersec'] = intersection
print(nested_dict)
