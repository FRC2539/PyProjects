#Thomas Zimmerman

cubes = []
def askPreference():
    print('Do you want to add another cube?')
    answer = input()
    if answer == 'yes':
        newCube()
    else:
        addVolumes()
def addVolumes():
    finalVolume = 0
    for i in cubes:
        finalVolume = finalVolume + i.finalans
        print('Cube #', int(cubes.index(i)) + 1, "volume is", i.finalans)
    print("The final volume is:", finalVolume)   
def newCube():
    print('Please input a valid number for width.')
    width = input()
    if not width.isnumeric():
        print("That's not right!")
    else:
        print('Please input a valid number for height.')
        height = input()
        if not height.isnumeric():
            print("That's not right!")
        else:
            print('Please input a valid number for length.')
            length = input()
            if not length.isnumeric():
                print("That's not right!")
    cube = Cube(int(width), int(height), int(length))
    cubes.append(cube)
    askPreference()
class Cube:
    def __init__(self, num1, num2, num3):
        self.width = num1
        self.height = num2
        self.length = num3
        self.finalans = int(self.height * self.length * self.width)

askPreference()

