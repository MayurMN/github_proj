from folder1.module1 import function1
from folder2.module2 import function2

def main():
    print function1("test")
    print function1(123)  # This will raise an error
    print function2(456)
    print function2("test")  # This will raise an error

if __name__ == "__main__":
    main()
