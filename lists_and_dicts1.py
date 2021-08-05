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
    new_list = [n**2 for n in range(1, 101) if n % 3 != 0] # With the first 100 positive numbers squared 
    return new_list

def comprehension_1():
    other_list = [n for n in range(1, 100000) if n % 36 == 0]
    return other_list

def dict_comprehension():
    new_dict = {n: n**3 for n in range(1, 101) if n % 3 == 0}
    return new_dict

def dict_comprehension1():
    new_dict1 = {n: round(n**.5, ndigits=3) for n in range(1, 101)}
    return new_dict1

if __name__ == '__main__':
    #print(comprehension())
    #print(comprehension_1())
    #print(dict_comprehension())
    print(dict_comprehension1())