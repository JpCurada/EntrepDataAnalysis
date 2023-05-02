import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

pan_pan_df = pd.read_csv('pan_pan_survey_data.csv', index_col=0)
pan_pan_df.fillna(0)

wafi_san_df = pd.read_csv('wafi_san_survey_data.csv', index_col=0)
wafi_san_df.fillna(0)

colors = ['#bbdefb', '#90caf9', '#64b5f6', '#42a5f5', '#2196f3', '#1e88e5']


def create_bar_chart(dataframe, title, xaxis_title, yaxis_title, colors, index_range):
    fig = go.Figure()

    for i, col in enumerate(dataframe.columns):
        fig.add_trace(go.Bar(
            name=col,
            x=list(dataframe.index[index_range]),
            y=list(dataframe[col][index_range]),
            offsetgroup=col,
            marker=dict(color=colors[i]),
        ))

    fig.update_layout(
        title=title,
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title,
        barmode='stack',
        showlegend=True,
        legend_title='Grade',
        font=dict(size=16),
        width=1000,
        height=500
    )
    
    return fig


fig = create_bar_chart(
    dataframe=pan_pan_df,
    title='How much would you spend for a pancake?',
    xaxis_title='Price Range',
    yaxis_title='Number of Respondents',
    colors=colors,
    index_range=slice(0, 4)
)

fig1 = create_bar_chart(
    dataframe=pan_pan_df,
    title='How many servings of pancakes do you prefer?',
    xaxis_title='Number of Servings',
    yaxis_title='Number of Respondents',
    colors=colors,
    index_range=slice(4, 8)
)

fig2 = create_bar_chart(
    dataframe=pan_pan_df,
    title='What type of packaging do you prefer?',
    xaxis_title='Packaging Type',
    yaxis_title='Number of Respondents',
    colors=colors,
    index_range=slice(8, 10)
)

fig3 = create_bar_chart(
    dataframe=pan_pan_df,
    title='Which drink do you prefer?',
    xaxis_title='Drinks',
    yaxis_title='Number of Respondents',
    colors=colors,
    index_range=slice(10, 12)
)

fig4 = create_bar_chart(
    dataframe=pan_pan_df,
    title='Which fruit toppings do you prefer?',
    xaxis_title='Fruit Toppings',
    yaxis_title='Number of Respondents',
    colors=colors,
    index_range=slice(12, 16)
)

fig5 = create_bar_chart(
    dataframe=pan_pan_df,
    title='What alternative sweetener do you prefer?',
    xaxis_title='Alternative Sweeteners',
    yaxis_title='Number of Respondents',
    colors=colors,
    index_range=slice(16, 19)
)

fig6 = create_bar_chart(
    dataframe=pan_pan_df,
    title='What portion size of the pancake do you prefer?',
    xaxis_title='Portion Size',
    yaxis_title='Number of Respondents',
    colors=colors,
    index_range=slice(19, 21)
)

fig7 = create_bar_chart(
    dataframe=pan_pan_df,
    title='Which will satisfy your convenience',
    xaxis_title='Choices',
    yaxis_title='Number of Respondents',
    colors=colors,
    index_range=slice(21, 23)
)

fig8 = create_bar_chart(
    dataframe=pan_pan_df,
    title='Which delivery of serving do you prefer?',
    xaxis_title='Choices',
    yaxis_title='Number of Respondents',
    colors=colors,
    index_range=slice(23, 25)
)

fig9 = create_bar_chart(
    dataframe=wafi_san_df,
    title='How much would you spend for a waffle sandwich?',
    xaxis_title='Price Range',
    yaxis_title='Number of Respondents',
    colors=colors,
    index_range=slice(0, 3)
)

fig10 = create_bar_chart(
    dataframe=wafi_san_df,
    title='How would you like chicken in your sandwich?',
    xaxis_title='Chicken',
    yaxis_title='Number of Respondents',
    colors=colors,
    index_range=slice(3, 5)
)

fig11 = create_bar_chart(
    dataframe=wafi_san_df,
    title='What type of packaging would you like your sandwich served?',
    xaxis_title='Packaging Type',
    yaxis_title='Number of Respondents',
    colors=colors,
    index_range=slice(5, 7)
)

fig12 = create_bar_chart(
    dataframe=wafi_san_df,
    title='Which type of egg do you prefer?',
    xaxis_title='Eggs',
    yaxis_title='Number of Respondents',
    colors=colors,
    index_range=slice(7, 11)
)

fig13 = create_bar_chart(
    dataframe=wafi_san_df,
    title='Select 2 flavors you prefer for your chicken.',
    xaxis_title='Flavors',
    yaxis_title='Number of Respondents',
    colors=colors,
    index_range=slice(11, 15)
)

fig14 = create_bar_chart(
    dataframe=wafi_san_df,
    title='Would you prefer any other type of savor in your sandwiches?',
    xaxis_title='Savories',
    yaxis_title='Number of Respondents',
    colors=colors,
    index_range=slice(15, 19)
)

fig15 = create_bar_chart(
    dataframe=wafi_san_df,
    title='What type of veggies would you like in your sandwiches?',
    xaxis_title='Veggies',
    yaxis_title='Number of Respondents',
    colors=colors,
    index_range=slice(19, 23)
)

fig16 = create_bar_chart(
    dataframe=wafi_san_df,
    title='What sauce do you prefer?',
    xaxis_title='Sauces',
    yaxis_title='Number of Respondents',
    colors=colors,
    index_range=slice(23, 27)
)

fig17 = create_bar_chart(
    dataframe=wafi_san_df,
    title='Which will satisfy your convenience',
    xaxis_title='Choices',
    yaxis_title='Number of Respondents',
    colors=colors,
    index_range=slice(27, 29)
)

fig18 = create_bar_chart(
    dataframe=wafi_san_df,
    title='How would you like your WAFI-SAN to be served?',
    xaxis_title='Choices',
    yaxis_title='Number of Respondents',
    colors=colors,
    index_range=slice(29, 31)
)