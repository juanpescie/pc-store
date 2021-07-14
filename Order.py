from Mouse import Mouse
from Monitor import Monitor
from Keyboard import Keyboard
from Computadora import Computer
class Order:
    order_counter = 0

    def __init__(self, computers):
        Order.order_counter += 1 
        self._id_order = Order.order_counter
        self._computers = list(computers)

    def add_computer(self, computer):
        self._computers.append(computer)
    
    def __str__(self):
        computers_str = ""
        for computer in self._computers:
            computers_str += f"{computer}"
        return f'''
Order {self._id_order}
    Computers:
        {computers_str}'''



m1 = Mouse("Genius", "USB")
k1 = Keyboard("Sony", "Inalambrico")
mon1 = Monitor("Sanyo",20)
k2 = Keyboard("dell", "USB")
m2 = Mouse("HP", "USB")
mon2 = Monitor("Samsung", 17)
computer1 = Computer("Razer", mon1, k1, m1)
computer2 = Computer("Samsung", mon2, k2, m2)
o1 = Order([computer1, computer2])
