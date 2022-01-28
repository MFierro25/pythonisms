import functools
import time

# dunder method examples

class Animal:
    # initiate object
    def __init__(self, type, name):
        self.type = type
        self.name = name
        
    # string representation of object    
    def __repr__(self):
        return f"I am a {self.type} my name is {self.name}"
    
    # return length of name
    def __len__(self):
        return len(self.name)

# decorator example

def slow_down(func):
    
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        value = func(*args, **kwargs)
        return value
    return wrapper_slow_down

# countdown using slow down decorator
@slow_down
def countdown(num):
    if num < 1:
        print('Go!')
    else:
        print(num)
        countdown(num - 1)
        
# generator example that doubles
def double(nums):
    for x in nums:
        yield x*2
                

    
if __name__ == '__main__':
    
    # create animal object
    kingKong = Animal('gorilla', 'King Kong')
    
    countdown(5)
        