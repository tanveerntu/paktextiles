
from plotly import graph_objs as go
import pandas as pd
import streamlit as st 

########################
#######################
#Setting page configuration and title for SEO
st.set_page_config(
    page_title = 'Pakistan Trade Statistics',
    page_icon = '✅',
    layout = 'wide'
)
#########################
#########################
# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


########################################
########################################
########################################
#data
df = pd.read_csv('paktrade_pbs.csv')

##############
#fig = go.Figure()
# add subplot properties when initializing fig variable
from plotly.subplots import make_subplots

fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                    vertical_spacing=0.01, 
                    row_heights=[0.65,0.35])
###############
# Add traces
fig.add_trace(go.Scatter(
    x=df["year"], 
    y=df["export_US$B"], 
    name="Exports", 
    text=df['export_US$B'],
    texttemplate='%{text:.3s}', # to text shorten into 3 digits, use '%{text:.3s}'
    mode="markers+lines",
    textposition="bottom right",
    textfont=dict(family="fjalla one, sans-serif", color="green", size=20),
    marker=dict(size=12, color="green"),
    line=dict(width=5, color="green")), row=1, col=1)

# Add traces
fig.add_trace(go.Scatter(
    x=df["year"], 
    y=df["import_US$B"], 
    name="Imports", 
    text=df['import_US$B'],
    texttemplate='%{text:.3s}', # to text shorten into 3 digits, use '%{text:.3s}'
    mode="markers+lines",
    textposition="bottom right",
    textfont=dict(family="fjalla one, sans-serif", color="red", size=20),
    marker=dict(size=12, color="red"),
    line=dict(width=5, color="red")), row=1, col=1)

# Plot MACD trace on 3rd row
#val = df['balance_US$B']
#colors = ['green' if val >= 0 
#          else 'red' for val in df['balance_US$B']]


fig.add_trace(go.Bar(x=df['year'], y=df['balance_US$B'],
                    name='Trade Balance', 
                    #text=df['balance_US$B'], #text on bars
                    #textfont_size=24, #text on bars
                    #textfont_family='roboto',
                    #texttemplate='%{text:.3s}', # to text shorten into 3 digits, use '%{text:.3s}'
                    marker_color='red', #bar colors
                    ), row=2, col=1)
###############
from PIL import Image
image = Image.open('logo.png')                    
#st.image(logo.png)
fig.add_layout_image(
    dict(
        source=image,
        xref="paper", yref="paper",
        x=1, y=-0.2,  #image postion on chart
        sizex=0.1, sizey=0.1, #image size on chart
        xanchor="right", yanchor="bottom"
    ))
#layout
fig.update_layout(
    autosize=False, height=650, width=1050,
    #legend_traceorder="reversed",
    margin=dict(t=60, b=120, l=40, r=40),
    plot_bgcolor='#ffffff',
    paper_bgcolor='#ffffff',
    
)
###############
#updates axes
fig.update_xaxes(showline=True, linewidth=8, linecolor='black', row=1, col=1)
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', row=1, col=1)
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1)

fig.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
fig.update_yaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
fig.update_yaxes(side='right', title='US$ Billion', title_font=dict(family='Roboto', color='black', size=20), row=1, col=1)
fig.update_yaxes(side='right', title='Trade Balance', title_font=dict(family='Roboto', color='black', size=20), row=2, col=1)

fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99', row=1, col=1)
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99', row=2, col=1)

###############

#title
fig.add_annotation(
            text="Pakistan Exports and Imports",
            font=dict(family='Fjalla one', color='#006BA2', size=36), 
            xref="x domain", yref="y domain",
            x=0, y=1.18, 
            showarrow=False,
            arrowhead=1)

#subtitle
fig.add_annotation(
            text="1950-51 to 2020-21",
            font=dict(family='roboto', color='black', size=24), 
            xref="x domain", yref="y domain",
            x=0, y=1.06, 
            showarrow=False,
            arrowhead=1)
#data reference
fig.add_annotation(
            text="Source: Pakistan Bureau of Statistics",
            font=dict(family='Fjalla one', color='#758D99', size=20), 
            xref="x domain", yref="y domain",
            x=0, y=-0.9, 
            showarrow=False,
            arrowhead=1)

