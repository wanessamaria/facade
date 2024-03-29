from datetime import datetime
import folium
import os

class Avaliacao:
    def __init__(self, usuario, comentario, classificacao):
        self.usuario = usuario
        self.comentario = comentario
        self.classificacao = classificacao

    def exibir_informacoes(self):
        print(f"Usuário: {self.usuario}")
        print(f"Comentário: {self.comentario}")
        print(f"Classificação: {self.classificacao}")

class CalculadoraHipoteca:
    def calcular_pagamento_mensal(self, valor_emprestimo, taxa_juros, anos):
        # Fórmula para calcular o pagamento mensal de uma hipoteca
        taxa_juros_mensal = (taxa_juros / 100) / 12
        numero_pagamentos = anos * 12
        pagamento_mensal = (valor_emprestimo * taxa_juros_mensal) / (1 - (1 + taxa_juros_mensal) ** -numero_pagamentos)
        return pagamento_mensal

class Mapa:
    def __init__(self):
        self.propriedades = []

    def adicionar_propriedade(self, propriedade):
        self.propriedades.append(propriedade)

    def exibir_mapa_interativo(self):
        # Cria um mapa centrado em uma localização inicial
        mapa = folium.Map(location=[-23.5505, -46.6333], zoom_start=10)  # Pode ajustar as coordenadas e o nível de zoom

        # Adiciona marcadores para cada propriedade
        for propriedade in self.propriedades:
            folium.Marker([propriedade.latitude, propriedade.longitude], popup=propriedade.endereco).add_to(mapa)

        # Exibe o mapa interativo (pode ser aberto em um navegador)
        mapa.save(os.path.join(os.getcwd(), 'mapa_interativo.html'))
        print("Mapa interativo gerado. Abra o arquivo 'mapa_interativo.html' em um navegador para visualizá-lo.")

class AnaliseMercado:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao

    def exibir_informacoes(self):
        print(f"Título da Análise: {self.titulo}")
        print(f"Descrição da Análise: {self.descricao}")

class Consulta:
    def __init__(self, propriedade, agente, cliente, data_hora):
        self.propriedade = propriedade
        self.agente = agente
        self.cliente = cliente
        self.data_hora = data_hora

    def exibir_informacoes(self):
        print(f"Consulta para o cliente {self.cliente}:")
        print(f"Agendada por: {self.agente.nome}")
        print(f"Data e Hora: {self.data_hora}")

class ConsultaCliente:
    def __init__(self, cliente, agente, data_hora):
        self.cliente = cliente
        self.agente = agente
        self.data_hora = data_hora

    def exibir_informacoes(self):
        print(f"Consulta para o cliente {self.cliente}:")
        print(f"Agendada por: {self.agente.nome}")
        print(f"Data e Hora: {self.data_hora}")

class TourVirtual:
    def __init__(self, descricao, url):
        self.descricao = descricao
        self.url = url

    def exibir_informacoes(self):
        print(f"Descrição: {self.descricao}, URL: {self.url}")

class Propriedade:
    def __init__(self, codigo, endereco, preco, latitude, longitude):
        self.codigo = codigo
        self.endereco = endereco
        self.preco = preco
        self.latitude = latitude
        self.longitude = longitude
        self.tours_virtuais = []
        self.avaliacoes = []

    def exibir_informacoes(self):
        print(f"Código: {self.codigo}, Endereço: {self.endereco}, Preço: {self.preco}")
        print(f"Localização: Latitude {self.latitude}, Longitude {self.longitude}")
        print("Tours Virtuais:")
        for tour_virtual in self.tours_virtuais:
            tour_virtual.exibir_informacoes()
        print("Avaliações:")
        for avaliacao in self.avaliacoes:
            avaliacao.exibir_informacoes()

    def adicionar_tour_virtual(self, tour_virtual):
        self.tours_virtuais.append(tour_virtual)

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

class PerfilAgente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.avaliacoes = []

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

    def exibir_informacoes(self):
        print(f"Nome do Agente: {self.nome}, E-mail do Agente: {self.email}")
        print("Avaliações:")
        for avaliacao in self.avaliacoes:
            avaliacao.exibir_informacoes()

