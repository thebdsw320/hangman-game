#  

def divisors(num):
    try:
        if num < 0 or num == 0:
            raise ValueError('Ingresa un numero entero positivo')    
        list_divisors = [n for n in range(1, num + 1) if num % n == 0]
        return list_divisors
    except ValueError as ve:
        print(ve)
        return False
        
def run():
    try:
        num = int(input('Ingresa un número: '))
        print(divisors(num=num))
    except ValueError:
        print('Ingresa un numero')

def palindrome(words):
        print(words == words[::-1])

if __name__ == '__main__':
    run()