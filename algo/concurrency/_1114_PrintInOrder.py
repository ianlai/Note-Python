class Foo:
    def __init__(self):
        pass
        self.done1 = False
        self.done2 = False

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.done1 = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self.done1:
            continue
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.done2 = True

    def third(self, printThird: 'Callable[[], None]') -> None:
        while not (self.done1 and self.done2):
            continue
        # printThird() outputs "third". Do not change or remove this line.
        printThird()