#Adding only the last date point value/text
fig.add_trace(go.Scatter(x=[df['year'].iloc[-1]],
                         y=[df['export_US$B'].iloc[-1]],
                         text=[df['export_US$B'].iloc[-1]],
                         name='',
                         mode='markers+text',
                         marker=dict(color='green', size=14),
                         textposition='top center',
                         textfont=dict(family="fjalla one, sans-serif", color="green", size=20),
                         texttemplate='$%{text:.3s}B', #text shorten into 3 digits
                         showlegend=False))

#Adding only the last date point value/text
fig.add_trace(go.Scatter(x=[df['year'].iloc[-1]],
                         y=[df['import_US$B'].iloc[-1]],
                         text=[df['import_US$B'].iloc[-1]],
                         name='',
                         mode='markers+text',
                         marker=dict(color='red', size=14),
                         textposition='top center',
                         textfont=dict(family="fjalla one, sans-serif", color="red", size=20),
                         texttemplate='$%{text:.3s}B', #text shorten into 3 digits
                         showlegend=False))

#Adding only the last date point value/text
fig.add_trace(go.Scatter(x=[df['year'].iloc[-1]],
                         y=[df['balance_US$B'].iloc[-1]],
                         text=[df['balance_US$B'].iloc[-1]],
                         name='',
                         mode='markers+text',
                         marker=dict(color='red', size=14),
                         textposition='bottom center',
                         textfont=dict(family="fjalla one, sans-serif", color="red", size=20),
                         texttemplate='$%{text:.3s}B', #text shorten into 3 digits
                         showlegend=False), row=2, col=1)
#legend
fig.update_layout(legend=dict(
    orientation="h",
    font=dict(family='Roboto', color='#758D99', size=16), 
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1))
######################
#show figure in streamlit web app
st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive
#config={'responsive': True}
##############################
##############################

#######################################
########################################
########################################
#data
df1 = pd.read_csv('monthly_trade.csv')
 
#calculating year-to-date YTD bales and adding new column for the same
df1['imports_ytd_21_22'] = df1['imports_21_22B'].cumsum()

df1['imports_ytd_20_21'] = df1['imports_20_21B'].cumsum()

df1['exports_ytd_20_21'] = df1['exports_20_21B'].cumsum()
df1['exports_ytd_21_22'] = df1['exports_21_22B'].cumsum()
df1['balance_ytd_20_21'] = df1['balance_20_21B'].cumsum()
df1['balance_ytd_21_22'] = df1['balance_21_22B'].cumsum()


##############
#fig = go.Figure()
# add subplot properties when initializing fig variable
from plotly.subplots import make_subplots

fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                    vertical_spacing=0.01, 
                    row_heights=[0.65,0.35])
###############
# Add traces
fig.add_trace(go.Scatter(
    x=df1["month"], 
    y=df1["imports_ytd_21_22"], 
    name="Imports 21-22", 
    text=df1['imports_ytd_21_22'],
    texttemplate='%{text:.3s}B', # to text shorten into 3 digits, use '%{text:.3s}'
    mode="markers+lines+text",
    textposition="bottom right",
    textfont=dict(family="fjalla one, sans-serif", color="red", size=20),
    marker=dict(size=12, color="red"),
    line=dict(width=5, color="red")), row=1, col=1)

fig.add_trace(go.Scatter(
    x=df1["month"], 
    y=df1["imports_ytd_20_21"], 
    name="Imports 20-21", 
    text=df1['imports_ytd_20_21'],
    texttemplate='%{text:.3s}B', # to text shorten into 3 digits, use '%{text:.3s}'
    mode="markers+lines+text",
    textposition="bottom right",
    textfont=dict(family="fjalla one, sans-serif", color="brown", size=20),
    marker=dict(size=12, color="brown"),
    line=dict(width=5, color="brown")), row=1, col=1)

fig.add_trace(go.Scatter(
    x=df1["month"], 
    y=df1["exports_ytd_20_21"], 
    name="Exports 20-21", 
    text=df1['exports_ytd_20_21'],
    texttemplate='%{text:.3s}B', # to text shorten into 3 digits, use '%{text:.3s}'
    mode="markers+lines+text",
    textposition="bottom right",
    textfont=dict(family="fjalla one, sans-serif", color="lightgreen", size=20),
    marker=dict(size=12, color="lightgreen"),
    line=dict(width=5, color="lightgreen")), row=1, col=1)

