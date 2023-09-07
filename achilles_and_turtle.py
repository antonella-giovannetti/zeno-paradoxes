class Runner:
    def __init__(self, name, position, speed):
        self.name = name
        self.position = position
        self.speed = speed
    def move(self, time):
        self.position += self.speed * time
    def __str__(self):
        return f"Position of {self.name} : {self.position}"

def achilles_and_turtle():
    achilles = Runner("Achilles", 0, 10)
    turtle = Runner("Turtle", 100, 1)
    it = 20
    first_time = True
    print("Achilles and the turtle")
    print("Initial State : ")
    print(achilles)
    print(turtle)
    for i in range(it):
        achilles.move(1)
        turtle.move(1)
        print(i + 1)
        print(achilles)
        print(turtle)
        if achilles.position > turtle.position and first_time:    
            print("Achilles to catch up to the turtle !")
            first_time = False
        if achilles.position > turtle.position and first_time:
            print("Achilles is at same level as the turtle")
            first_time = False
achilles_and_turtle()
