# VERSÃO V3.0 Final em Barras
# EDITADO EM 22/03 ÀS 20:02

import plotly.express as px # Importação do Plotly para criar o design dos gráficos
from pandas import read_excel # Importação da função read_excel, para ler excel, da biblioteca Pandas
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__) # Isso aqui tem a função de colocar o site pra funcionar

# DECLARAÇÃO DO BANCO DE DADOS A SER UTILIZADO:
df1 = read_excel("https://github.com/Trabalho-APC-DASH/Painel-APC/blob/main/Banco%20de%20Dados/Brasil-Exportacao_cafe_por_pais.xlsx?raw=true")


# ORGANIZAÇÃO DAS OPÇÕES PARA O DROPDOWN:

# FUNÇÃO QUE IRÁ SUBSTITUIR A FUNÇÃO 'UNIQUE' DO NUMPY:
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
fig1 = px.bar(df1, x="CONTINENTE", y="TOTAL", color="PAÍS DESTINO", height=700, title='Compra de Café Brasileiro por País')


# DECLARAÇÃO DO LAYOUT DA PÁGINA WEB COM HTML, CSS E O DCC:
app.layout = html.Div(children=[

    dcc.Dropdown(opcoes, value='Todos os Continentes', id='Filtro_Continentes', style={
        "border-radius": "30px",
        "background-color": "darkgrey"
    }),

    dcc.Dropdown(opcoes2, value='TOTAL', id='Filtro_Tipo', style={
        "border-radius": "30px",
        "background-color": "darkgrey"
    }),

    dcc.Graph(
        id='Grafico_dados',
        figure=fig1
    )

])


# DEFINIÇÃO PARA QUE A MUDANÇA, DEPENDENDO DO QUE ESTIVER SELECIONADO NO DROPDOWN, FUNCIONE (CALLBACK):

# DEFINIÇÃO DE FUNÇÃO PARA QUE SUBSTITUA A FUNÇÃO 'LOC' DO PANDAS:
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

# INÍCIO DO CALLBACK:
@app.callback(
    Output('Grafico_dados', 'figure'),
    Input('Filtro_Tipo', 'value'),
    Input('Filtro_Continentes', 'value')
)
def update_de_dash(tipo, continente):
    dfFl1 = df1.values

    if tipo == 'TOTAL':
        if continente == 'Todos os Continentes':

            fig1 = px.bar(df1, x="CONTINENTE", y="TOTAL", color="PAÍS DESTINO", height=700, title='Compra de Café Brasileiro por País por Continente')

        else:  

            filtro = filtragem(dfFl1, str(continente), None)
            fig1 = px.bar(filtro, x=0, y=6, color=1, height=700, title=f'Compra de Café Brasileiro ({continente})', labels={'0': 'CONTINENTE', '6': 'TOTAL', '1': 'PAÍS DESTINO'})

    else:
        if continente == 'Todos os Continentes':

            fig1 = px.bar(df1, x="CONTINENTE", y=str(tipo), color="PAÍS DESTINO", height=700, title=f'Compra de Café {tipo} Brasileiro por Continente')

        else:

            filtro = filtragem(dfFl1, str(continente), str(tipo))
            fig1 = px.bar(filtro, x=0, y=2, color=1, height=700, title=f'Compra de Café {tipo} Brasileiro ({continente})', labels={'0': 'CONTINENTE', '1': 'PAÍS DESTINO', '2': tipo})

    return fig1


# OUTRA VEZ, PARA MARCAR O FIM DA CONTRUÇÃO DO APP, E PARA DEIXAR O SITE FUNCIONANDO:
if __name__ == '__main__':
    app.run_server(debug=True)