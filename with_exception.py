"""Example context managers"""
class ContextManager:
    def __init__(self) -> None:
        self.list = [*range(3)]
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is IndexError:
            print('Out of range!')
            print( exc_tb, exc_type, exc_value)
            print("But we'll keep going...")
            return True
        elif exc_type is not None:
            print('Trouble!')

#this = ContextManager()
with ContextManager() as this:
    for i in range(5):
        print(this.list[i])
    print("About to leave the 'with'.")
""" print("Still going. Let's be nice:")
with this:
    for n in this.list:
        print(n)
    print("About to leave the 'with'.")
print("Exited the 'with'.") """
with this:
    print("Let's make trouble...")
    x = this.list[1]/this.list[0]
print('Still?!')

""" print("Decorators!")
from contextlib import contextmanager

@contextmanager
def listing():
    print("Setting up the list")
    yield range(3)
    print("Done with the list")

with listing() as list:
    for n in list:
        print(n)

@contextmanager
def tough_list():
    print("We won't let errors stop us!")
    try:
        yield range(3)
    except IndexError as err:
        print("Out of range!")
        print(err)
    finally:
        print("Still going!")

with tough_list() as list:
    for i in range (5):
        print(list[i])
    print("About to leave the 'with'.")
print("Out of the 'with'.") """