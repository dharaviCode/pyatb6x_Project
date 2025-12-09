count = 0

def increment():
    global count #Making this variable global by using keyword "global"
    count = count + 1
    print(count)

increment()
increment()
increment()

