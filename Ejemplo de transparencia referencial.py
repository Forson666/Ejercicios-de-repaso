def potencia(a,b):
	y = 1
	for x in range (1, b+1):
		y = y * a
	return y

def potenciaconTR(a,b):
	if b == 1:
		return a
	else:
		return a * potenciaconTR(a,b-1)