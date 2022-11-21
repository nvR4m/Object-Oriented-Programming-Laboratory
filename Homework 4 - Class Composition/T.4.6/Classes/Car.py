class Car:
    def __init__(self, producer, licence_plate, current_speed, top_speed, soft_arabesc):
        self.producer = producer
        self.licence_plate = licence_plate
        self.current_speed = current_speed
        self.top_speed = top_speed
        self.soft_arabesc = soft_arabesc

    def vizitaLaVericu(self):
        if self.soft_arabesc is False:
            self.soft_arabesc = True
            self.top_speed += 50
            print("Stage 2! You run fast now!")
        else: 
            print("You already have stage 2!")



    