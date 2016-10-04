# AUTHOR Shruti Kannan kshruti@bu.edu
# AUTHOR Sanya Kalra skalra@bu.edu
# AUTHOR Rashmi Agarwal rashmi23@bu.edu
class Polynomial():
	def __init__(self, p = [0]):			# =[0] is very imprtant. check piazza for more info
		exp=[]
		val=[]	
		self.p=list(p)						# if prof inputs tuples as input in compiler, it will convert to list. some ppl were getting an error due to tuples. 
		for i in range(len(self.p)):
			exp.append(i)
			val.append(self.p[len(self.p)-i-1])		#exp= i and values are arranged in descending order
		self.p=dict(zip(exp,val))					#converting to dictionary with lsit 'exp' as keys and list 'val' as values
		
		
	def __add__(self, other):		
		p3=Polynomial()
		for i in self.p:					#if key in self and other, add values
			if i in other.p:
				p3[i]=self.p[i]+other.p[i]
			else:
				p3[i]=self.p[i]				# if key in self but not other, add self
		for i in other.p:
			if i not in self.p:				#if key in other and not self, add other
				p3[i]=other.p[i]								 
		return p3		
		
	def __sub__(self, other):
		p3=Polynomial()
		for i in self.p:
			if i in other.p:
				p3[i]=self.p[i]-other.p[i]
			else:
				p3[i]=self.p[i]
		for i in other.p:
			if i not in self.p:
				p3[i]=other.p[i]
		return p3
		
	def __mul__():
		result_p=Polynomial()
                for i in self.p:
                        for j in other.p:
                                result_p[i+j] += self.p[i]*other.p[j]
                return result_p
		
	def __eq__(self, other):
		flag=0
                if len(self.p)!=len(other.p):
                        return False
                else:
                        for i in self.p:
                                if self.p==other.p:
                                        flag=1
                if flag==1:
                        return True
                return False
	
	#Error in derivative
	def differentiate(self):
                diff = Polynomial(self.p)
                for i in self.p:
                    self.p[i+1] = self.p[i]*diff.p[i]
                del self.p[0]
		
	def deriv(self):
		dpdx = Polynomial(self.p[:]) 
		dpdx.differentiate()
		return dpdx
		
	def eval(self, x):
		ans=0
		for i in range(len(self.p)):
			ans +=self.p[i]*(x**(i))
		return ans
	
	def __setitem__(self,key,item):
		#able to set coefficient of exponent which is 0 in the given poly
		#self.p[len(self.p)-key-1]=item
		self.p[key]=item

	def __getitem__(self,key):
		if key not in self.p:
			return 0
		else:
			return self.p[key]	
		
	def __str__(self):
		#print(self.p)
		s = ''
		for i in self.p:
			if self.p[i] != 0:
				s += "+({}*x^{})".format(self.p[i],i)
			#print (i, self.p[i])'''
		#print(self.p.keys(), self.p.values())
		return s
				
	def __repr__(self):
		return self.__str__()

def main():
	#p1={}
	p1=Polynomial([1.4,2,3.4,4.2])
	#p1=Polynomial({0:12.3,1:54.2,2:64.2,3:12,4:43.77})
	#for i,j in enumerate(p11):
	#	p1[i]=j
	#p1=Polynomial(p11)
	
	#p2={}
	p2=Polynomial([5,6.4,7.2])
	#p2=Polynomial({0:12,1:34,2:56,3:24.3})
	#for i,j in enumerate(p22):
	#	p2[i]=j
	#p2=Polynomial(p22)
	#p1[100]=24
	#p2[20]=12
	
	p3=p1 +	p2
	print(p3)
	
		
if __name__ == '__main__':
    main()
