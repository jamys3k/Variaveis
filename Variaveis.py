# Variaveis

# Qual a definição?

# Um mecanismo de armazenamento volátil de dados, ou seja, dados salvos em "pedacinhos" da memória RAM do sistema em uso, sendo ele qual for, 
# Desktop, Notebook ou qualquer dispositivo que possuia um sistema programado em qualquer linguagem.

# Declaração

print("A criação de variavéis e atribuição de valores, sendo float, int ou string, no pyhton, fazemos da seguinte maneira:")

idade = 20
print(idade)

idade = 21
print(idade)

nome = 'jamys'
print(nome)

sobrenome = "Henrique"
print(sobrenome)

# Essa maniera de declação de variaveis é simples, podendo ser alterado o valor em posteriori, como no exemplo acima. (Possuímos aqui o tipo de 
# variavel "String" que pode-se utilizar de as duplas "" ou aspas simples '' mas é sempre interessante manter o padrão. ou simples ou duplas para todo o documento)

# Tipos nativos
# Tipos numéricos: Inteiros(int) e decimais(float)

preco = 1000 #Int
tipo_preco = type(preco)

print(preco)
print(tipo_preco)

juros = 0.5 #float
tipo_juros = type(juros)

print(juros)
print(tipo_juros)

# Tipos de texto: strings (str)
primeiro_nome = "Jamys" #string
print(primeiro_nome)
print(type(primeiro_nome))

pais = 'Brasil' #String

print(pais)
print(type(pais))

# Tipos lógicos: Booleanos(bool)

usuario_maior_de_idade = False

print(usuario_maior_de_idade)
print(type(usuario_maior_de_idade)) #bool

#Tipo vazio (NoneType)

telefone_fixo = None

print(telefone_fixo)
print(type(telefone_fixo)) #NoneType
