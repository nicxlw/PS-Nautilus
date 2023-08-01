import pandas as pd

#classe de atributos do modelo
class Auv:
    def __init__(self, thrusters: int, sensores: list, ano: int, nome: str, equipe: int):
        self.__thrusters = thrusters
        self.__sensores = sensores
        self.__ano = ano
        self.__nome = nome
        self.__equipe = equipe

    #getters
    def get_thrusters(self):
        return self.__thrusters
    def get_sensores(self):
        return self.__sensores
    def get_ano(self):
        return self.__ano
    def get_nome(self):
        return self.__nome
    def get_equipe(self):
        return self.__equipe
        

#classe de métodos do modelo
class Nautilus:

    def __init__(self):
        pass
    
    #coleta dos valores de atributos de um objeto da clase Auv
    def valores(self, robo):
        nome = robo.get_nome()
        ano = robo.get_ano()
        sensores = robo.get_sensores()
        thrusters = robo.get_thrusters()
        equipe = robo.get_equipe()
        return nome, ano, sensores, thrusters, equipe

    #utiliza a biblioteca 'pandas' e o método 'valores' para montar uma tabela com os AUVs
    def tabela(self):
        colunas = ['Nome', 'Ano', 'Sensores', "Thrusters", 'Tam. equipe']
        linhas = [' ', ' ']
        print('\n---------------Tabela de AUVs---------------\n')
        nome, ano, sensores, thrusters, equipe = metodos.valores(brhue) #pega as informaçoes do brhue
        brhue_info = [nome, ano, sensores, thrusters, equipe]
        nome, ano, sensores, thrusters, equipe = metodos.valores(lua) #pega as informaçoes da lua
        lua_info = [nome, ano, sensores, thrusters, equipe]
        total_info = [brhue_info, lua_info] #monta uma matriz com as informações
        tabela = pd.DataFrame(data=total_info, index=linhas, columns=colunas) #transforma a matriz em tabela
        print(tabela)

    #exibe as informações de um AUV escolhido pelo usuário
    def exibir(self):
        opcao = int(input(('\nExibir qual auv? (digite o número)\n1 - BrHUE\n2 - Lua\n'))) #usuario insere um numero

        #o numero corresponde a um AUV 
        if(opcao == 1):
            robo = brhue
        elif(opcao == 2):
            robo = lua
        else:
            print('Opção inválida.') 
            return
        nome, ano, sensores, thrusters, equipe = metodos.valores(robo) #pega as informaçoes do AUV escolhido

        #exibe as informações
        print(f'Nome do AUV: {nome}')
        print(f'Ano de construção: {ano}')
        print(f'Lista de sensores: {sensores}')
        print(f'Número de thrusters: {thrusters}')
        print(f'Tamanho da equipe: {equipe}')

    #rankeia os AUV do mais novo para o mais velho
    def ranking(self):
        print('\nAUVs ordenados de mais novo para mais velho:')
        if (lua.get_ano() > brhue.get_ano()):
            print(f'1- {lua.get_nome()}\n2- {brhue.get_nome()}')
        else:
            print(f'1- {brhue.get_nome()}\n2- {lua.get_nome()}')

#cria 'brhue' e 'lua' como objetos da classe 'Auv' e chama os métodos da classe 'Nautilus'
brhue = Auv(thrusters=6, sensores=['Pressão', 'Profundidade'], ano=2020, nome= 'BrHUE', equipe='35')
lua = Auv(thrusters=8, sensores=['Pressão interna', 'Pressão externa'], ano=2022, nome= 'Lua', equipe='42')
metodos = Nautilus() #'metodos' é um objeto da classe 'Nautilus' utilizado para chamar os métodos
metodos.tabela()
metodos.exibir()
metodos.ranking()




