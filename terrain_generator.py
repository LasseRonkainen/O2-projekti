import random

#Creates random terrain within given size (width, length)

def Create_terrain():

    file = input("Give filenime for terrain : ") + ".txt"
    size = input("Give terrain size in form x,y : ")
    size = size.split(',')

    if len(size) == 2:
        x = size[0].strip()
        y = size[1].strip()

        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y) 
                 
        else:
            print("Try using integer numbers next time")

        f = open(file, "w")

        for i in range(x):
            for j in range(y):
                f.write(str(random.randint(1, 3)))
                if j < y - 1:
                    f.write("   ")
            if i < x - 1:
                f.write("\n")

        f.close()

    else:
        print("You managed somehow to fail")


Create_terrain()