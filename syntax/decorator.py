# Decorator

def animalCall(func):
    def wrap():
        print("----------------")
        print("Running function '{}'".format(func.__name__))
        func()
        print("----------------")
    return wrap

def dogBark():
    print("Bark!")

@animalCall     #This is the decorator syntax candy
def catMiaow():
    print("Miaow~~~")

# animalCall(dogBark)()  #(1) call dogBark with animalCall
# dogBark()              #(2) call dogBark directly

animalCall(catMiaow)() #(3) call catMiaow with animalCall
catMiaow()             #(4) call catMiaow with animalCall
                       #when using this syntax candy, we don't call it like (3) anymore
                       #otherwise, it will be a recursive call 