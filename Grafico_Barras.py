# VERSÃO V3.0 Final em Barras
# EDITADO EM 22/03 ÀS 20:02

import plotly.express as px # Importação do Plotly para criar o design dos gráficos
from pandas import read_excel # Importação da função read_excel, para ler excel, da biblioteca Pandas
from dash import Dash, dcc, html, Input, Output
'''
A importação da biblioteca Dash fara a função da construção do layout do site em que os gráficos serão inseridos, dentre
as funções declaradas, temos:

@ Dash: Está servindo somente para colocar o site em funcionamento;

@ dcc: Função responsável por inserir o gráfico na página Web;

@ html: Função responsável por permitir organizar e criar um layout com nossa cara para o site, contudo ele não personaliza
o gráfico, somente a página web:

@ Input: Será utilizado mais a frente para que, dependendo de um gatilho disparada pelo usuário, algo será modificado na
página, neste caso, o input será a caixa de seleção (dropdown). O input será a origem do gatilho.

@ Output: Será utilizado mais a frente, este é o destinatário do gatilho efetuado pelo usuário, ou seja, a função que define
quem será alterado, neste caso o gráfico.
'''

app = Dash(__name__) # Isso aqui tem a função de colocar o site pra funcionar

# DECLARAÇÃO DO BANCO DE DADOS A SER UTILIZADO:
df = read_excel("https://github.com/Trabalho-APC-DASH/Painel-APC/blob/main/Banco%20de%20Dados/Brasil-Exportacao_cafe_por_pais.xlsx?raw=true")

# ORGANIZAÇÃO DAS OPÇÕES PARA O DROPDOWN:
opcoes = list(df["CONTINENTE"].unique())
opcoes.insert(0, 'Todos os Continentes')
del opcoes[6]

opcoes2 = ['ARÁBICA (Por sacas de 60kg)', 'CONILLON (Por sacas de 60kg)', 'SOLÚVEL (Por sacas de 60kg)', 'TORRADO (Por sacas de 60kg)', 'TOTAL']

'''
Nesta etapa, esta sendo efetuada as seguintes questões:

@ Primeiro é declarada a variável OPCOES, que fará uma lista (através da função 'list') das opções presentes na coluna
CONTINENTE do dataframe "df" (variável declarada para armazenar a leitura realizada pelo pandas na linha 25). A função
'unique()' logo adiante, tem como objetivo organizar esta lista sem repetir as opções que já foram escritas nela;

@ Na linha seguinte (Linha 29), é feito uma inserção na posição 0 dessa lista, cujo receberá uma string
'Todos os Continentes';

@ Na última linha das OPCOES, mandei deletar a informação da 6º posição, pois NO ARQUIVO do excel (banco de dados), a última linha é
nula, ou seja, não possui nada escrita nela e, por isso, estava sendo armazenada na lista um valor 'null' para representa-la.
Como ela não será útil, apaguei.

@ Na segunda variável OPCOES2, foi feita uma listas das colunas por tipo de café, IGUAL AO ARQUIVO EXCEL, que o usuário poderá escolher em um
dropdown logo adiante.
'''

# DECLARAÇÃO DE COMO O GRÁFICO IRÁ SER ORGANIZADO:
fig = px.bar(df, x="CONTINENTE", y="TOTAL", color="PAÍS DESTINO", height=700, title='Compra de Café Brasileiro por País')


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
        figure=fig
    )

])

'''
Nesta etapa temos:

@ Declaração do app.layout que indica o início na organização visual do site;

@ O html.div serve como uma divisão no HTML, para separar grupos de imagens, textos ou até mesmo uma mistura de ambas.
Basicamente é um bloco de informação dentro dela.

@ Quando criamos um bloco em que dentro dela terá mais informações, chamamos a origem de pai e as informações dispostas
em seu interior, ou originadas a partir desse bloco, de filhas ('Children'). A função div aqui no python precisa desse
parâmetro para que seja descritas as informações que ficarão dentro dela;


@ O dcc.Dropdown está criando, na página web, a tal caixa de seleção PARA OS CONTINENTES. Entre parênteses temos:

- Definição das opções que serão mostradas na caixa de seleção, neste caso, será a lista criada na linha 28 'OPCOES';

- O valor (value) inicial que a caixa de seleção estará selecionada.

- Um id para nomear essa função que, porém, será utilizadas para chamar ela mais tarde.

- O Style recebe um '={}', pois são propriedades de outra "Linguagem", por assim dizer, que é o CSS, responsável por
pequenas e grandes modificações na contrução web. Em resumo:

HTML: Funciona como ESQUELETO do site, ele define onde ficará o botão, a caixa de texto, a barra de navegação, a imagem,
o rodapé, e por aí vai.

CSS: Funciona como a MAQUIAGEM do site, ele define como será o botão, a fonte e cor da caixa de texto, o estilo da barra
de navegação, o tamanho e posição da imagem, etc.

- Sendo assim, estamos alterando 2 características do Dropdown em CSS: O Raio da borda (Border-Radius) para que as 
quinas da caixa de seleção fique redonda, e a Cor de Fundo do Dropdown (Background-Color) para Darkgrey;

@ Logo após o primeiro Dropdown, temos a inserção de um segundo Dropdown, que será o seletor para os tipos de cafés;

@ Logo após criarmos os Dropdown's e dar características à ela, temos o dcc.Graph, que só coloca a figura do gráfico que
fizemos na linha 48 no site.
'''

