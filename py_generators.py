# # problem 1 :

def fibonacci_generator(n):
    a,b = 0,1
    count = 0
    while count < n :
        yield a
        a,b = b, a+b
        count += 1

for num in fibonacci_generator(10):
    print(num)

# # problem 2 :

def range_gen(n):
    current = 1
    while current <= n:
        yield current
        current += 1


for num in range_gen(5):
    print(num)


# # problem 3 :
def prime_generator(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
        
    current = 2
    while current <= n:
        if is_prime(current):
            yield current
        current += 1

for num in prime_generator(20):
    print(num, end=" ") 


# # problem 4 :
def char_counter(text):
    char_dict = {}
    
    for char in text:
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    
    for char, count in char_dict.items():
        yield char, count

text = "harsh mori"
for char, count in char_counter(text):
    print(f"'{char}': {count}")
