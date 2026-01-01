'''# Loop 10,000 times and add a character to a string using s += "a".
deep dive : strings are immutable. Everytime you do  +=, python distroyed the old string and create a brand new 
larger one in a new memory address. fix: use "".join(list_of_char)

'''
def add_char(old_string,char):
    old_size = len(old_string)
    new_size = old_size + 1

    new_memory = malloc(new_size)

    for i in range(old_size):
        new_memory[i] = old_string[i]

    new_memory[old_size] = char
    return "".join(new_memory)
def malloc(new_size):
    return ['']*new_size
def main():
    old_string = "My name is Sharna"
    char = '.'
    print(add_char(old_string,char))
main()
