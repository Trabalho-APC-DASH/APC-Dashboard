# VERSÃO FINAL V1.0 EM BARRAS
# ALTERADO EM 03/04 - 00:31

import plotly.express as px
from pandas import read_excel
from dash import Dash, dcc, html



app = Dash(__name__)

df2 = read_excel('https://github.com/Trabalho-APC-DASH/Painel-APC/blob/main/Banco%20de%20Dados/UnidadesReceita.xlsx?raw=true')

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

# INSERÇÃO DE LAYOUT NA PÁGINA:
app.layout = html.Div(children=[

    dcc.Graph(
        id='Grafico_dados',
        figure=fig2
    )

])

# SINTAXE FINAL
if __name__ == '__main__':
    app.run_server(debug=True)