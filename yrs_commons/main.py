class MyClass:
    def __init__(self):
        self.value = "Hello from MyClass!"
    
    def greet(self):
        return self.value

def my_function():
    return "Hello from my_function!"

def main():
    print("This runs when package is called from command line")
    
if __name__ == "__main__":
    main()
