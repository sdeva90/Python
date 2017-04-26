import math

#Variable declaration
#n1 = 1.54   #refractive index of core
#NA = 0.5    #numerical aperture
n1 = int(input(" Please Enter the First Number: "))
NA = int(input(" Please Enter the second number: "))
#Calculation
n2 = math.sqrt(n1**2-NA**2)

#Result
print ("Refractive index of cladding is",n2)
