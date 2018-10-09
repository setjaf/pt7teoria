Sigma=('a','b',' ')

Gama=('A','B','Z')

z='Z'

F='q4'

Q=('q1','q2','q3','q4')

s='q1'

Delta={
	('q1','a','Z'):('q2','BZ'),
	('q1','','A'):('q4','Z'),
	('q2','a','B'):('q2','BB'),
	('q2','b','B'):('q3',''),
	('q3','b','B'):('q3',''),
	('q3',' ','Z'):('q4','Z')
}

def push(w,stack):
    for s in w[::-1]:
	stack.append(s)
    return stack

def print_stack(stack):
	#print(''.join(stack[::-1]))
        print(''.join(stack[::]))
	return

def transicion(estado,c,stack):
	top=stack.pop();
	print('Transicion ('+estado+','+c+','+top+')')
	if c in Sigma:
		if (estado,c,top) in Delta.keys():
			estado,agregar=Delta[(estado,c,top)]
			if agregar!='':
				stack=push(agregar,stack)
			print_stack(stack);
			return estado,stack,True
		else:
			return estado,stack,False		
	else:
		return estado,stack,False

cadena='aabb '

estado=s

stack=[z]

STATUS=True

for c in cadena:
	estado,stack,STATUS=transicion(estado,c,stack)
	if not STATUS or len(stack)==0:
		break

if STATUS and estado==F:
	print('La cadena esta dentro del lenguaje')
else:
	print('La cadena no esta en dentro del lenguaje')