class PropriedadeFacade:
    def __init__(self):
        self.gerenciador = GerenciadorPropriedades()

    def adicionar_propriedade(self, codigo, endereco, preco, latitude, longitude):
        propriedade = Propriedade(codigo, endereco, preco, latitude, longitude)
        self.gerenciador.adicionar_propriedade(propriedade)
        print("Propriedade adicionada com sucesso!")

    def listar_propriedades(self):
        self.gerenciador.listar_propriedades()

    def editar_propriedade(self, codigo, novo_endereco, novo_preco):
        self.gerenciador.editar_propriedade(codigo, novo_endereco, novo_preco)

    def excluir_propriedade(self, codigo):
        self.gerenciador.excluir_propriedade(codigo)

    def exibir_mapa_interativo(self):
        self.gerenciador.exibir_mapa_interativo()

    def agendar_consulta(self, codigo_propriedade, agente, cliente, data_hora):
        self.gerenciador.agendar_consulta(codigo_propriedade, agente, cliente, data_hora)

    def listar_consultas(self):
        self.gerenciador.listar_consultas()

    def adicionar_tour_virtual(self, codigo_propriedade, descricao, url):
        self.gerenciador.adicionar_tour_virtual(codigo_propriedade, descricao, url)

    def listar_tours_virtuais(self, codigo_propriedade):
        self.gerenciador.listar_tours_virtuais(codigo_propriedade)

    def agendar_consulta_cliente(self, cliente, agente, data_hora):
        self.gerenciador.agendar_consulta_cliente(cliente, agente, data_hora)

    def adicionar_analise_mercado(self, titulo, descricao):
        self.gerenciador.adicionar_analise_mercado(titulo, descricao)

    def listar_analises_mercado(self):
        self.gerenciador.listar_analises_mercado()

    def calcular_pagamento_hipoteca(self, codigo_propriedade, valor_emprestimo, taxa_juros, anos):
        self.gerenciador.calcular_pagamento_hipoteca(codigo_propriedade, valor_emprestimo, taxa_juros, anos)

    def avaliar_propriedade(self, codigo_propriedade):
        self.gerenciador.avaliar_propriedade(codigo_propriedade)

    def avaliar_agente(self, nome_agente):
        self.gerenciador.avaliar_agente(nome_agente)

