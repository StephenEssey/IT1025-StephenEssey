class Shark: #Defining Shark class
    def __init__(self, name):
        self.name = name

    def swim(self): #Defining swim() method
        print(self.name + " is swimming.")

    def be_awesome(self): #Defining be_awesome() method
        print(self.name + " is being awesome.")

def main(): #Defining object names
    sammy = Shark("Sammy")
    sammy.be_awesome()
    stevie = Shark("Stevie")
    stevie.swim()
    stephen = Shark("Stephen")
    stephen.swim()

if __name__ == "__main__":
  main()
