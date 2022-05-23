# def livro():
#     titulo = input('Título: ')
#     autor = input('Autor: ')

# menu = input('1. cadastrar, 2. consultar, 3. atualizar ')

# if menu == '1':
#     livro()
# elif menu == '2':
#     livro()
# elif menu == '3':
#     livro()
# else:
#     print('digite uma opção válida')

def livro(titulo, autor):
    titulo_livro = titulo
    autor_livro = autor
menu = input('1. cadastrar, 2. consultar, 3. atualizar ')


if menu == '1':
    livro(input('Título: '), input('Autor: '))
elif menu == '2':
    livro('céu', 'Rui')
elif menu == '3':
    titulo_do_livro = input('Título: ')
    autor_do_livro = input('Autor: ')
    livro(titulo_do_livro, autor_do_livro)
else:
    print('digite uma opção válida')
    
# if menu == '1':
#     titulo = input('Título: ')
#     autor = input('Autor: ') 

# elif menu == '2':
#     titulo = input('Título: ')
#     autor = input('Autor: ') 

# elif menu == '3':
#     titulo = input('Título: ')
#     autor = input('Autor: ') 