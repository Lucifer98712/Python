print("Python has entered the party!")
print(3+2)

def sec_to_min(s):
    mi=s/60
    print(str(s) + ' sec = ' + str(mi) + ' min')

sec_to_min(6000)

#use * when no. of arguments are not known
#Normal argument passing i.e only one value per call, used when no. of arguments are known

def banks(*ban):
    for i in range (6):
        print(ban[i] + ' is the best bank.')


banks('Himalayan', 'NIC', 'Global', 'Laxmi', 'Everest', 'Nepal')




