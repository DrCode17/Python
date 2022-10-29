#!/usr/bin/python
# coding: utf8

def kiir(tomb, meret):
	for i in range(0, meret+1):
		print tomb[i]

a = [2, 3, 7, 8]
b = [3, 6, 9, 12, 18]
c = [0] * 9

n = len(a)
m = len(b)

i = 0
j = 0
k = -1
		

while i<n and j<m :
	k+=1
	if a[i]<b[j] :
		c[k] = a[i]
		i+=1
	elif a[i] == b[j] :
		c[k] = a[i]
		i+=1
		j+=1			
	elif a[i] > b[j] :
		c[k] = b[j]
		j+=1
			
		
while i<n :
	k+=1
	c[k] = a[i]
	i+=1
		
while j<m :
	k+=1
	c[k] = b[j]
	j+=1

kiir(c, k)		