class GerenciadorPropriedades:
    def __init__(self):
        self.propriedades = []
        self.perfis_agentes = []
        self.consultas = []
        self.consultas_clientes = []
        self.analises_mercado = []
        self.mapa = Mapa()

    def adicionar_propriedade(self, propriedade):
        self.propriedades.append(propriedade)
        self.mapa.adicionar_propriedade(propriedade)
        
    def adicionar_perfil_agente(self, perfil):
        self.perfis_agentes.append(perfil)

    def listar_perfis_agentes(self):
        print("Lista de Perfis de Agentes:")
        for perfil in self.perfis_agentes:
            perfil.exibir_informacoes()

    def exibir_mapa_interativo(self):
        self.mapa.exibir_mapa_interativo()

    def listar_propriedades(self):
        print("Lista de Propriedades:")
        for propriedade in self.propriedades:
            propriedade.exibir_informacoes()

    def editar_propriedade(self, codigo, novo_endereco, novo_preco):
        for propriedade in self.propriedades:
            if propriedade.codigo == codigo:
                propriedade.endereco = novo_endereco
                propriedade.preco = novo_preco
                print(f"A propriedade {codigo} foi editada com sucesso.")
                return
        print(f"Propriedade com o código {codigo} não encontrada.")

    def excluir_propriedade(self, codigo):
        for propriedade in self.propriedades:
            if propriedade.codigo == codigo:
                self.propriedades.remove(propriedade)
                print(f"A propriedade {codigo} foi excluída com sucesso.")
                return
        print(f"Propriedade com o código {codigo} não encontrada.")

    def agendar_consulta(self, codigo_propriedade, agente, cliente, data_hora):
        propriedade = self.obter_propriedade_por_codigo(codigo_propriedade)
        if propriedade:
            consulta = Consulta(propriedade, agente, cliente, data_hora)
            self.consultas.append(consulta)
            print("Consulta agendada com sucesso!")
        else:
            print(f"Propriedade com código {codigo_propriedade} não encontrada.")

    def listar_consultas(self):
        print("Lista de Consultas:")
        for consulta in self.consultas:
            consulta.exibir_informacoes()

    def obter_propriedade_por_codigo(self, codigo):
        for propriedade in self.propriedades:
            if propriedade.codigo == codigo:
                return propriedade
        return None

    def adicionar_tour_virtual(self, codigo_propriedade, descricao, url):
        propriedade = self.obter_propriedade_por_codigo(codigo_propriedade)
        if propriedade:
            tour_virtual = TourVirtual(descricao, url)
            propriedade.adicionar_tour_virtual(tour_virtual)
            print(f"Tour Virtual adicionado à propriedade {codigo_propriedade} com sucesso!")
        else:
            print(f"Propriedade com código {codigo_propriedade} não encontrada.")

    def listar_tours_virtuais(self, codigo_propriedade):
        propriedade = self.obter_propriedade_por_codigo(codigo_propriedade)
        if propriedade:
            print(f"Tours Virtuais para a propriedade {codigo_propriedade}:")
            for tour_virtual in propriedade.tours_virtuais:
                tour_virtual.exibir_informacoes()
        else:
            print(f"Propriedade com código {codigo_propriedade} não encontrada.")

    def agendar_consulta_cliente(self, cliente, agente, data_hora):
        consulta_cliente = ConsultaCliente(cliente, agente, data_hora)
        self.consultas_clientes.append(consulta_cliente)
        print("Consulta de cliente agendada com sucesso!")

    def obter_perfil_agente_por_nome(self, nome):
        for perfil in self.perfis_agentes:
            if perfil.nome == nome:
                return perfil
        return None

    def adicionar_analise_mercado(self, titulo, descricao):
        analise_mercado = AnaliseMercado(titulo, descricao)
        self.analises_mercado.append(analise_mercado)
        print("Análise de mercado adicionada com sucesso!")

    def listar_analises_mercado(self):
        print("Lista de Análises de Mercado:")
        for analise_mercado in self.analises_mercado:
            analise_mercado.exibir_informacoes()

    def calcular_pagamento_hipoteca(self, codigo_propriedade, valor_emprestimo, taxa_juros, anos):
        propriedade = self.obter_propriedade_por_codigo(codigo_propriedade)
        if propriedade:
            calculadora_hipoteca = CalculadoraHipoteca()
            pagamento_mensal = calculadora_hipoteca.calcular_pagamento_mensal(valor_emprestimo, taxa_juros, anos)
            print(f"O pagamento mensal estimado para a propriedade {codigo_propriedade} é de R${pagamento_mensal:.2f}.")
        else:
            print(f"Propriedade com código {codigo_propriedade} não encontrada.")

    def avaliar_propriedade(self, codigo_propriedade):
        propriedade = self.obter_propriedade_por_codigo(codigo_propriedade)

        if propriedade:
            usuario = input("Digite seu nome de usuário: ")
            comentario = input("Digite seu comentário: ")
            classificacao = int(input("Digite a classificação (de 1 a 5): "))

            avaliacao = Avaliacao(usuario, comentario, classificacao)
            propriedade.adicionar_avaliacao(avaliacao)
            print("Avaliação adicionada com sucesso!")
        else:
            print(f"Propriedade com código {codigo_propriedade} não encontrada.")

    def avaliar_agente(self, nome_agente):
        agente = self.obter_perfil_agente_por_nome(nome_agente)

        if agente:
            usuario = input("Digite seu nome de usuário: ")
            comentario = input("Digite seu comentário: ")
            classificacao = int(input("Digite a classificação (de 1 a 5): "))

            avaliacao = Avaliacao(usuario, comentario, classificacao)
            agente.adicionar_avaliacao(avaliacao)
            print("Avaliação do agente adicionada com sucesso!")
        else:
            print(f"Agente com nome {nome_agente} não encontrado.")

