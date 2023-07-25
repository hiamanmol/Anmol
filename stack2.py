from stack import ScreenInterface, Stack

def main():
    interface1 = ScreenInterface(title="App Home Page")
    interface2 = ScreenInterface(title="Product 1 page")
    interface3 = ScreenInterface(title="Product 2 page")

    stack = Stack()
    stack.push(interface1)    #-> HEAD
    stack.push(interface2)
    stack.push(interface3)    #-> TAIL

    stack.pop()
    stack.pop()
    stack.pop()

    stack.iterate()
    print("Stack :", vars(stack))
if __name__ == "__main__":
    main()


