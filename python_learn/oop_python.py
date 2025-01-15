from numbers import Number
# class Lamp():
#     """
#     Create lamp with following parameters:
#     """
#     def __init__(self, status, brightness):
#         self.status = status
#         self.brightness = brightness

#     def print_info(self):
#         print(f'Brightness is {self.brightness}')
#         print(f'Status is {self.status}')

# lamp_1 = Lamp(False, 8)
# lamp_1.print_info()

class Electronic_device():
    def __init__(self, voltage, name):
        self.voltage = voltage
        self.name = name
    
    status = False

    def on(self):
        self.status = True
        print(f'Device {self.name} is working')

    def off(self):
        self.status = False
        print(f'Device {self.name} is stopped')
    
    def info(self):
        """
            Print info about device
        """
        print(f'{self.name.capitalize()} status if {self.status}')

class Lamp(Electronic_device):

    brightness = 0
    __count_turn_on = 0

    def turn_on(self):
        self.__count_turn_on += 1

    def show_counts_turn_on(self):
        return self.__count_turn_on
        

    def info(self):
        print(f'brightness is {self.brightness}')
    


class Cleaner(Electronic_device):
    type_of_cleaning = 'middle'

    def cleaning(self):
        if self.type_of_cleaning == 'middle' and self.status == True:
            print('djdjdjdj')
        if self.type_of_cleaning == 'hard':
            print('DJDJDJDJ')

new_lamp = Lamp('220v', 'lamp')
new_lamp.turn_on()
print(new_lamp.show_counts_turn_on())
new_lamp.turn_on()
print(new_lamp.show_counts_turn_on())
new_lamp.turn_on()
print(new_lamp.show_counts_turn_on())

# Перегрузка классов
class Simple_add_test():
    def __add__(self, n):
        print(f"Want to add {n}?")
        print(f"Don't do it!")

new_test_add = Simple_add_test()
b = new_test_add + 5

from numbers import Number

class MyNum(Number):
    def __init__(self, value):
        self.value = value
    def __iadd__(self, n):
        self.value += n
        return MyNum(self.value)
        
    def get_val(self):
        return self.value

n = MyNum(10)
n += 10
print(n.get_val())

# Очередь 
from queue import Queue
class MyQueue(Queue):
    def __init__(self):
        self.values = []

    def push(self, val):
        return self.values.append(val) 

    def front(self):
        if len(self.values) > 0:
            return self.values[0]

    def pop(self):
        if len(self.values) > 1:
            self.values = self.values[1:]
        else:
            self.values = []

# new_queue = MyQueue()
# new_queue.push(12)
# new_queue.push(25)
# print(new_queue.front())
# new_queue.pop()
# print(new_queue.front())
# new_queue.pop()
# print(new_queue.front())

# Neiron
class Neuron():
    def __init__(self, w, f = lambda x: x):
        self.w = w
        self.f = f
        self.prev_x = None

    def forward(self, x):
        self.prev_x = x
        return self.f(sum(map(lambda x, w: x * w, x, self.w)))


    def backlog(self):
        return self.prev_x

l = [4, 5, 6, 3, 4]
f = lambda x: x
x = [5, 2, 9, 4, 34]
y = [1, 4, 9, 3, 2]
new_n = Neuron(l, f)
print(new_n.backlog())
print(new_n.forward(x))
print(new_n.backlog())
print(new_n.forward(y))
print(new_n.backlog())


        
