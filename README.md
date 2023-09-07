
# <p align="center">Zeno's paradoxes</p>

“We have two ears and one mouth, so we should listen more than we say.”
</br>
Zeno of Citium, as quoted by Diogenes Laërtius
    
## Introduction

This project explores Zeno's famous paradoxes, philosophical conundrums that have challenged the intellect for centuries. Zeno of Elea, a pre-Socratic philosopher of the sixth century BC, formulated these paradoxes to challenge our understanding of motion and reality. Through this project, we will simulate these paradoxes using Python to better understand them.

## Simulated Paradoxes

### 1. Paradox of Achilles and the tortoise
In this paradox, Zeno imagines Achilles, a fast runner, in competition with a slower tortoise. Although Achilles gives the tortoise a head start, it seems he can never overtake it. Every time Achilles reaches the spot where the tortoise was, the latter has already moved on, creating an infinite series of steps to reach the tortoise.

#### The python script
This Python script simulates the Paradox of Achilles and the Tortoise, using objects to represent Achilles and the Tortoise, and their movement in a race.

##### Classes used
- Runner: This class represents a runner with the attributes name (runner's name), position (runner's current position) and speed (runner's speed in meters per second). The move method allows the runner to move according to the time spent.

##### Main function
- achilles_and_turtle(): This function creates two instances of the Runner class, one for Achilles and one for Turtle. It initializes their respective positions and speeds, then simulates their run using a loop. At each iteration, the positions of Achilles and the Turtle are updated according to their speed and elapsed time. The progress of the race is displayed at each stage.

This simulation illustrates the Paradox of Achilles and the Tortoise by showing how Achilles, thanks to his superior speed, always ends up overtaking the Tortoise, even if at first it seems he'll never catch up due to the infinitely divisible distances.

### 2. Paradox of the dichotomy
In this paradox, Zeno stands in front of a tree holding a stone. To reach the tree, the stone must travel an infinite series of continuously-reducing distances, each step taking a finite amount of time. According to Zeno, this means that the stone can never reach the tree.

#### This python script 
This Python script simulates the Dichotomy Paradox, also known as Zeno's Race Paradox, by modeling the throwing of a stone towards a tree located at a given distance.

##### Function used
- dichotomy_paradox(d_tree): This function takes the distance d_tree between the stone and the tree as a parameter. It simulates the throwing of the stone using a while loop. At each iteration, the distance covered by the stone (d_rock) is updated by adding half the distance of the current step, and the value of step is divided by 2. The stone's progress is displayed at each step.

This simulation illustrates the Dichotomy Paradox by showing how, although the stone takes an infinite series of steps to reach the tree, it eventually reaches the tree in a finite time.

### 3. Paradox of the flying arrow
In this paradox, Zeno imagines an arrow in flight. At every instant, the arrow occupies a precise position in space. However, since time is made up of instants in which nothing happens, the arrow seems to remain motionless at all times, suggesting that movement is impossible.

#### This python script 

This Python script simulates the Arrow in Flight Paradox, a paradox formulated by Zeno to challenge the notion of motion in discrete time.

##### Function used
- arrow_in_flight(velocity, time_interval, d_target): This function takes as parameters the arrow speed (velocity), the time interval between each measurement (time_interval) and the total distance to the target (d_target). It simulates the flight of the arrow using a for loop. At each iteration, the arrow's position is calculated by adding the distance covered during a time interval to the previous position. The arrow's progress is displayed at each step, with a pause defined by time_interval. At the end, the arrow's final position is displayed.

This simulation illustrates the Arrow in Flight Paradox by showing how, although the arrow occupies a precise position at each instant, it can travel a finite distance to reach the target.

## Target skills
- Programming in Python.
- Understanding algorithmic concepts.
- Use of the Pygame library to enhance the visual aspect of simulations.