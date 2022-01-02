# Api Moeda

Este projeto é uma extensão da API [Awesome API](https://docs.awesomeapi.com.br). 
Basicamente, ele mostra todas as moedas que a Awesome API tem e todas as suas conversões possíveis de serem utilizadas, além de mostrar o país de cada moeda.
## Tecnologias utilizadas
* Python 3.8
* Selenium
* BeautifulSoup
* pandas
* Json
* Flask

1. ### Como usar:
    * Fazendo uma requisição:
    ```
    import requests as r

    #Pegar os tipos de moedas
    dados_moedas = r.get("http://apimoeda.herokuapp.com/moedas")

    #Pegar os tipos de conversões
    dados_conversões =  r.get("http://apimoeda.herokuapp.com/conversao")
    ```
2. ### Manipulando o arquivo em formato json
    * Fazendo a conversão:
    ```
    import json
    dict_moedas = dados_moedas.json()
    dict_conversoes = dados_conversões.json()
    ```
3. ### Obtendo os valores e chaves:
    ```
    for i in dict_moedas['Tipo da moeda']:
    for key, value in i.items():
        print(key,value)

    for i in dict_conversoes['Tipo de conversao']:
    for key, value in i.items():
        print(key,value)
    ```
4. ### Criando uma tabela de forma estruturada
```
import pandas as pd
#Pegando os valores de cada dicionário
values = [value.values() for value in dict_moedas['Tipo da moeda']]
#Pegando as chaves de cada dicionário
keys = [key.keys() for key in dict_moedas['Tipo da moeda']]

df = pd.DataFrame(values, index=keys, columns=['Cód Moeda', "País"])
print(df)
```
5. ### Resultado
* Para o caso de Moedas

|   |      Cód Moeda      |  País |
|----------|:-------------:|------:|
|(Cod_da_moeda, Paises)  |   AFN | Afghani do Afeganistao
(Cod_da_moeda, Paises)   |   MGA |  Ariary Madagascarense
(Cod_da_moeda, Paises)   |   THB |         Baht Tailandes
(Cod_da_moeda, Paises)   |   PAB |       Balboa Panamenho
(Cod_da_moeda, Paises)   |   ETB |            Birr Etiope
...                      |    ...|                     ...
(Cod_da_moeda, Paises)   |   XAGG|                  XPrata
(Cod_da_moeda, Paises)   |    XRP|                     XRP
(Cod_da_moeda, Paises)   |    CNY|             Yuan Chines
(Cod_da_moeda, Paises)   |    CNH|    Yuan chines offshore
(Cod_da_moeda, Paises)   |    PLN|           Zloti Polones

[155 rows x 2 columns]

## Feito por
Abel ❤️

__Minhas Rede Sociais__:
* [Linkedin](https://www.linkedin.com/in/abel-rapha-data-science/)
* [Email](contato@abelrapha.com)
* [Canal do YouTube](https://www.youtube.com/channel/UCwA0jaKFfgyOUrWx5CN_Nzw) 
* [Instagram](https://www.instagram.com/abel_rapha/)
* [Github](https://github.com/AbelRapha)
