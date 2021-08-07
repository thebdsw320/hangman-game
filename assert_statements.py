def divisors(num):
        list_divisors = [n for n in range(1, num + 1) if num % n == 0]
        return list_divisors
        
def run():
        num = input('Ingresa un número: ')
        assert num.isnumeric() and int(num) > 0, 'Ingresa un numero (positivo)'
        print(divisors(int(num)))

def palindrome(words):
        print(words == words[::-1])

if __name__ == '__main__':
    run()