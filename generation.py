import random



def generate():

    #taking all possible letters, numbers and symbols
    #This will be added env variable
    upper_cases = """ABCDEFGHIJKLMNOQRSTUVWXYZ"""
    lower_cases = """abcdefghijklmnopqrstuyvwxyz"""
    numbers = """0123456789"""
    symbols = """"é!'+%&/()=?_*-#${[]}\|@€,;><.:"""


    #picking characters in list
    a = random.sample(upper_cases, 4)
    a += random.sample(lower_cases, 3)
    a += random.sample(numbers, 3)
    a += random.sample(symbols, 3)
    
    #shuffle
    random.shuffle(a)

    password = ""

    for i in a:
        password+= i

    return password



    
