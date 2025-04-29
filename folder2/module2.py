def function2(param):
     try:
         if not isinstance(param, int):
             raise ValueError("Parameter must be an integer")
         return "Function 2 from module 2 with param: " + str(param)
     except ValueError as e:
         return str(e)

print function2(456)
print function2("test")  # This will raise an error
