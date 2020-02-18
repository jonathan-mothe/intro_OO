class Cliente:

    def __init__(self, nome):
        self.nome = nome

    @property   # indica que este método representa uma propriedade 
    def nome(self): 
        print("chamando @property nome()")
        return self.__nome.title()

    @nome.setter    # cria um setter sem adição do set antes do nome do método
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome