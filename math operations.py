import math 
  
a = 2.3
  

print ("The ceil of 2.3 is : ", end="") 
print (math.ceil(a)) 
  

print ("The floor of 2.3 is : ", end="") 
print (math.floor(a)) 
a = -10
  
b= 5
  
 
print ("The absolute value of -10 is : ", end="") 
print (math.fabs(a)) 
  

print ("The factorial of 5 is : ", end="") 
print (math.factorial(b)) 

a = -10
b = 5.5
c = 15
d = 5
 
print ("The copysigned value of -10 and 5.5 is : ", end="") 
print (math.copysign(5.5, -10)) 
  

print ("The gcd of 5 and 15 is : ", end="") 
print (math.gcd(5,15)) 

print ("The e**4 value is : ", end="") 
print (math.exp(4)) 
   
 
print ("The value of log 2 with base 3 is : ", end="") 
print (math.log(2,3)) 


print ("The value of log2 of 16 is : ", end="") 
print (math.log2(16)) 
   
 
print ("The value of log10 of 10000 is : ", end="") 
print (math.log10(10000)) 


print ("The value of 3 to the power 2 is : ", end="") 
print (math.pow(3,2)) 
   
 
print ("The value of square root of 25 : ", end="") 
print (math.sqrt(25)) 

print ("The value of sine of pi/6 is : ", end="") 
print (math.sin(a)) 
   
print ("The value of cosine of pi/6 is : ", end="") 
print (math.cos(a)) 

a = math.pi/6
b = 3
c = 4
   

print ("The value of tangent of pi/6 is : ", end="") 
print (math.tan(a)) 
   

print ("The value of hypotenuse of 3 and 4 is : ", end="") 
print (math.hypot(b,c)) 

a = math.pi/6
b = 30
  
 
print ("The converted value from radians to degrees is : ", end="") 
print (math.degrees(a)) 
   

print ("The converted value from degrees to radians is : ", end="") 
print (math.radians(b)) 

a = 4
  

print ("The gamma() of 4 is : ", end="") 
print (math.gamma(a)) 


print ("The value of const. pi is : ", end="") 
print (math.pi) 
  

print ("The value of const. e is : ", end="") 
print (math.e) 


if (math.isnan(math.nan)): 
       print ("The number is nan") 
else : print ("The number is not nan") 
  
 
if (math.isinf(math.inf)): 
       print ("The number is positive infinity") 
else : print ("The number is not positive infinity")
