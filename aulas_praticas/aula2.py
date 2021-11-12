#AULA 2 - CURSO PYTHON DATA SCIENCE - https://youtu.be/1xXK_z9M6yk
#EXTRAÇÃO E MANIPULAÇÃO DE DADOS - I - BÁSICO
#PROFESSOR MEIGAROM
'''
BOM DIA GALERAAAA, TUDO BEM COM VOCÊS!!
Acabei de fazer os exercícios da Aula 02 de Python e cheguei nesses resultados:

Mais alguém conseguiu? Vamos comparar os resultados!
8. Qual a data mais antiga de construção de um imóvel?
R: 1900
9. Qual a data mais antiga de renovação de um imóvel?
R: 1934
10. Quantos imóveis tem 2 andares?
R: 8241
11. Quantos imóveis estão com a condição igual a “regular” ?
R: 19.710 imóveis com condição regular.
12. Quantos imóveis estão com a condição igual a “bad”e possuem “vista para água” ?
R: 2 imóveis "bad" com "vista para água"
13. Quantos imóveis estão com a condição igual a “good” e são “new_house”?
R: 1701
14. Qual o valor do imóvel mais caro do tipo “studio” ?
R: 1.247.000,00
15. Quantos imóveis do tipo “apartment” foram reformados em 2015 ?
R: 0 imóveis
16. Qual o maior número de quartos que um imóveis do tipo “house” possui ?
R: 33 quartos
17. Quantos imóveis “new_house” foram reformados no ano de 2014?
R: 91 imóveis
'''

import pandas as pd
data = pd.read_csv('ds/kc_house_data.csv')

#EXEMPLOS

#MOSTRAR NA TELA O TIPO DE DADOS DE CADA COLUNA

#print(data.dtypes)

#formatar para o formato datetime
ex_data = pd.to_datetime(data['date'])

print(ex_data)

#CONVERTER UM TIPO DE VARIAVEL PARA OUTRO
ex_float = data['bedrooms'].astype(float)
# dentro do astype pode ser: (float, int"(32)",int64,str,)

#Exibir determinadas linhas e quais colunas
print(data[['id','bedrooms']].head(3))

## CRIANDO NOVAS COLUNAS DENTRO DA BASE DE DADOS

data['teste']='teste de um novo valor'

#DELETAR VARIAVEIS
data = data.drop(['teste'], axis=1) #sobrescrevo o conjunto data
colunas_que_quero_remover = ['teste','id']
#data = data.drop(colunas_que_quero_remover, axis=1)

#SELECIONAR AS COLUNAS
colunas_que_quero_selecionar = ['date','id','bedrooms']

print(data[['date']])
#print(data[colunas_que_quero_selecionar)

#Procurar pelos índices das linhas e colunas
#data[linhas,colunas]

print(data.iloc[0:10,0:3])

print(data.loc[:,colunas_que_quero_selecionar])

#RESPONDENDO AS PERGUNTAS
print('1. Qual a data mais antiga do portfolio?')
data['date']=pd.to_datetime(data['date'])
print(data.sort_values('date',ascending=True).head(1))

print('\n2. Quantos imóveis possuem o número máximo de andares?')
print(data['floors'].unique())
print(data['floors'].unique().max())

print(data[data['floors']==3.5].shape)
print(len (data[data['floors']==3.5]))

print('\n3. Criar uma classificação para os imóveis de alto e baixo padrão de acordo com a condição do preço')
	data['level'] ='standard'

	data.loc[data['price']>540000,'level']='high level'
	data.loc[data['price']<540000,'level']='low level'

print(data.head())

print('\n4. Criar um relatório ordenado pelo Preço, id, data, nº de quartos, metros e nível')
cols_4 = ['id','date','price','bedrooms','sqft_lot','level']

report = data[cols_4].sort_values('price',ascending=False)

print(report.head())

report.to_csv('ds/relatorio_aula2.csv', index=False)

print('\n5. Criar um mapa onde exibe as casas ')

import plotly.express as px
data_map = data[['id', 'lat','long','price','level']]

print(data_map)
mapa = px.scatter_mapbox(data_map, lat='lat', lon='long', hover_name='id',
               hover_data=['price','level'],
               color_discrete_sequence=['purple'],
               zoom=3,
               height=500
               )

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(margin={'r':0,'t':0,'l':0,'b':0})
#mapa.show()

