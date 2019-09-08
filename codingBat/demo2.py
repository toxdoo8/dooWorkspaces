

def parrot_trouble(talking, hour):
    if talking == True and hour in range(0, 23):
        print(True)
    else:
        print(False)

parrot_trouble(True, 3)
parrot_trouble(True, 23)
parrot_trouble(True, 33)