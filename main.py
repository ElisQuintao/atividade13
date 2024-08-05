#Crie um programa em que o usuário possa cadastrar uma lista de tarefas a fazer no dia. Após terminar, envie o link do repositório no GitHub.
# lista de tarefas

lista_tarefas = []

#inicio do loop
while True:
    print('1 - inserir novo nome.')
    print('2 - Listar as tarefas')
    print('3 - sair do programa.')
   
#opcao do usuario
    opcao = input('Escolha uma opção: ')
    

    #verifica a escolha
    match opcao:
        case '1':
            nova_tarefa = input('insira uma nova atividade: ').capitalize()
            lista_tarefas.append(nova_tarefa)
            print(f'{nova_tarefa} inserido com sucesso')
            continue
            
        case '2':
            print('\nListar de tarefas')
            for tarefa in lista_tarefas:
                print(tarefa)
            continue
        case '3':
            print('Programa encerrado.')
            break
        case _:
            print('Opção invalida.')
            
