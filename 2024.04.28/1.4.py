def repeat(func_obj):
    def wrapper(num: int = 2, *args, **kwargs):
        for i in range(num):
            func_obj(*args, **kwargs)
    return wrapper

        
@repeat
def testing_function():
    print('python')
    
# >>> testing_function()
# python
# python
# >>> testing_function(3)
# python
# python
# python
# >>> testing_function(4)
# python
# python
# python
# python