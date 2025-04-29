def function1(param):
     try:
         if not isinstance(param, basestring):
             raise ValueError("Parameter must be a string")
         return "Function 1 from module 1 with param: " + param
     except ValueError as e:
         return str(e)

print function1("test")
print function1(123)  # This will raise an error
