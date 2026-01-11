# Apply two decorators: @bold and @italic to a string returning function
def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper
@bold
@italic
def name():
    return "Hello Krisna"
print(name())