#mapa.write_html('ds/mapa.html')

#RESPONDENDO AS PERGUNTAS
print('1. Crie uma nova coluna chamada house_age. Se o valor da coluna date for maior que 2014-01-01 -> new_house; Se o valor da coluna date for menor, old_house.')
data['date']=pd.to_datetime(data['date'])
data['house_age'] ='old_house'
data.loc[data['date']>='2014-06-30','house_age']='new_house'

print(data.loc[:4,['id','price','date','house_age']])
#print(data.loc[data['date']<'2014-01-01'])

print('\n2. Crie uma nova coluna chamada "dormitory_type". Se o valor da coluna "bedrooms" for igual a 1: "studio"; se for igual 2: "apartment". Se for maior que 2:"house".')
data['dormitory_type'] ='studio'
data.loc[data['bedrooms']==2,'dormitory_type']='apartment'
data.loc[data['bedrooms']>2,'dormitory_type']='house'
print(data.loc[:4,['id','price','dormitory_type','bedrooms']])

print('\n3. Crie uma nova coluna "condition_type". Se o valor da coluna "condition" for menor ou igual a 2: bad. Se for 3 ou 4 regular. Se o valor for 5: good.')
data['condition_type'] ='regular'
data.loc[data['condition']<=2,'condition_type']='bad'
data.loc[data['condition']>4,'condition_type']='good'
print(data.loc[:4,['id','price','dormitory_type','bedrooms','condition','condition_type']])

print('\n4. Modifique o TIPO da coluna para "condition" para string.')
print(data[['id','price','condition','condition_type']].dtypes)
data['condition'] = data['condition'].astype(str)
print('\n')
#print(data[['id','price','condition','condition_type']].dtypes)
print(data.loc[:4,['id','price','condition','condition_type']].dtypes)

print('\n5. Delete as colunas: "sqft_living15" e "sqft_lot15".')
print(data[['id','price','sqft_living15','sqft_lot15']].head())
data = data.drop(['sqft_living15','sqft_lot15'], axis=1) #sobrescrevo o conjunto data
print(data.columns)

print('\n6. Modifique o tipo da coluna "yr_built" para date.')
data['yr_built']=pd.to_datetime(data['yr_built'])
print(data[['yr_built']].dtypes)

print('\n7. Modifique o tipo da coluna "yr_renovated" para DATE')
data['yr_renovated']=pd.to_datetime(data['yr_renovated'])
print(data[['yr_renovated']].dtypes)

print('8. Qual a data mais antiga de construção de um imóvel?')
print(data[['id','yr_renovated','yr_built','house_age']].sort_values('yr_built',ascending=True).head(1))
print('9. Qual a data mais antiga de renovação de um imóvel?')
print(data[['id','yr_renovated','yr_built','house_age']].sort_values('yr_renovated',ascending=True).head(1))

print('10. Quantos imóveis tem 2 andares?')
print (len (data.loc[data["floors"] == 2]))

print('11. Quantos imóveis estão com a condição igual a “regular” ?')
print (len (data.loc[data["condition_type"] == 'regular']))

print('12. Quantos imóveis estão com a condição igual a “bad”e possuem “vista para água” ?')
print (len (data.loc[(data["condition_type"] == 'bad') & (data["waterfront"] == True)]))

print('13. Quantos imóveis estão com a condição igual a “good” e são “new_house”?')
print (len (data.loc[(data["condition_type"] == 'good') & (data["house_age"] == 'new_house')]))

print('14. Qual o valor do imóvel mais caro do tipo “studio” ?')
print ( (data.loc[data["dormitory_type"] == 'studio'].sort_values('price',ascending=False).head(1)))

print('15. Quantos imóveis do tipo “apartment” foram reformados em 2015 ?')
print (len (data.loc[(data["dormitory_type"] == 'apartment') & (data["yr_renovated"] >= '2015-01-01')]))

print('16. Qual o maior número de quartos que um imóveis do tipo “house” possui ?')
print(data['bedrooms'].loc[data["dormitory_type"] == 'house'].unique().max())
print('17. Quantos imóveis “new_house” foram reformados no ano de 2014?')
print (len (data.loc[(data["house_age"] == 'new_house') & (data["yr_renovated"] >= '2014-01-01') & (data["yr_renovated"] < '2015-01-01')]))
