#AULA 1 - CURSO PYTHON DATA SCIENCE - https://youtu.be/1xXK_z9M6yk
#PROFESSOR MEIGAROM

#demanda do exercício de fixação, carregar conjunto de dados e responder as perguntas
'''
1. Quantas casa estão disponíveis para compra?
2. Quantos atributos as casas possuem? (número de quartos, numero de garagens, m2, vista pro mar)
3. Quais são os atributos
4. Qual a casa mais cara do portfólio (casa com maior valor)?
5. Qual a casa com o mair número de quartos?
6. Qual a soma total de quartos do conjunto dados?
7. Quantas casas possuem 2 banheiros?
8. Qual o preço médio de todas as casas no conjuno de dados?
9. Qual o preço médio de casas com 2 banheiros?
10. Qual o preço mínimo entre as casas com 3 quartos?
11. Quantas casas possuem mais de 300 metros quadrados na sala de estar?
12. Quantas casas tem mais de 2 andares?
13. Quantas casas tem vista para o mar?
14. Das casas com vista para o mar, quantas tem 3 quartos?
15. Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros?


https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
https://paulovasconcellos.com.br/28-comandos-%C3%BAteis-de-pandas-que-talvez-voc%C3%AA-n%C3%A3o-conhe%C3%A7a-6ab64beefa93

https://anandology.com/python-practice-book/index.html
'''

import pandas as pd
data = pd.read_csv('ds/kc_house_data.csv')
print(f'1. Quantas casa estão disponíveis para compra?\n {len (data.index)}')
print(f'2. Quantos atributos as casas possuem? (número de quartos, numero de garagens, m2, vista pro mar?\n {len(data.columns)}')
print(f'3. Quais são os atributos?\n {data.columns}')
df2= data.set_index('price').max(1) #print(f'4. Qual a casa mais cara do portfólio (casa com maior valor)?\n {df2.head() }')
#print(f'4. Qual a casa mais cara do portfólio (casa com maior valor)?\n {data.max(axis="columns").sort_values(ascending=False) }')
print(f'4. Qual a casa mais cara do portfólio (casa com maior valor)?\n {(data.sort_values("price", ascending=False)).head(1) }')
print(f'5. Qual é a casa com o maior número de quartos?\n {(data.sort_values("bedrooms", ascending=False)).head(1)}')
df3= data['bedrooms'].sum()
print(f'6. Qual a soma total de quartos do conjunto dados?\n {df3}')
print(f'7. Quantas casas possuem 2 banheiros?\n {len (data.loc[data["bathrooms"] == 2])}')
df4= data['price'].median()
print(f'8. Qual o preço médio de todas as casas no conjuno de dados?\n {df4}')
df5=(data.loc[data["bathrooms"] == 2]).median()
print(f'9. Qual o preço médio de casas com 2 banheiros?\n {df5["price"]}')
df6=(data.loc[data["bathrooms"] == 3])
df7 = df6.sort_values("price", ascending=True).head(1)
#df6.sort_values("price", ascending=True).head(1)
print(f'10. Qual o preço mínimo entre as casas com 3 quartos?\n {df7["price"]}')
df8=(data.loc[data["sqft_living"] >=300])
print(f'11. Quantas casas possuem mais de 300 metros quadrados na sala de estar?\n {len (df8)}')
df9=(data.loc[data["floors"] >2])
print(f'12. Quantas casas tem mais de 2 andares?\n {len (df9)}')
df10=(data.loc[data["waterfront"] ==1])
print(f'13. Quantas casas tem vista para o mar?\n {len (df10)}')
df11=(data.loc[(data["waterfront"] ==1) & (data["bedrooms"] ==3)])
print(f'14. Das casas com vista para o mar, quantas tem 3 quartos?\n {len (df11)}')
print(f'15. Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros?\n {len (df8.loc[df8["bathrooms"] >2])}')

'''
Para fechar a AULA 01 de PYTHON do ZERO ao DS:

Essas são as respostas finais com os códigos:

#1. Quantas casas estão disponíveis para compra?
# R: 21613
print( df1.shape[0] )

#2. Quantos atributos as casas possuem?
# R: 21
print( df1.shape[1] )

#3. Quais são os atributos das casas?
print( df1.columns )

#4. Qual a casa mais cara ( casa com o maior valor de venda )?
# R: O imóvel com o id 6762700020 é o mais caro
print( df1[['id', 'price']].sort_values( 'price', ascending=False ) )

#5. Qual a casa com o maior número de quartos?
# R: O imóvel com o id 2402100895 tem 33 quartos
print( df1[['id', 'bedrooms']].sort_values( 'bedrooms', ascending=False ) )

#6. Qual a soma total de quartos do conjunto de dados?
# R: A soma total de quartos é de 72854
print( df1['bedrooms'].sum() )

#7. Quantas casas possuem 2 banheiros?
# R: 1930 imóveis possem 2 banheiros
print( df1[df1['bathrooms'] == 2].shape )

#8. Qual o preço médio de todas as casas no conjunto de dados?
# R: O preço médio dos imóvesi do conjunto de dados é de R$ 540.088,14
print( df1['price'].mean() )

#9. Qual o preço médio de casas com 2 banheiros?
# R: O preço médio das casas com 2 banheiros é de R$ 457.889,71
print( df1.loc[df1['bathrooms'] == 2, 'price'].mean() )
    
#10. Qual o preço mínimo entre as casas com 3 quartos?
# R: O preço mínimo das casas de 3 quartos é de R$ 82.000,0
print( df1.loc[df1['bedrooms'] == 3, 'price'].min() )

#11. Quantas casas possuem mais de 300 metros quadrados na sala de estar?
# OBS: 1 pé quadrado = 0,09 metros quadrados
# R: 2141 imóveis possuem mais de 300 metros quadrados na sala de estar.
df1['m2_living'] = df1['sqft_living'] * 0.092
print( df1[df1['m2_living'] > 300].shape )

#12. Quantas casas tem mais de 2 andares?
# R: 782 imóveis tem mais de 2 andares
print( df1[df1['floors'] > 2].shape )

#13. Quantas casas tem vista para o mar?
# R: 163 imóves tem vista para o mar
print( df1[df1['waterfront'] == 1].shape )

#14. Das casas com vista para o mar, quantas tem 3 quartos?
# R: 64 imóveis tem vista para o mar e possuem 3 quartos
print( df1[(df1['waterfront'] == 1 ) & ( df1['bedrooms'] == 3 )].shape )

#15. Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros?
# R: 288 imóveis tem mais de 300 metros quadrados de sala de estar e mais de 2 banheiros
print( df1[(df1['m2_living'] > 300) & (df1['bathrooms'] > 2)].shape )
'''