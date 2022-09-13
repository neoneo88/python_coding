#testing 1- reverse my name in string
myname = ["first","second","third"]
myname[0]="third"
myname[2]="first"
for element in myname:
    print(element)


#testing2-find the highest number in the array
list = [2,3,4,100,5]
list.sort()
print(list)
print(list[-1])

#testing3 = return name with character a
names = ['sing yee', 'zigang', 'landon']
a = "a"

for name in names:
    if a in name:
        print(name)

#testing4 - return name with age below or equal to 28

def dick():
    d = {}
    d['Neo']= 25
    d['Tom']= 29
    d['Hey']= 40
    
    for key, value in d.items():
        if value > 28:
            print (key,value)

dick()