# DEFINIÇÃO PARA QUE A MUDANÇA, DEPENDENDO DO QUE ESTIVER SELECIONADO NO DROPDOWN, FUNCIONE:
@app.callback(
    Output('Grafico_dados', 'figure'),
    Input('Filtro_Tipo', 'value'),
    Input('Filtro_Continentes', 'value')
)
def update_de_dash(tipo, continente):
    
    if tipo == 'TOTAL':
        if continente == 'Todos os Continentes':

            fig = px.bar(df, x="CONTINENTE", y="TOTAL", color="PAÍS DESTINO", height=700, title='Compra de Café Brasileiro por País por Continente')

        else:

            filtro = df.loc[df['CONTINENTE']==continente, :]
            fig = px.bar(filtro, x="CONTINENTE", y="TOTAL", color="PAÍS DESTINO", height=700, title=f'Compra de Café Brasileiro ({continente})')

    else:
        if continente == 'Todos os Continentes':

            fig = px.bar(df, x="CONTINENTE", y=str(tipo), color="PAÍS DESTINO", height=700, title=f'Compra de Café {tipo} Brasileiro por Continente')

        else:

            filtro = df.loc[df['CONTINENTE']==continente, :]
            fig = px.bar(filtro, x="CONTINENTE", y=str(tipo), color="PAÍS DESTINO", height=700, title=f'Compra de Café {tipo} Brasileiro ({continente})')

    return fig

'''
CALLBACK:

@ Para que as alterações funcionem, utilizaremos um callback para nos dar assistência às variáveis que serão enviadas para a nossa função.
Dentro do callback, temos 3 parâmetros, sendo 2 iguais. São eles:

- INPUT: Que determinará o gatilho que necessário para algo mudar.

- OUTPUT: Quem será alterado.


@ Sob essa definição, temos um OUTPUT a ser alterado. Entre parênteses, inserimos:

- O nome (id) do objeto a ser alterado. Neste caso será o 'Grafico_dados', que é o dcc responsável em mostrar o gráfico fig ma página web.

- O fator específico do objeto escolhido como OUTPUT a ser alterado, neste caso será a variável figure, que armazena as informações da
estrutura do gráfico (linha 74).

@ Temos, após o OUTPUT, 2 INPUTS, que serão responsáveis em definir qual o continente e o tipo de café o usuário irá querer observar.
Entre parenteses, seguimos a mesma regra dos argumentos do OUTPUT.


FUNÇÃO:

@ Criamos o prefixo def para iniciar a função, com o nome de 'update_de_dash'. Para que consigamos trabalhar bem com as
alterações nos gráficos, iremos receber 2 argumentos graças aos dois INPUTS declaradas no callback. Na ordem temos o INPUT
do tipo de café, e o segundo INPUT cuidará de receber o continente que o usuário irá buscar.

@ Tendo em mãos esses dois argumentos (def update_de_dash(TIPO, CONTINENTE), na linha 124) podemos trabalhar a filtragem
o retorno delas na variável fig, que será mostrada na página web.


@ Temos 2 situações para o Tipo de café selecionado:

- Todos os tipos de cafés;

- Tipo de café específico.

@ Temos também 2 situações para os continentes selecionados:

- Todos os continentes;

- Continente específico.


@ Por isso, temos que separá-los em if's, que dará o resultado final do gráfico dependendo da combinação destas seleções:

- PRIMEIRO IF: 
    Para caso de TODOS OS TIPOS DE CAFÉ

    - PRIMEIRO SUB-IF:
        Para caso de TODOS OS TIPOS DE CAFÉ & TODOS OS CONTINENTES

    - SEGUNDO SUB-IF:
        Para caso de TODOS OS TIPOS DE CAFÉ & CONTINENTE ESPECÍFICO


- SEGUNDO IF:
    Para caso de TIPO DE CAFÉ ESPECÍFICO

    - PRIMEIRO SUB-IF:
        Para caso de TIPO DE CAFÉ ESPECÍFICO & TODOS OS CONTINENTES

    - SEGUNDO SUB-IF:
        Para caso de TIPO DE CAFÉ ESPECÍFICO & CONTINENTE ESPECÍFICO

    
    Retorno do gráfico dependendo da combinação escolhida.
'''

# OUTRA VEZ, PARA MARCAR O FIM DA CONTRUÇÃO DO APP, E PARA DEIXAR O SITE FUNCIONANDO:
if __name__ == '__main__':
    app.run_server(debug=True)