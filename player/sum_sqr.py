def sumdsqr(n):
	sum=0
	while(n!=0):
		r=n%10
		sum+=r*r
		n//=10
	return sum
def happy(n):
	while(n>0):
		n=sumdsqr(n)
		if n==1:
			print('happy number')
			return
	print('not happy number')
def main():
	try:
		n=int(input())
		happy(n)
	except:
		print('invalid')
main()
