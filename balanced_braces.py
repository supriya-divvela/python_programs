n=int(input())
ol=[['{','}']]
cl=[['{','}']]
while len(ol):
	p=ol.pop(0)
	if len(p)>n*2:
	    break
	for i in range(len(p)):
		s=list(p)
		s.insert(i+1,'{')
		s.insert(i+2,'}')
		if s not in cl:
		    cl.append(s)
		    ol.append(s)
[print(''.join(i)) for i in list(filter(lambda x:len(x)==2*n,cl))]


'''
input:3
output:
{{}{}}
{{{}}}
{{}}{}
{}{}{}
{}{{}}
'''
