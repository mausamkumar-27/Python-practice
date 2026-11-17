def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("Something is happening BEFORE the function runs")
        result=func(*args,**kwargs)
        print("Something is happening AFTER the function runs")
        return result
    return wrapper
@my_decorator
def say_hello(name):
    print(f"Hello,{name}")
say_hello("Mausam Kumar")