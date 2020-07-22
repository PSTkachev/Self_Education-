class Animals():
    def breathe(self):
        print('дышит')
        pass
    def move(self):
        print('двигается')
        pass
    def eat_food(self):
        print('ест')
        pass
class Mammals(Animals):
    def feed_young_with_milk(self):
        print('кормит детенышей молоком')
        pass
class Giraffes(Mammals):
    def __init__(self, spots): #стр. 107
        self.giraffe_spots = spots
        #Аргумент self дает функции класса
        #возможность вызывать другие функции этого класса
        #(а также классов-предков).   
    def eat_leaves_from_trees(self):
        print('ест листья')
        pass
    def find_food(self):
        self.move()
        print("Я нашел еду!")
        self.eat_food()
        print('ем')
    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()
    def left_foot_forward(self):
            print('левая нога вперед')
    
    def left_foot_back(self):
            print('левая нога назад')
            
    def right_foot_forward(self):
            print('правая нога вперед')
    
    def right_foot_back(self):
            print('правая нога назад')
    def dance(self):
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()
        
reginald = Giraffes(100)
print(reginald.giraffe_spots)
reginald.move()
reginald.find_food()
reginald.dance()
