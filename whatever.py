def list():
    list = range(0,5)
    a = 3
    for x in list:
        if x>a:
            return x+10

#dictionary
def dick():
    d = {}
    d['Neo']= 25
    d['Tom']= 29
    d['Hey']= 40
    
    for key, value in d.items():
        if value > 28:
            print (key,value)

dick()


