
# Novo Gráfico em Linhas - VERSÃO FINAL V1.0
# Editado em 05/04 - 11:13


import plotly.express as px
from pandas import read_excel
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go


app = Dash(__name__) 


df = read_excel('https://github.com/Trabalho-APC-DASH/Painel-APC/blob/main/Banco%20de%20Dados/Preco_Medio.xlsx?raw=true')
lista1 = df.values

opcoes = []
for n in df:
    opcoes += [n]

opcoes.insert(0, 'Todos os Tipos de Café')
del opcoes[1]
del opcoes[7]


fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Mês/Ano'], y=df['Conillon'],
                    mode='lines',
                    name='Conillon'))
fig.add_trace(go.Scatter(x=df['Mês/Ano'], y=df['Arábica'],
                    mode='lines',
                    name='Arábica'))
fig.add_trace(go.Scatter(x=df['Mês/Ano'], y=df['Total Café Verde'],
                    mode='lines', name='Total (Café Verde)'))

fig.add_trace(go.Scatter(x=df['Mês/Ano'], y=df['Torrado'],
                    mode='lines', name='Torrado'))
fig.add_trace(go.Scatter(x=df['Mês/Ano'], y=df['Solúvel'],
                    mode='lines', name='Solúvel'))
fig.add_trace(go.Scatter(x=df['Mês/Ano'], y=df['Total Industrializado'],
                    mode='lines', name='Total (Industrializado)'))

fig.update_layout(title='Preço Médio do Café',
                   xaxis_title='Ano',
                   yaxis_title='Preço (R$)')


app.layout = html.Div(children=[

    dcc.Dropdown(opcoes, value='Todos os Tipos de Café', id='filtro3'),

    dcc.Graph(
        id='Grafico_dados',
        figure=fig
    ),

])

@app.callback(
    Output('Grafico_dados', 'figure'),
    Input('filtro3', 'value')
)
def UpdateDeDash1(value):
    if value == 'Todos os Tipos de Café':

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['Mês/Ano'], y=df['Conillon'],
                            mode='lines',
                            name='Conillon'))
        fig.add_trace(go.Scatter(x=df['Mês/Ano'], y=df['Arábica'],
                            mode='lines',
                            name='Arábica'))
        fig.add_trace(go.Scatter(x=df['Mês/Ano'], y=df['Total Café Verde'],
                            mode='lines', name='Total (Café Verde)'))

        fig.add_trace(go.Scatter(x=df['Mês/Ano'], y=df['Torrado'],
                            mode='lines', name='Torrado'))
        fig.add_trace(go.Scatter(x=df['Mês/Ano'], y=df['Solúvel'],
                            mode='lines', name='Solúvel'))
        fig.add_trace(go.Scatter(x=df['Mês/Ano'], y=df['Total Industrializado'],
                            mode='lines', name='Total (Industrializado)'))

        fig.update_layout(title='Preço Médio do Café',
                        xaxis_title='Ano',
                        yaxis_title='Preço Médio (R$)')

    else:

        fig = px.line(df, x='Mês/Ano', y=str(value), title=f'Preço Médio ({value})', labels={ str(value) : f'Preço Médio (R$) - {value}'})

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)