def main():

    my_list:list[float] = [1,2,3,4]
    my_set: set[float] = {1,2,3,}
    my_tuple: tuple[float] = (1,2,3,4)
    my_dict: dict[str,float] = {'a':1.0}


    new_list = my_list.__add__([5])
    print(new_list)

if __name__ == "__main__":  # entry point do python
    main()


lista = []

for i in range(10):
        lista.append(i)
    
nova_lista = [number for number in range(10)]
nova_list_even = [number for number in range(100) if number % 2 is 0]
nova_list_even = (number for number in range(100) if number % 2 is 0)

for i in range(100):
     if i %2 is 0:
          nova_list_even.append(i)

print(list)
print(nova_lista)
print(nova_list_even)


