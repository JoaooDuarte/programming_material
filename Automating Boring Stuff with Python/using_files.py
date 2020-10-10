import shelve
shelfFile = shelve.open('mydata')
#dogs = ['Zophiez', 'Pookaz', 'Simonz']
#shelfFile['dogs'] = dogs
#shelfFile.close()

#shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))