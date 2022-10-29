t = [ 3, 8, 2, 4, 5, 1, 6]

n = len(t)
ker = 5

i = 0
while i < n and t[i] != ker:
    i = i + 1

if(i < n):
    print('Van ' + str(ker) + ' elem')
    print("Helye: ", i+1)
else:
    print('Nincs ' + str(ker) + ' elem!')