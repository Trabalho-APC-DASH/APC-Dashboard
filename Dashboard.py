import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html, Input, Output
from plotly.subplots import make_subplots

df = pd.read_excel("Painel-APC\Agricultura-valor-da-produo-brasil.xlsx")
df2 = pd.read_excel("Painel-APC\Brasil-Exportacao_cafe_por_pais.xlsx")

fig = make_subplots(
    rows=2, cols=1,
    row_heights=[1.6, 1.6],
    specs=[
        [{"type": "bar"}],
        [{"type": "pie"}]
    ]
)



fig.show()