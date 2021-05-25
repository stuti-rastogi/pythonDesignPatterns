class MakeMeal:
   def prepare(self): pass
   def cook(self): pass
   def consume(self): pass

   def go(self):
      self.prepare()
      self.cook()
      self.consume()


class MakePizza(MakeMeal):
    def prepare(self):
        print ("Prepare Pizza")

    def cook(self):
        print ("Cook Pizza")

    def consume(self):
        print ("Eat Pizza")


class MakeTea(MakeMeal):
    def prepare(self):
        print ("Prepare Tea")

    def cook(self):
        print ("Cook Tea")

    def consume(self):
        print ("Drink Tea")


if __name__ == "__main__":
    makePizza = MakePizza()
    makePizza.go()

    print (25 * '-')

    makeTea = MakeTea()
    makeTea.go()
