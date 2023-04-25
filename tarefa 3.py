class Pais:
    def __init__(self,codigo,nome,dimensao):
        self.__codigo = codigo
        self.__nome = nome
        self.__dimensao = dimensao
        self.__populacao = 0
        self.__vizinhos = []

    def setCodigo(self,codigo):
        self.__codigo = codigo

    def getCodigo(self):
        return self.__codigo    
    
    def compararIgual(self,pais):
        #retorna true/false
        if self.__codigo == pais.getCodigo():
            return True
        else:
            return False

    def verificarVizinho(self,pais):
        for i in self.__vizinhos:
            if i.compararIgual(pais) == True:
                return True
        return False

    def calcularDensidade(self):
        return self.__populacao/self.__dimensao

    #OBS.: este método está errado (em revisão) -- CORRIGIDO!!!!
    def vizinhosComuns(self,pais):
        vizinhosPais = pais.getVizinhos() #pega a listagem de vizinhos do outro pais
        vizinhosAmbos = [] #inicia a lista dos vizinhos comuns a ambos
        for i in vizinhosPais:  
            if self.verificarVizinho(i) == True: #verifica se o vizinho do outro país é vizinho do país
                vizinhosAmbos.append(i) #adiciona na lista de ambos se verdadeiro! :)
        return vizinhosAmbos #retorna a lista, como o exercício pede!


    def adicionarVizinho(self,pais):
        self.__vizinhos.append(pais)

    def getVizinhos(self):
        return self.__vizinhos
    
    def listarVizinhos(self):
        for i in self.__vizinhos:
            print(i.getCodigo())
    
    def setPais(self,codigo,nome,dimensao,populacao,vizinhos):
        self.__codigo = codigo
        self.__nome = nome
        self.__dimensao = dimensao
        self.__populacao = populacao
        self.__vizinhos.append(vizinhos)

    def getDimensao(self):
        return self.__dimensao

    def getPopulacao(self):
        return self.__populacao
    
    def setPopulacao(self,populacao):
        self.__populacao=populacao

    def getNome(self):
        return self.__nome

class Continente():
    def __init__(self,nome):
        self.__nome=nome
        self.__paises=[]
    
    def inserePais(self,pais):
        self.__paises.append(pais)
    
    def dimensaoTotal(self):
        soma=0
        for i in self.__paises:
            soma+=(i.getDimensao())
        return soma

    def populacaoTotal(self):
        soma=0
        for i in self.__paises:
            soma+=(i.getPopulacao())
        return soma
    
    def densidadeTotal(self):
        popT=self.populacaoTotal()
        dimeT=self.dimensaoTotal()
        return popT/dimeT
    
    def maisPopuloso(self):
        maior=0
        for i in self.__paises:
            populacao=i.getPopulacao()
            if populacao>maior:
                maior = populacao
                pais=i
        return pais
    
    def menosPopuloso(self):
        menor=8000000000
        for i in self.__paises:
            populacao=i.getPopulacao()
            if populacao<menor:
                menor = populacao
                pais=i
        return pais
    
    def maiorDimensao(self):
        maior=0
        for i in self.__paises:
            dimensao=i.getDimensao()
            if dimensao>maior:
                maior = dimensao
                pais=i
        return pais
    
    def menorDimensao(self):
        menor=self.maiorDimensao().getDimensao()
        for i in self.__paises:
            dimensao=i.getDimensao()
            if dimensao<menor:
                menor = dimensao
                pais=i
        return pais

    def razaoTerritorial(self):
        maior=self.maiorDimensao()
        menor=self.menorDimensao()
        return maior.getDimensao()/menor.getDimensao()
    
    def getNome(self):
        return self.__nome


#####################

pais01 = Pais('BRA','Brasil',100)

pais02 = Pais('ARG','Argentina',101)

pais03 = Pais('URU','Uruguai',120)
pais04 = Pais('PAR','Paraguai',104)
pais05 = Pais('CHI','Chile',101)
pais06 = Pais('PER','Peru',200)

## adicionando população
pais01.setPopulacao(200)
pais02.setPopulacao(150)
pais03.setPopulacao(220)
pais04.setPopulacao(120)
pais05.setPopulacao(198)
pais06.setPopulacao(189)

#adicionando vizinhos ao BRA
pais01.adicionarVizinho(pais02)
pais01.adicionarVizinho(pais03)
pais01.adicionarVizinho(pais04)
pais01.adicionarVizinho(pais06)

#adicionando vizinhos a ARG

pais02.adicionarVizinho(pais01)
pais02.adicionarVizinho(pais03)
pais02.adicionarVizinho(pais04)
pais02.adicionarVizinho(pais05)

print(pais01.getNome(),'é vizinho do',pais02.getNome())
print(pais01.verificarVizinho(pais02))

print('densidade do ',pais01.getNome())
print(pais01.calcularDensidade())

print('densidade do ',pais02.getNome())
print(pais02.calcularDensidade())

print('compara pais01 e pais02')
print(pais01.compararIgual(pais02))

print('vizinhos do',pais01.getNome())
pais01.listarVizinhos()

print('vizinhos do',pais02.getNome())
pais02.listarVizinhos()
print('vizinhos comuns entre',pais01.getNome(),'e',pais02.getNome())
vizinhosComuns = pais01.vizinhosComuns(pais02)
for i in vizinhosComuns:
    print(i.getCodigo())


cont1=Continente('America')
cont1.inserePais(pais01)
cont1.inserePais(pais02)
cont1.inserePais(pais03)
cont1.inserePais(pais04)
cont1.inserePais(pais05)
cont1.inserePais(pais06)

print(cont1.getNome())
print('Densidade total:',cont1.densidadeTotal())
print('Dimensao total:',cont1.dimensaoTotal())
print('Populacao total:',cont1.populacaoTotal())
print('Maior pais :',cont1.maiorDimensao().getCodigo())
print('Menor pais:',cont1.menorDimensao().getCodigo())
print('Pais mais populoso:',cont1.maisPopuloso().getCodigo())
print('Pais menos populoso:',cont1.menosPopuloso().getCodigo())
print('razao do maior territorio pelo menor',cont1.razaoTerritorial())

