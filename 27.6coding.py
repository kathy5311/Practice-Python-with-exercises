with open('rt.p','w') as file:
    file.write(input("Write it!"))

with open('rt.p','r') as file:
    for i in file:
        words = i.split()
        for word in words:
            if 'c' in word:
                print(word.strip(",.")) 


