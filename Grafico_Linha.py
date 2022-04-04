import plotly.express as px
from pandas import read_excel
from dash import Dash, dcc, html

df = read_excel('https://github.com/Trabalho-APC-DASH/Painel-APC/blob/main/Banco%20de%20Dados/Consumo_cafe.xlsx?raw=true')
lista3 = df.values

app = Dash(__name__)

df2 = []
for a in lista3:
    df2 += [[a[0], a[1], '2017/18']]
    df2 += [[a[0], a[2], '2018/19']]
    df2 += [[a[0], a[3], '2019/20']]
    df2 += [[a[0], a[4], '2020/21']]



fig = px.line(df2, x=2, y=1, color=0, markers=True, symbol=0 , title='Consumo (Em milhares de sacas de 60kg)' ,labels={
    '0': 'Países',
    '1': 'Consumo',
    '2': 'Ano'
})

app.layout = html.Div(children=[

    dcc.Graph(
        id='Grafico_dados',
        figure=fig
    )

])


if __name__ == '__main__':
    app.run_server(debug=True)
