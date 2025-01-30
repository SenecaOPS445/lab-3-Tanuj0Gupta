# def hello():
#     print('Hello World')
#     print('Inside a Function')
    

# my_stuff = hello()
# print('Stuff return from hello():',my_stuff)
# print('the object my_stuff is of type:',type(my_stuff))


# def return_text_value():
#     name = 'Terry'
#     greeting = 'Good Morning ' + name 
#     return greeting

# text = return_text_value()
# print(text)

# def square(number):
#     return number ** 2
# # print(square(5))
# # print(square(10))
# # print(square(12))
# # print(square(square(2)))
# # print(square('2'))

# def sum_numbers(number1, number2):
#     return int(number1) + int(number2)
# sum_numbers(5, 10)
# sum_numbers(50, 100)
# print(square(sum_numbers(5, 5)))

def describe_temperature(temp):
    if temp > 30:
        return 'hot'
    elif temp < 0:
        return 'cold'
    elif temp == 20:
        return 'perfect'
    return 'ok'

print(describe_temperature(50))
# Will return 'hot'
print(describe_temperature(20))
# Will return 'perfect'
print(describe_temperature(-50))
# Will return 'cold'
print(describe_temperature(25))
# Will return 'ok'
print(describe_temperature(10))
# Will return 'ok'