fig.add_trace(go.Scatter(
    x=df1["month"], 
    y=df1["exports_ytd_21_22"], 
    name="Exports 21-22", 
    text=df1['exports_ytd_21_22'],
    texttemplate='%{text:.3s}B', # to text shorten into 3 digits, use '%{text:.3s}'
    mode="markers+lines+text",
    textposition="bottom right",
    textfont=dict(family="fjalla one, sans-serif", color="green", size=20),
    marker=dict(size=12, color="green"),
    line=dict(width=5, color="green")), row=1, col=1)

# Plot MACD trace on 3rd row
#val = df['balance_US$B']
#colors = ['green' if val >= 0 
#          else 'red' for val in df['balance_US$B']]


fig.add_trace(go.Scatter(x=df1['month'], y=df1['balance_ytd_20_21'],
                    name='Trade Balance 20-21', 
                    text=df1['balance_ytd_20_21'],
                    texttemplate='%{text:.3s}B', # to text shorten into 3 digits, use '%{text:.3s}'
                    mode="markers+lines+text",
                    textposition="top right",
                    textfont=dict(family="fjalla one, sans-serif", color="lightblue", size=20),
                    marker=dict(size=12, color="lightblue"),
                    line=dict(width=5, color="lightblue")), row=2, col=1)

fig.add_trace(go.Scatter(x=df1['month'], y=df1['balance_ytd_21_22'],
                    name='Trade Balance 21-22', 
                    text=df1['balance_ytd_21_22'],
                    texttemplate='%{text:.3s}B', # to text shorten into 3 digits, use '%{text:.3s}'
                    mode="markers+lines+text",
                    textposition="top right",
                    textfont=dict(family="fjalla one, sans-serif", color="orange", size=20),
                    marker=dict(size=12, color="orange"),
                    line=dict(width=5, color="orange")), row=2, col=1)
###############
from PIL import Image
image = Image.open('logo.png')                    
#st.image(logo.png)
fig.add_layout_image(
    dict(
        source=image,
        xref="paper", yref="paper",
        x=1, y=-0.2,  #image postion on chart
        sizex=0.1, sizey=0.1, #image size on chart
        xanchor="right", yanchor="bottom"
    ))
#layout
fig.update_layout(
    autosize=False, height=650, width=1050,
    #legend_traceorder="reversed",
    margin=dict(t=80, b=100, l=40, r=40),
    plot_bgcolor='#ffffff',
    paper_bgcolor='#ffffff',
)
###############
#updates axes
fig.update_xaxes(showline=True, linewidth=8, linecolor='black', row=1, col=1)
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', row=1, col=1)
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1)

fig.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
fig.update_yaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
fig.update_yaxes(side='right', title='US$ Billion', title_font=dict(family='Roboto', color='black', size=20), row=1, col=1)
fig.update_yaxes(side='right', title='Trade Balance', title_font=dict(family='Roboto', color='black', size=20), row=2, col=1)

fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99', row=1, col=1)
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99', row=2, col=1)

###############

#title
fig.add_annotation(
            text="Pakistan Exports and Imports",
            font=dict(family='Fjalla one', color='#006BA2', size=36), 
            xref="x domain", yref="y domain",
            x=0, y=1.21, 
            showarrow=False,
            arrowhead=1)

#subtitle
fig.add_annotation(
            text="2020-21 vs. 2021-22 (cumulative figures till recent month)",
            font=dict(family='roboto', color='black', size=24), 
            xref="x domain", yref="y domain",
            x=0, y=1.09, 
            showarrow=False,
            arrowhead=1)
#data reference
fig.add_annotation(
            text="Source: Pakistan Bureau of Statistics",
            font=dict(family='Fjalla one', color='#758D99', size=20), 
            xref="x domain", yref="y domain",
            x=0, y=-0.85, 
            showarrow=False,
            arrowhead=1)


#legend
fig.update_layout(legend=dict(
    orientation="h",
    font=dict(family='Roboto', color='#758D99', size=16), 
    yanchor="bottom",
    y=1.05,
    xanchor="right",
    x=1.07))
######################
#show figure in streamlit web app
st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive
##############################
##############################

