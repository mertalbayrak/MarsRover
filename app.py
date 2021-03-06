class FileOperations():
    def readFile(self,file):
        with open(file, "r+") as f:
            return f.readlines()

class Plateau():
    def __init__(self, positionX, positionY):
        self.positionX = positionX
        self.positionY = positionY

class Rover():
    def __init__(self, plateau, inputs):
        self.plateau = plateau
        self.positionX = inputs[0]
        self.positionY = inputs[1]
        self.direction = inputs[2]
        self.isFinished = False

    def printPositionAndDirection(self):
        print("{} {} {}".format(self.positionX, self.positionY, self.direction))

    def changeDirection(self, inputs):
        for input in inputs:      
            if self.direction == 'N':
                if input == 'L':
                    self.direction = 'W'
                elif input == 'R':
                    self.direction = 'E'
                elif input == 'M':
                    self.positionY = self.positionY + 1 if not (self.positionY + 1 > self.plateau.positionY) else self.plateau.positionY
            elif self.direction == 'W':
                if input == 'L':
                    self.direction = 'S'
                elif input == 'R':
                    self.direction = 'N'
                elif input == 'M':
                    self.positionX = self.positionX - 1 if self.positionX - 1 > 0 else 0
            elif self.direction == 'E':
                if input == 'L':
                    self.direction = 'N'
                elif input == 'R':
                    self.direction = 'S'
                elif input == 'M':
                    self.positionX = self.positionX + 1 if not (self.positionX + 1 > self.plateau.positionX) else self.plateau.positionX
            elif self.direction == 'S':
                if input == 'L':
                    self.direction = 'E'
                elif input == 'R':
                    self.direction = 'W'
                elif input == 'M':
                    self.positionY = self.positionY - 1 if self.positionY - 1 > 0 else 0
        self.printPositionAndDirection()

if __name__ == "__main__":
    file = FileOperations()
    #test icin input dosyas?? okunuyor
    inputs = file.readFile("inputs.txt")
    #okunan input dosyas??ndaki her bir sat??r ayr?? bir list olacak ??ekilde d??zenleniyor(digit olanlar int'e d??n????t??r??l??yor)
    inputs = [[int(i) if i.isdigit() == True else i for i in input.strip().split()] for input in inputs]
    #okunan ilk sat??rdaki de??erler plateau rectangular i??in set ediliyor.
    plateau = Plateau(inputs[0][0], inputs[0][1])
    #i??lem sonras?? ilk input listeden ????kart??l??yor.
    inputs.pop(0)
    #plateau harici kalan inputlar i??in 2'??erli ??ekilde for d??ng??s?? ile rover hareketi ger??ekle??tiriliyor.
    for i in range(0,len(inputs),2):
        rover = Rover(plateau, inputs[i])
        rover.changeDirection(''.join(inputs[i+1]))