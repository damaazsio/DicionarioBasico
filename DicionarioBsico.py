clientes ={
    'clientes': {
        'nome':'Willy',
        'sobrenome': 'Damásio',
    },
     'clientes2' : {
        'nome' : 'Francisco',
        'sobrenome' :'Damásio',
        
     },
}

for clientes1, clientes2 in clientes.items():
    print(f'Exibindo {clientes1}')
    for dados1, dados2 in clientes2.items():
        print(f'\t{dados1} = {dados2}')