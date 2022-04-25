# VERSÃO FINAL - ÚNICA - V1.0
# ALTERADA EM 03/04 -- 18:30


# EXPORTAÇÕES:
import plotly.express as px
from pandas import read_excel
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go


# DECLARAÇÃO DO 1º DATAFRAME:
df1 = read_excel("https://github.com/Trabalho-APC-DASH/Painel-APC/blob/main/Banco%20de%20Dados/Brasil-Exportacao_cafe_por_pais.xlsx?raw=true")

# DECLARAÇÃO DO 2º DATAFRAME:
df2 = read_excel('https://github.com/Trabalho-APC-DASH/Painel-APC/blob/main/Banco%20de%20Dados/UnidadesReceita.xlsx?raw=true')

# DECLARAÇÃO DO 3º DATAFRAME:
df3 = read_excel('https://github.com/Trabalho-APC-DASH/Painel-APC/blob/main/Banco%20de%20Dados/Preco_Medio.xlsx?raw=true')

# DECLARAÇÃO DO 4º DATAFRAME:
df4 = read_excel('https://github.com/Trabalho-APC-DASH/Painel-APC/blob/main/Banco%20de%20Dados/Paises_exportadores_cafe.xlsx?raw=true')



# INÍCIO A ORGANIZAÇÃO DE DADOS:
# =========================================================================
# DATAFRAME 1)

# ORGANIZAÇÃO DAS OPÇÕES PARA O DROPDOWN:
def funcao_unique(lista):

    resultado = []

    unicidade = set(lista)

    for elemento in unicidade:
        resultado.append(elemento)

    return resultado

opcoes = funcao_unique(df1['CONTINENTE'])

opcoes.insert(0, 'Todos os Continentes')
del opcoes[1]
opcoes2 = ['ARÁBICA (Por sacas de 60kg)', 'CONILLON (Por sacas de 60kg)', 'SOLÚVEL (Por sacas de 60kg)', 'TORRADO (Por sacas de 60kg)', 'TOTAL']

# DECLARAÇÃO DE COMO O GRÁFICO IRÁ SER ORGANIZADO:
fig1 = px.bar(df1, x="CONTINENTE", y="TOTAL", color="PAÍS DESTINO", title='Compra de Café Brasileiro por País')


#Definição de Cores para o background dos graficos

colors = {
    'background' : '#392620',    
}

# ===========================================================================
# DATAFRAME 2)

# TRANSFORMAÇÃO DO DF2 PARA UMA LISTA MODIFICÁVEL:
lista = df2.values

# DECLARAÇÃO DO DATAFRAME OFICIAL DO DF2:
dfOf1 = []

# REORGANIZAÇÃO DO DF2:
for n in lista:
    dfOf1 += [[n[0], n[1], 'Importação Jan/Fev2022']]
    dfOf1 += [[n[0], n[3], 'Exportação Jan/Fev2022']]
    dfOf1 += [[n[0], n[5], 'Importação Jan/Fev2021']]
    dfOf1 += [[n[0], n[7], 'Exportação Jan/Fev2021']]


# DECLARAÇÃO DE COMO O GRÁFICO IRÁ SER ORGANIZADO:
fig2 = px.bar(dfOf1, x=0, y=1, color=2, barmode="group", title='Exportação/Importação por Receita Federal', labels={
             '0': 'Unidade Da Receita Federal',
             '1': 'Sacas (60kg)',
             '2': 'Tipo'
            })



# ============================================================================
# DATAFRAME 3)


# MEMORIZAÇÃO DAS COLUNAS DA PRIMEIRA LINHA PRESENTE NO DATAFRAME 3:
opcoes3 = []
for n in df3:
    opcoes3 += [n]

# EXCLUSÃO DE DADOS DESNECESSÁRIOS PARA EXIBIÇÃO NO GRÁFICO:
del opcoes3[0]
del opcoes3[6]

# DECLARAÇÃO PRIMÁRIA DE COMO O GRÁFICO IRÁ SER ORGANIZADO:
fig3 = go.Figure()

for cafe in opcoes3:
    fig3.add_trace(go.Scatter(x=df3['Mês/Ano'], y=df3[cafe],
                        mode='lines', name=cafe))

# ATUALIZAÇÃO DE TÍTULO E NOMEAÇÃO DA PARTE VERTICAL DO GRÁFICO E HORIZONTAL:
fig3.update_layout(title='Preço Médio do Café Brasileiro',
                   xaxis_title='Ano',
                   yaxis_title='Preço (R$)')

# INSERÇÃO DE UMA NOVA OPÇÃO PARA O DROPDOWN:
opcoes3.insert(0, 'Todos os Tipos de Café')

# ==============================================================================
# DATAFRAME 4)

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
                         hover_data=[2], # Definição de Acrescimo de informação, neste caso a coluna 2 esta sendo acrescentada nos dados do mapa, que são as Produções
                         labels={'3':'Continente', '0':'País ID', "2":'Produção'} # Renomeação dos tópicos no mapa, para que seja melhor interpretado
)

fig4.update_geos(
    landcolor="#06832F",
    oceancolor="#1E8AC9",
    showocean=True,
    lakecolor="#5FC4D0",
)
# =======================================================================================




# INÍCIO PARA EXECUÇÃO DO LAYOUT E INSERÇÃO DOS GRÁFICOS:
app = Dash(__name__)

