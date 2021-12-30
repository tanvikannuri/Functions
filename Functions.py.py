thing1 = 1
thing2 = 2
def swapFileData (str): 
    with open(thing1, 'r') as a:
        data_a = a.read ()

    with open(thing2, 'r') as a:
        data_b = a.read ()

    with open(thing1, "w") as a:
        a.write(data_b)

    with open(thing2, "w") as a:
        a.write(data_a)