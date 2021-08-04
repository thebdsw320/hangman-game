def run():
    my_dict = {'first_name':'Andres', 'last_name':'Manuel'}
    my_list = [1, "Hello", True, 4.5]
    
    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-1, -2, 0, 1, 2],
        'floating_nums': [1, 1.1, 1.2, 1.5, 5.6]
    }

    for k, v in super_dict.items():
        print(k, '-', v)

def comprehension():  # Generates a list comprehension
    new_list = [n**2 for n in range(101)] # With the first 100 positive numbers squared 
    return new_list

if __name__ == '__main__':
    print(comprehension())