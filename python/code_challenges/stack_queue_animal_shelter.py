from data_structures.queue import Queue


class AnimalShelter:

    def __init__(self):
        # starts two empty queues
        self.queue_cats = Queue()
        self.queue_dogs = Queue()

    def enqueue(self, value):
        
        # checks if the node is cat or dog
        if value.type == "cat":

            self.queue_cats.enqueue(value)

        if value.type == "dog":

            self.queue_dogs.enqueue(value)

    def dequeue(self, pref):

        # checks if the pref the user submitted is cat or dog  
        if pref == "cat":

            cat_dequeue = self.queue_cats.dequeue()

            return cat_dequeue
        
        if pref == "dog":

            dog_dequeue = self.queue_dogs.dequeue()

            return dog_dequeue
        



class Dog:
    def __init__(self):
        self.type = "dog"


class Cat:

    def __init__(self):
        self.type = "cat"

    
    