def menu():
    print("\nEscolha uma opção:")
    print("1. Adicionar Propriedade")
    print("2. Listar Propriedades")
    print("3. Editar Propriedade")
    print("4. Excluir Propriedade")
    print("5. Agendar Consulta")
    print("6. Listar Consultas")
    print("7. Adicionar Tour Virtual")
    print("8. Listar Tours Virtuais")
    print("9. Agendar Consulta Cliente")
    print("10. Adicionar Análise de Mercado")
    print("11. Listar Análises de Mercado")
    print("12. Calcular Pagamento de Hipoteca")
    print("13. Avaliar Propriedade")
    print("14. Avaliar Agente")
    print("15. Exibir Mapa Interativo")
    print("0. Sair")

# Inicialização da Facade
propriedade_facade = PropriedadeFacade()

# Loop principal do programa
while True:
    menu()
    opcao = input("\nDigite o número da opção desejada: ")

    if opcao == "1":
        codigo = input("Digite o código da propriedade: ")
        endereco = input("Digite o endereço da propriedade: ")
        preco = float(input("Digite o preço da propriedade: "))
        latitude = float(input("Digite a latitude da propriedade: "))
        longitude = float(input("Digite a longitude da propriedade: "))
        propriedade_facade.adicionar_propriedade(codigo, endereco, preco, latitude, longitude)
    elif opcao == "2":
        propriedade_facade.listar_propriedades()
    elif opcao == "3":
        codigo = input("Digite o código da propriedade que deseja editar: ")
        novo_endereco = input("Digite o novo endereço: ")
        novo_preco = float(input("Digite o novo preço: "))
        propriedade_facade.editar_propriedade(codigo, novo_endereco, novo_preco)
    elif opcao == "4":
        codigo = input("Digite o código da propriedade que deseja excluir: ")
        propriedade_facade.excluir_propriedade(codigo)
    elif opcao == "5":
        codigo_propriedade = input("Digite o código da propriedade: ")
        agente_nome = input("Digite o nome do agente: ")
        cliente = input("Digite o nome do cliente: ")
        data_hora = datetime.strptime(input("Digite a data e hora (formato: YYYY-MM-DD HH:MM): "), '%Y-%m-%d %H:%M')
        propriedade_facade.agendar_consulta(codigo_propriedade, agente_nome, cliente, data_hora)
    elif opcao == "6":
        propriedade_facade.listar_consultas()
    elif opcao == "7":
        codigo_propriedade = input("Digite o código da propriedade: ")
        descricao = input("Digite a descrição do tour virtual: ")
        url = input("Digite a URL do tour virtual: ")
        propriedade_facade.adicionar_tour_virtual(codigo_propriedade, descricao, url)
    elif opcao == "8":
        codigo_propriedade = input("Digite o código da propriedade: ")
        propriedade_facade.listar_tours_virtuais(codigo_propriedade)
    elif opcao == "9":
        cliente = input("Digite o nome do cliente: ")
        agente_nome = input("Digite o nome do agente: ")
        data_hora = datetime.strptime(input("Digite a data e hora (formato: YYYY-MM-DD HH:MM): "), '%Y-%m-%d %H:%M')
        propriedade_facade.agendar_consulta_cliente(cliente, agente_nome, data_hora)
    elif opcao == "10":
        titulo = input("Digite o título da análise de mercado: ")
        descricao = input("Digite a descrição da análise de mercado: ")
        propriedade_facade.adicionar_analise_mercado(titulo, descricao)
    elif opcao == "11":
        propriedade_facade.listar_analises_mercado()
    elif opcao == "12":
        codigo_propriedade = input("Digite o código da propriedade: ")
        valor_emprestimo = float(input("Digite o valor do empréstimo: "))
        taxa_juros = float(input("Digite a taxa de juros (%): "))
        anos = int(input("Digite o número de anos: "))
        propriedade_facade.calcular_pagamento_hipoteca(codigo_propriedade, valor_emprestimo, taxa_juros, anos)
    elif opcao == "13":
        codigo_propriedade = input("Digite o código da propriedade que deseja avaliar: ")
        propriedade_facade.avaliar_propriedade(codigo_propriedade)
    elif opcao == "14":
        nome_agente = input("Digite o nome do agente que deseja avaliar: ")
        propriedade_facade.avaliar_agente(nome_agente)
    elif opcao == "15":
        propriedade_facade.exibir_mapa_interativo()
    elif opcao == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, digite novamente.")
