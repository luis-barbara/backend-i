def my_sum(*args):
    return sum(args)
  
numbers = (1,2,3,4,5)
result = my_sum(*numbers)
print(result)



def my_filtered_function(threshold, **kwargs):
    for key, value in kwargs.items():
        if value > threshold:
            print(f"{key}:{value}")
   

grades = {'John': 7.8, 'Mary': 9.0, 'Matt': 8.6, 'Michael': 9.5}

value=8.0
my_filtered_function(value, **grades)