app.layout = html.Div(className='Tudo' , children=[

    
    html.Nav(className='BarraNavegacao', children=[

    ]),
    

    html.Div(className='Letreiro1', children=[
        
        html.H1(children=['Café☕'], className='Titulo'),
    
    ]),


    html.Div(className='Todos', children= [

    html.Div(className='PrimeiroGrafico' , children=[
      
        html.Div(className='Dropdowns', children=[
            dcc.Dropdown(opcoes, value='Todos os Continentes', id='Filtro_Continentes', className='Dropdown1', style={
                        'background-color': 'chocolate',
                        'border-radius': '14px',
                        'border-color': 'transparent',                       
                        }),
            ]),
           html.Div(children=[
            dcc.Dropdown(opcoes2, value='TOTAL', id='Filtro_Tipo', className='Dropdown2', style={
                        'background-color': 'chocolate',
                        'border-radius': '14px',
                        'border-color': 'transparent',                       
                        }),
            ]),
        dcc.Graph(
        id='Grafico_dados',
        figure=fig1
        )
       
    ]),

    html.Div(className='SegundoGrafico', children=[

        dcc.Graph(
        id='Grafico_dados2',
        figure=fig2
    )
    ]),

    html.Div(className='TerceiroGrafico', children=[

        dcc.Dropdown(opcoes3, value='Todos os Tipos de Café', id='filtro3', className='Dropdown3', style={
                     'background-color': 'chocolate',
                     'border-radius': '14px',
                     'border-color': 'transparent'}),

        dcc.Graph(
            id='Grafico_dados3',
            figure=fig3
        ),

    ]),

    html.Div(className='QuartoGrafico', children=[

        dcc.Graph(
        id='Grafico_dados4',
        figure=fig4
    )
    ])
    ])  
    ]) 

# =====================================================================================================================
# INICIAÇÃO AOS CALLBACKS:

# CALLBACK PARA O GRÁFICO 1 (EM BARRAS):

# DEFINIÇÃO DE FUNÇÃO PARA FILTRAGEM QUE IRÁ SUBSTITUIR A FUNÇÃO 'LOC' DO PANDAS:
def filtragem(dataframe, pesquisa, coluna):
    Filtro = []
    
    if coluna == None:
        
        for linha in dataframe:
            if linha[0] == pesquisa:
                Filtro += [[linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6]]]


    else:
        referencia = 2
        for alternativa in opcoes2:
            if str(coluna) == str(alternativa):
                for linha in dataframe:
                    if linha[0] == pesquisa:
                        Filtro += [[linha[0], linha[1], linha[referencia]]]
            referencia += 1
        

    return Filtro


@app.callback(
    Output('Grafico_dados', 'figure'),
    Input('Filtro_Tipo', 'value'),
    Input('Filtro_Continentes', 'value')
)
def update_de_dash(tipo, continente):
    dfFl1 = df1.values

    if tipo == 'TOTAL':
        if continente == 'Todos os Continentes':

            fig1 = px.bar(df1, x="CONTINENTE", y="TOTAL", color="PAÍS DESTINO", title='Compra de Café Brasileiro por País por Continente')

        else:  

            filtro = filtragem(dfFl1, str(continente), None)
            fig1 = px.bar(filtro, x=0, y=6, color=1, title=f'Compra de Café Brasileiro ({continente})', labels={'0': 'CONTINENTE', '6': 'TOTAL', '1': 'PAÍS DESTINO'})

    else:
        if continente == 'Todos os Continentes':

            fig1 = px.bar(df1, x="CONTINENTE", y=str(tipo), color="PAÍS DESTINO", title=f'Compra de Café {tipo} Brasileiro por Continente')

        else:

            filtro = filtragem(dfFl1, str(continente), str(tipo))
            fig1 = px.bar(filtro, x=0, y=2, color=1, title=f'Compra de Café {tipo} Brasileiro ({continente})', labels={'0': 'CONTINENTE', '1': 'PAÍS DESTINO', '2': tipo})

    return fig1

# ======================================================================================================================
# CALLBACK PARA O GRÁFICO 2:
@app.callback(
    Output('Grafico_dados3', 'figure'),
    Input('filtro3', 'value')
)
def UpdateDeDash1(value):
    if value == 'Todos os Tipos de Café':

        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=df3['Mês/Ano'], y=df3['Conillon'],
                            mode='lines',
                            name='Conillon'))
        fig3.add_trace(go.Scatter(x=df3['Mês/Ano'], y=df3['Arábica'],
                            mode='lines',
                            name='Arábica'))
        fig3.add_trace(go.Scatter(x=df3['Mês/Ano'], y=df3['Total Café Verde'],
                            mode='lines', name='Total (Café Verde)'))

        fig3.add_trace(go.Scatter(x=df3['Mês/Ano'], y=df3['Torrado'],
                            mode='lines', name='Torrado'))
        fig3.add_trace(go.Scatter(x=df3['Mês/Ano'], y=df3['Solúvel'],
                            mode='lines', name='Solúvel'))
        fig3.add_trace(go.Scatter(x=df3['Mês/Ano'], y=df3['Total Industrializado'],
                            mode='lines', name='Total (Industrializado)'))

        fig3.update_layout(title='Preço Médio do Café Brasileiro',
                        xaxis_title='Ano',
                        yaxis_title='Preço Médio (R$)')

    else:

        fig3 = px.line(df3, x='Mês/Ano', y=str(value), title=f'Preço Médio ({value}) Brasileiro', labels={ str(value) : f'Preço Médio (R$) - {value}'})

    return fig3

if __name__ == '__main__':
    app.run_server(debug=True)