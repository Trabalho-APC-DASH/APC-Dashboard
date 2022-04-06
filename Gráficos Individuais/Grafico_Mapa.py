# VERSÃO BETA V1.1 EM MAPA
# EDITADO EM 01/04 ÀS 16:15

import plotly.express as px
from pandas import read_excel
from dash import Dash, dcc, html

# FUNCIONAMENTO DO SITE
app = Dash(__name__)

# DEFINIÇÃO DO BANCO DE DADOS:
df4 = read_excel('https://github.com/Trabalho-APC-DASH/Painel-APC/blob/main/Banco%20de%20Dados/Paises_exportadores_cafe.xlsx?raw=true')

# TRANSFORMAÇÃO DO DF4 PARA UMA LISTA MODIFICÁVEL:
Lista3 = df4.values

# LISTA DE TODOS OS PAÍSES DIVIDIDO POR CONTINENTES PARA SER UTILIZADO NO PASSSO MAIS ABAIXO:
Oceania = ['Estados Federados da Micronésia', 'Fiji', 'Ilhas Marshall', 'Ilhas Salomão', 'Kiribati' ,'Nauru', 'Nova Zelândia', 'Palau', 'Papua-Nova Guiné', 'Samoa', 'Tonga', 'Tuvalu', 'Vanuatu', 'Ilhas Cook']
América_do_Norte = ['Canadá', 'Estados Unidos da América', 'México']
América_Central = ['Antígua e Barbuda', 'Bahamas', 'Barbados', 'Belize', 'Costa Rica', 'Cuba', 'Dominica', 'El Salvador', 'Granada', 'Guatemala', 'Haiti', 'Honduras', 'Jamaica', 'Nicarágua', 'Panamá', 'República Dominicana', 'Santa Lúcia', 'São Cristóvão e Névis', 'São Vicente e Granadinas', 'Trindade e Tobago']
América_do_Sul = ['Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 'Equador', 'Guiana', 'Guiana Francesa', 'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela']
Europa = ['Albânia', 'Alemanha', 'Andorra', 'Áustria', 'Bélgica', 'Bielorrússia', 'Bósnia e Herzegovina', 'Bulgária', 'Cazaquistão', 'Chipre', 'Croácia', 'Dinamarca', 'Eslováquia', 'Eslovênia', 'Espanha', 'Estônia', 'Finlândia', 'França', 'Grécia', 'Hungria', 'Irlanda', 'Islândia', 'Itália', 'Letônia', 'Liechtenstein', 'Lituânia', 'Luxemburgo', 'Malta', 'Moldávia', 'Mônaco', 'Montenegro', 'Noruega', 'Países Baixos', 'Polônia', 'Portugal', 'Tchéquia', 'Macedônia do Norte', 'Inglaterra', 'Irlanda do Norte', 'Escócia', 'País de Gales', 'Romênia', 'Rússia', 'San Marino', 'Sérvia', 'Suécia', 'Suíça', 'Turquia', 'Ucrânia', 'Vaticano']
Ásia = ['Timor Leste', 'Birmânia', 'Afeganistão', 'Arábia Saudita', 'Armênia', 'Azerbaijão', 'Bahrein', 'Bangladesh', 'Brunei', 'Butão', 'Camboja', 'Cazaquistão', 'Catar', 'China', 'Chipre', 'Cingapura', 'Coreia do Norte', 'Coreia do Sul', 'Egito', 'Emirados Árabes', 'Filipinas', 'Geórgia', 'Iêmen', 'Índia', 'Indonésia', 'Irã', 'Iraque', 'Israel', 'Japão', 'Jordânia', 'Kuwait', 'Laos', 'Líbano', 'Malásia', 'Maldivas', 'Mianmar', 'Mongólia', 'Nepal', 'Omã', 'Paquistão', 'Quirguistão', 'Rússia', 'Síria', 'Sri Lanka', 'Tajiquistão', 'Tailândia', 'Timor-Leste', 'Turcomenistão', 'Turquia', 'Uzbequistão', 'Vietnã', 'Taiwan', 'República Popular da China']
África = ['África do Sul', 'Angola', 'Argélia', 'Benim', 'Botswana', 'Burquina Faso', 'Burundi', 'Camarões', 'Chade', 'Costa do Marfim', 'Djibouti', 'Egito', 'Eritreia', 'Etiópia', 'Gabão', 'Gâmbia', 'Gana', 'Guiné', 'Guiné-Bissau', 'Guiné Equatorial', 'Madagáscar', 'Cabo Verde', 'Comores', 'São Tomé e Príncipe', 'Seychelles', 'Lesoto', 'Libéria', 'Líbia', 'Malawi', 'Mali', 'Marrocos', 'Mauritânia', 'Moçambique', 'Namíbia', 'Níger', 'Nigéria', 'Quênia', 'República da África Central', 'República Democrática do Congo', 'República do Congo', 'República de Maurício', 'Ruanda', 'Senegal', 'Serra Leoa', 'Somália', 'Eswatini', 'Sudão', 'Sudão do Sul', 'Tanzânia', 'Togo', 'Tunísia', 'Uganda', 'Zâmbia', 'Zimbábue', 'República Popular do Congo']

# DECLARAÇÃO DO DATAFRAME OFICIAL DO DF4:
dfOf3 = []

# INÍCIO DE REPETIÇÃO PARA CADA ELEMENTO DA LISTA "ListaDeFiltro"
for ln in Lista3:
    for cont in Oceania: # INÍCIO DE REPETIÇÃO PARA CADA ELEMENTO DA LISTA "Oceania"

        if ln[1] == cont: # CASO O PAÍS DA LISTA DE FILTRO SE ENCONTRE NA DA OCEANIA, SEU CONTINENTE SERÁ OCEANIA.
            dfOf3 += [[ln[0], ln[1], ln[2],'Oceania']]

    for cont in América_do_Norte: # INÍCIO DE REPETIÇÃO PARA CADA ELEMENTO DA LISTA "América_Do_Norte"

        if ln[1] == cont: # CASO O PAÍS DA LISTA DE FILTRO SE ENCONTRE NA AMÉRICA DO NORTE, SEU CONTINENTE SERÁ AMÉRICA DO NORTE.
            dfOf3 += [[ln[0], ln[1], ln[2], 'América do Norte']]

    for cont in América_Central: # MESMA LÓGICA DOS PASSOS ANTERIORES...
        if ln[1] == cont:
            dfOf3 += [[ln[0], ln[1], ln[2], 'América Central']]

    for cont in América_do_Sul:
        if ln[1] == cont:
            dfOf3 += [[ln[0], ln[1], ln[2], 'América do Sul']]

    for cont in Europa:
        if ln[1] == cont:
            dfOf3 += [[ln[0], ln[1], ln[2], 'Europa']]

    for cont in Ásia:
        if ln[1] == cont:
            dfOf3 += [[ln[0], ln[1], ln[2], 'Ásia']]

    for cont in África:
        if ln[1] == cont:
            dfOf3 += [[ln[0], ln[1], ln[2], 'África']]


# DECLARAÇÃO DE COMO O GRÁFICO IRÁ SER ORGANIZADO:
fig4 = px.scatter_geo(dfOf3, # Definição do DataFrame a ser utilizado
                         title= 'Produção de Café Anual (Toneladas)',
                         locations= 0, # As localizações se darão da coluna 0 do DataFrame, que são os ID's
                         projection= 'orthographic', # Projeção do mapa no tipo Ortográfica
                         opacity= 1, # Definição da opacidade das bolinhas no mapa
                         hover_name= 1, # Dado de Nome, que foi definido pela coluna 1 do DataFrame, que é os Países
                         color= 3, # Definição da separação de cores, definida pela coluna 3 do DataFrame, que são os continentes
                         height=800,
                         hover_data=[2], # Definição de Acrescimo de informação, neste caso a coluna 2 esta sendo acrescentada nos dados do mapa, que são as Produções
                         labels={'3':'Continente', '0':'País ID', "2":'Produção'} # Renomeação dos tópicos no mapa, para que seja melhor interpretado
)

fig4.update_geos(
    landcolor="#06832F",
    oceancolor="#1E8AC9",
    showocean=True,
    lakecolor="#5FC4D0",
)

# LAYOUT DO SITE:
app.layout = html.Div(children=[

    dcc.Graph(
        id='Grafico_dados',
        figure=fig4
    )

]) 

# SINTAXE PARA DEIXAR O SITE NO AR:
if __name__ == '__main__':
    app.run_server(debug=True)