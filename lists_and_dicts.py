def run():
    my_dict = {'first_name':'Andres', 'last_name':'Manuel'}
    my_list = [1, "Hello", True, 4.5]

    super_list = []

    for i in range(3):
        name_format = {'first_name': '','second_name':''}
        for key in name_format:
            val = input(key + ': ')
            name_format[key] = val
        super_list.append(name_format)

    return super_list
    
    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-1, -2, 0, 1, 2],
        'floating_nums': [1, 1.1, 1.2, 1.5, 5.6]
    }

    for k, v in super_dict.items():
        print(k, '-', v)

if __name__ == '__main__':
    runned = run()
    print(runned)