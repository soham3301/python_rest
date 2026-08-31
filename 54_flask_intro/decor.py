import time

def delay_decor(input_function):
    def wrapper_function():
        print("1")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("3")
        time.sleep(1)
        input_function()
    return wrapper_function

@delay_decor
def say_hello():
    print("Hello")

@delay_decor
def say_goodbye():
    print("Good Bye")

@delay_decor
def ask_howare_you():
    print("Hey, How are you?")

say_goodbye()