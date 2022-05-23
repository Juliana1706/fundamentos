def exemplo(): 
    print('olá mundo!')

exemplo()

def estudo():
    print('matemática')

estudo()

def soma(n1, n2):
    print(n1 + n2)
soma(9, 4)

#a = int(input('Digite um número: '))
#b = int(input('Digite um outro número: '))
#soma(a, b)

#a = input('Digite um número: ')
#b = input('Digite um outro número: ')
#soma(int(a), int(b))

def python(usuario):
    print('Olá, ' + usuario)
python('Juliana')

def frutas(citricas):
    print(citricas)
frutas('limão, laranja')

def frutas(*citricas):
    print(citricas)
frutas('limão', 'laranja', 'abacaxi')

def frutas(*citricas):
    print(citricas)

f_cit = ['limão', 'laranja', 'abacaxi']
frutas(*f_cit)