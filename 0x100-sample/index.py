from unittest import result
import cs50
from sys import argv
import logging

# from PIL import Image, ImageFilter

# before = Image.open("IMG_7579.jpg")
# after = before.filter(ImageFilter.BoxBlur(10))
# after.save("out.jpg")


# ans = input("what's ur name\n")
# print(f"hello {ans}")


# x = cs50.get_int("x: ")
# y = int(input("y: "))
# print(x+y)


# ans = input("Do you agree?\n")
# if ans.lower() in ['y', 'yes']:
# 	print("Yes")
# elif ans.lower() in ['n', 'no']:
# 	print("No")
# else:
# 	raise ValueError("invalid input")


# scores = []

# for i in range(1,4):
# 	scores.append(int(input(f"score {i}: ")))
# avg = sum(scores) / len(scores)

# print(f"Average: {avg:.2f}")


# def safe_print(my_list_1, my_list_2):
#     new_list = []
#     list_len =len(my_list_1) + len(my_list_2)
#     for i in range(list_len ):
#         result = my_list_1[i] / my_list_2[i]
#         new_list.append(result)


# num1 = [1, 2, 3, 4, 5, 6]
# num2 = [7, 8, 9, 10, 11]
# safe_print(num1, num2)

num = [1,2,3,4,5]
print(type(num))
print(num)