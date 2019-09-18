#operator overloading 

#addition of two object using operator overloading

class add:
	def __init__(self, n1, n2):
  		self.n1 = n1 
    	self.n2 = n2 
   	
	def __add__(self, other):
    	a1 = self.n1 + other.n1
    	a2 = self.n2 + other.n2
    
    	sum = add(a1, a2)
		return sum
	
s1 = add(23, 24)
s2= add(22, 31)

sum = s1 + s2 
print(sum.n1)
print(sum.n2)

#addition of three objects using operator overloading

class add:
	
	def __init__(self, n1, n2):
		self.n1 = n1 
		self.n2 = n2
	
	def __add__(self, other):
		a1 = self.n1 + other.n1
		a2 = self.n2 + other.n2
		
		sum = add(a1,a2)
		return sum


s1 = add(27, 32)
s2 = add(22, 41)
s3 = add(36, 52)

sum1 = s1 + s2

n11 = sum1.n1
n22 = sum1.n2

s4 = add(n11,n22)

sum2 = s3 + s4 
print(sum2.n1)
print(sum2.n2)
