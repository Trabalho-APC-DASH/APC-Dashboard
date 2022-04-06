
# Novo Gráfico em Linhas - VERSÃO FINAL V1.0
# Editado em 05/04 - 11:13


import plotly.express as px
from pandas import read_excel
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go


app = Dash(__name__) 


df3 = read_excel('https://github.com/Trabalho-APC-DASH/Painel-APC/blob/main/Banco%20de%20Dados/Preco_Medio.xlsx?raw=true')

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


app.layout = html.Div(children=[

    dcc.Dropdown(opcoes3, value='Todos os Tipos de Café', id='filtro3'),

    dcc.Graph(
        id='Grafico_dados3',
        figure=fig3
    ),

])

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