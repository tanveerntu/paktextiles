import streamlit as st
import pandas as pd
from plotly import graph_objs as go
from plotly.subplots import make_subplots
import plotly.express as px 
from PIL import Image

# Use the full page instead of a narrow central column
st.set_page_config(
    page_title = 'Pakistan Textile Exports',
    page_icon = '✅',
    layout = 'wide'
)
# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
#from pages import garments, knitwear, textile  # import your app modules here

st.sidebar.header('Pakistan Textile Exports')

page_names = ['Total Textile Exports', #index =0
            'Raw Cotton Exports', #index=1
            #'Carded/Combed Cotton Exports', 
            'Cotton Yarn Exports',
            #'Non-Cotton Yarn Exports',
            'Cotton Cloth Exports',
            'Knitwear Exports',
            'Bedwear Exports',
            'Readymade Garments Exports',
            'Towel Exports',
            'Overall Pakistan Trade',
            'Cotton Statistics',
            #'Tents & Tarpaulines Exports',
            #'Artifical Silk & Synthetics Exports',
            #'Made-ups excluding Bedwear & Towels',
            #'Other Textiles Exports'
            ]


page = st.sidebar.radio('Navigation', page_names, index=0)
#st.write("**The variable 'page' returns:**", page)

########################################
########################################

if page == 'Cotton Statistics':

    #importing csv file as dataframe
    df = pd.read_csv('cotton_districts.csv')


    #shorten name of a district for better display on chart
    #df['District'] = df['District'].replace('Shaheed Benazirabad', 'Benazirabad')
    ########################################
    ########################################
    #yearly trend chart
    ########################################

    #creating new colum 'Bales_sum' of yearly sum of bales
    df_yearly = df.groupby(['Year']).agg(Bales_sum=('Bales', 'sum')).reset_index()

    ##############################

    ##############################
    fig_cd = go.Figure()
    # Add traces
    fig_cd.add_trace(go.Bar(x=df_yearly['Year'], y=df_yearly['Bales_sum'],
                        name='Cotton Bales', 
                        text=df_yearly['Bales_sum'], #text on bars
                        textfont_size=24, #text on bars
                        textfont_family='roboto',
                        textposition='auto',
                        texttemplate='%{text:.3s}', # to text shorten into 3 digits, use '%{text:.3s}'
                        marker_color='#006BA2', #bar colors
                        hovertemplate='%{x} <br>Cotton Bales: %{y}'
                        ))
    from PIL import Image
    image = Image.open('logo.png')                    
    #st.image(logo.png)
    fig_cd.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=1,  #image postion on chart
            sizex=0.15, sizey=0.15, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    fig_cd.update_layout(
        autosize=False, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=40, l=40, r=40),
        #title="Cotton Production in Pakistan",
        #title_font=dict(size=30, color='#111111', family="fjalla one, sans-serif"),
        xaxis_title='', yaxis_title="No. of Bales",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
    )


    fig_cd.update_xaxes(showline=True, linewidth=2, linecolor='black')
    fig_cd.update_yaxes(showline=True, linewidth=2, linecolor='black')

    fig_cd.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig_cd.update_yaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig_cd.update_yaxes(title_font=dict(family='Roboto', color='black', size=24))

    #fig_cd.update_xaxes(font=dict(color='#111111', size=24, family="roboto, sans-serif"))

    fig_cd.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')

    #title
    fig_cd.add_annotation(
                text="Cotton Production",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="x domain", yref="y domain",
                x=0, y=1.15, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig_cd.add_annotation(
                text="in Pakistan over the last few years of the closing season",
                font=dict(family='roboto', color='black', size=24), 
                xref="x domain", yref="y domain",
                x=0, y=1.08, 
                showarrow=False,
                arrowhead=1)
    #datasource
    fig_cd.add_annotation(
                text="Source: Pakistan Cotton Ginners Association/National Textile University, Pakistan",
                font=dict(family='Roboto', color='#758D99', size=20), 
                xref="x domain", yref="y domain",
                x=0, y=-0.13, 
                showarrow=False,
                arrowhead=1)


    st.plotly_chart(fig_cd, use_container_width=True) # to show Figure; container width true makes fig. size responsive

    ###
    #######################################
    ###############################
    #cotton exports and imports
    ##############################
    df_e = pd.read_csv('yearly_cotton_imports_pbs.csv')


    ##############################

    ##############################
    fig = go.Figure()
    # Add traces

    fig.add_trace(go.Bar( 
                x=df_e["year"], 
                y=df_e["imp_bales"],
                text=df_e["imp_bales"],
                marker_color='#ff6b6c',
                name='Imports' #name on legend
                ))

    fig.add_trace(go.Bar( 
                x=df_e["year"], 
                y=df_e["exp_bales"],
                text=df_e["exp_bales"],
                marker_color='#3ebcd2',
                name='Exports'
                ))

    fig.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=1,  #image postion on chart
            sizex=0.15, sizey=0.15, #image size on chart
            xanchor="right", yanchor="bottom"
        ))
    fig.update_traces(texttemplate='%{text:.2s}', textposition='auto', textfont_size=24, textfont_family='roboto', textfont_color="#111111")

    fig.update_layout(
        autosize=False, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=40, l=40, r=40),
        xaxis_title='', yaxis_title="No. of Bales",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
    )

    fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black')

    fig.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig.update_yaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig.update_yaxes(title_font=dict(family='Roboto', color='black', size=24))

    #fig_cd.update_xaxes(font=dict(color='#111111', size=24, family="roboto, sans-serif"))

    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')

    #title
    fig.add_annotation(
                text="Cotton Exports & Imports",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="x domain", yref="y domain",
                x=0, y=1.15, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig.add_annotation(
                text="in Pakistan over the last few years of the closing season",
                font=dict(family='roboto', color='black', size=24), 
                xref="x domain", yref="y domain",
                x=0, y=1.08, 
                showarrow=False,
                arrowhead=1)
    #datasource
    fig.add_annotation(
                text="Source: Pakistan Bureau of Statistics/National Textile University, Pakistan",
                font=dict(family='Roboto', color='#758D99', size=20), 
                xref="x domain", yref="y domain",
                x=0, y=-0.13, 
                showarrow=False,
                arrowhead=1)

    fig.update_layout(legend=dict(
        orientation="h",
        font=dict(family='Roboto', color='#758D99', size=16), 
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=0.8))
    st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive

    ###############################
    ################################
    #monthly cotton imports
    #importing csv file as dataframe
    df_m = pd.read_csv('monthly_cotton_imports_pbs.csv')
    #calculating year-to-date YTD bales and adding new column for the same
    df_m['bales_ytd'] = df_m['bales'].cumsum()
    df_m['usd_ytd'] = df_m['USD'].cumsum()


    ##############
    fig = go.Figure()
    ###############
    # Add traces
    fig.add_trace(go.Bar(x=df_m['month'], y=df_m['bales_ytd'],
                        name='Cotton Bales', 
                        text=df_m['bales_ytd'], #text on bars
                        textfont_size=24, #text on bars
                        textfont_family='roboto',
                        textposition='auto',
                        texttemplate='%{text:.3s}', # to text shorten into 3 digits, use '%{text:.3s}'
                        marker_color='#006BA2', #bar colors
                        ))

    fig.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=1,  #image postion on chart
            sizex=0.15, sizey=0.15, #image size on chart
            xanchor="right", yanchor="bottom"
        ))
    ###############
    #layout
    fig.update_layout(
        autosize=False, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=90, l=90, r=40),
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
    )
    ###############
    #updates axes
    fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black')
    fig.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig.update_yaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig.update_yaxes(title='Cumulative No. of Bales', title_font=dict(family='Roboto', color='black', size=24))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    ###############
    #title
    fig.add_annotation(
                text="Cotton Imports",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="x domain", yref="y domain",
                x=0, y=1.18, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig.add_annotation(
                text="in Pakistan in the current financial year 2021-22",
                font=dict(family='roboto', color='black', size=24), 
                xref="x domain", yref="y domain",
                x=0, y=1.10, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig.add_annotation(
                text="Source: Pakistan Bureau of Statistics/National Textile University, Pakistan",
                font=dict(family='Roboto', color='#758D99', size=20), 
                xref="x domain", yref="y domain",
                x=0, y=-0.18, 
                showarrow=False,
                arrowhead=1)
    ######################
    #show figure in streamlit web app
    st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive
    ##############################
    ##############################
    ##############
    fig = go.Figure()
    ###############
    # Add traces

    fig.add_trace(go.Bar(x=df_m['month'], y=df_m['usd_ytd'],
                        name='Cotton Bales', 
                        text=df_m['usd_ytd'], #text on bars
                        textfont_size=24, #text on bars
                        textfont_family='roboto',
                        textposition='auto',
                        texttemplate='%{text:.3s}', # to text shorten into 3 digits, use '%{text:.3s}'
                        marker_color='#ff6b6c', #bar colors
                        ))

    fig.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=1,  #image postion on chart
            sizex=0.15, sizey=0.15, #image size on chart
            xanchor="right", yanchor="bottom"
        ))
    ###############
    #layout
    fig.update_layout(
        autosize=False, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=90, l=90, r=40),
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
    )
    ###############
    #updates axes
    fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black')
    fig.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig.update_yaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig.update_yaxes(title='Cumulative US$', title_font=dict(family='Roboto', color='black', size=24))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    ###############
    #title
    fig.add_annotation(
                text="Cost of Cotton Imports",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="x domain", yref="y domain",
                x=0, y=1.18, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig.add_annotation(
                text="Cumulative price paid for cotton imports till recent month)",
                font=dict(family='roboto', color='black', size=24), 
                xref="x domain", yref="y domain",
                x=0, y=1.10, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig.add_annotation(
                text="Source: Pakistan Bureau of Statistics/National Textile University, Pakistan",
                font=dict(family='Roboto', color='#758D99', size=20), 
                xref="x domain", yref="y domain",
                x=0, y=-0.18, 
                showarrow=False,
                arrowhead=1)
    ######################
    #show figure in streamlit web app
    st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive
    ##############################
    ##############################

    ##############################
    #grouping by province

    ###############################

    df_punjab = df[df['Province'] == 'Punjab']
    df_punjab = df_punjab.groupby(['Year']).agg({'Bales':'sum'}).reset_index()

    df_sindh = df[df['Province'] == 'Sindh']
    df_sindh = df_sindh.groupby(['Year']).agg({'Bales':'sum'}).reset_index()

    df_baluchistan = df[df['Province'] == 'Baluchistan']
    df_baluchistan = df_baluchistan.groupby(['Year']).agg({'Bales':'sum'}).reset_index()


    fig = go.Figure()


    fig.add_trace(go.Bar( 
                x=df_punjab["Year"], 
                y=df_punjab["Bales"],
                text=df_punjab["Bales"],
                marker_color='#ff6b6c',
                name='Punjab' #name on legend
                ))

    fig.add_trace(go.Bar( 
                x=df_sindh["Year"], 
                y=df_sindh["Bales"],
                text=df_sindh["Bales"],
                marker_color='#3ebcd2',
                name='Sindh'
                ))

    fig.add_trace(go.Bar( 
                x=df_baluchistan["Year"], 
                y=df_baluchistan["Bales"],
                text=df_baluchistan["Bales"],
                marker_color='#006BA2',
                name='Baluchistan'
                ))

    fig.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=1,  #image postion on chart
            sizex=0.15, sizey=0.15, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    fig.update_traces(texttemplate='%{text:.2s}', textposition='auto', textfont_size=24, textfont_family='roboto', textfont_color="#111111")

    fig.update_layout(
        autosize=True, height=650, width=1050,
        margin=dict(t=100, b=120, l=40, r=40),
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        bargap=0.2,                             #value can be An int or float in the interval [0, 1]
    )

    fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black')

    fig.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig.update_yaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig.update_yaxes(title_font=dict(family='Roboto', color='black', size=24))

    #fig_cd.update_xaxes(font=dict(color='#111111', size=24, family="roboto, sans-serif"))

    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    fig.update_yaxes(title="No. of Bales",
        title_font=dict(size=25, color='#111111', family="roboto"),
        )


    #title
    fig.add_annotation(
                text="Cotton Production",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="x domain", yref="y domain",
                x=0, y=1.19, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig.add_annotation(
                text=f"in different Pakistani provinces over the last few years",
                font=dict(family='roboto', color='black', size=24), 
                xref="x domain", yref="y domain",
                x=0, y=1.11, 
                showarrow=False,
                arrowhead=1)

    fig.add_annotation(
                text="Source: Pakistan Cotton Ginners Association/National Textile University, Pakistan",
                font=dict(family='Roboto', color='#758D99', size=20), 
                xref="x domain", yref="y domain",
                x=0, y=-0.24, 
                showarrow=False,
                arrowhead=1)
    fig.update_layout(legend=dict(
        orientation="h",
        font=dict(family='Roboto', color='#758D99', size=16), 
        yanchor="bottom",
        y=1.08,
        xanchor="right",
        x=0.8))
    st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive


    ############################
    ############################
    # district-wise chart
    ###########################
    #year = df["Year"]
    #latest_year = year.max()
    #filter data for latest_year

    df_latest_year = df[df['Period'] == '2021-22']



    fig = go.Figure()
    # Add traces
    fig.add_trace(go.Bar(x=df_latest_year['District'], y=df_latest_year['Bales'],
                        name='Cotton Bales', 
                        text=df_latest_year['Bales'], #text on bars
                        textfont_size=24, #text on bars
                        textfont_family='roboto',
                        texttemplate='%{text:.3s}', # to text shorten into 3 digits, use '%{text:.3s}'
                        marker_color='#006BA2', #bar colors
                        
                        ))

    fig.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=1,  #image postion on chart
            sizex=0.15, sizey=0.15, #image size on chart
            xanchor="right", yanchor="bottom"
        ))
    fig.update_layout(
        autosize=False, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=40, l=40, r=40),
        #title="Cotton Production in Pakistan",
        #title_font=dict(size=30, color='#111111', family="fjalla one, sans-serif"),
        xaxis_title='', yaxis_title="No. of Bales",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
    )

    fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black')

    fig.update_xaxes(tickangle=90, tickfont=dict(family='Roboto', color='black', size=24))
    fig.update_yaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig.update_yaxes(title_font=dict(family='Roboto', color='black', size=24))

    #fig_cd.update_xaxes(font=dict(color='#111111', size=24, family="roboto, sans-serif"))

    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    fig.update_xaxes({'categoryorder':'total descending'})


    #title
    fig.add_annotation(
                text="Cotton Production",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="x domain", yref="y domain",
                x=0, y=1.22, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig.add_annotation(
                text=f"in different Pakistani districts during 2020-21 season",
                font=dict(family='roboto', color='black', size=24), 
                xref="x domain", yref="y domain",
                x=0, y=1.11, 
                showarrow=False,
                arrowhead=1)

    fig.add_annotation(
                text="Source: Pakistan Cotton Ginners Association/National Textile University, Pakistan",
                font=dict(family='Roboto', color='#758D99', size=20), 
                xref="x domain", yref="y domain",
                x=0, y=-0.75, 
                showarrow=False,
                arrowhead=1)


    st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive


    ########################
    ########################
    # montlhy cotton arrivals chart
    ###########################
    #################
    df_cotton_arrivals = pd.read_csv('cotton_arrivals.csv')

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_cotton_arrivals["Date"], 
        y=df_cotton_arrivals["2018-19"], 
        name="2018-19", 
        text=df_cotton_arrivals['2018-19'],
        texttemplate='%{text:.3s}', #text shorten into 3 digits
        mode="markers+lines",
        textposition="bottom right",
        textfont=dict(family="roboto, sans-serif", size=18, color="#eca220"),
        marker=dict(size=8, color="#eca220"),
        line=dict(width=2, color="#eca220"),
    ))

    fig.add_trace(go.Scatter(
        x=df_cotton_arrivals["Date"], 
        y=df_cotton_arrivals["2019-20"], 
        name="2019-20", 
        text=df_cotton_arrivals['2019-20'],
        texttemplate='%{text:.3s}', #text shorten into 3 digits
        mode="markers+lines",
        textposition="bottom right",
        textfont=dict(family="roboto, sans-serif", size=18, color="#b4bb3b"),
        marker=dict(size=8, color="#b4bb3b"),
        line=dict(width=2, color="#b4bb3b"),
    ))

    fig.add_trace(go.Scatter(
        x=df_cotton_arrivals["Date"], 
        y=df_cotton_arrivals["2020-21"], 
        name="2020-21", 
        text=df_cotton_arrivals['2020-21'],
        texttemplate='%{text:.3s}', #text shorten into 3 digits
        mode="markers+lines",
        textposition="bottom right",
        textfont=dict(family="roboto, sans-serif", color="#963c4c", size=18),
        marker=dict(size=8, color="#963c4c"),
        line=dict(width=2, color="#963c4c"),
    ))

    fig.add_trace(go.Scatter(
        x=df_cotton_arrivals["Date"], 
        y=df_cotton_arrivals["2021-22"], 
        name="2021-22", 
        text=df_cotton_arrivals['2021-22'],
        texttemplate='%{text:.3s}', # to text shorten into 3 digits, use '%{text:.3s}'
        mode="markers+lines+text",
        textposition="bottom right",
        textfont=dict(family="fjalla one, sans-serif", color="#106ea0", size=20),
        marker=dict(size=12, color="#106ea0"),
        line=dict(width=5, color="#106ea0")
    ))

    fig.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=1,  #image postion on chart
            sizex=0.15, sizey=0.15, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    fig.update_layout(
        autosize=True, height=650, width=1050,
        margin=dict(t=90, b=120, l=40, r=40),
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        bargap=0.2,                             #value can be An int or float in the interval [0, 1]
    )

    fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black')

    fig.update_xaxes(tickangle=90, tickfont=dict(family='Roboto', color='black', size=24))
    fig.update_yaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig.update_yaxes(title_font=dict(family='Roboto', color='black', size=24))

    #fig_cd.update_xaxes(font=dict(color='#111111', size=24, family="roboto, sans-serif"))

    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    fig.update_yaxes(title="Cumulative number of bales",
        title_font=dict(size=25, color='#111111', family="roboto"),
        )


    #title
    fig.add_annotation(
                text="Monthly Cotton Arrival",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="x domain", yref="y domain",
                x=0, y=1.19, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig.add_annotation(
                text=f"in Pakistani factories",
                font=dict(family='roboto', color='black', size=24), 
                xref="x domain", yref="y domain",
                x=0, y=1.11, 
                showarrow=False,
                arrowhead=1)

    fig.add_annotation(
                text="Source: Pakistan Cotton Ginners Association/National Textile University, Pakistan",
                font=dict(family='Roboto', color='#758D99', size=20), 
                xref="x domain", yref="y domain",
                x=0, y=-0.24, 
                showarrow=False,
                arrowhead=1)
    fig.update_layout(legend=dict(
        orientation="h",
        font=dict(family='Roboto', color='#758D99', size=16), 
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=0.75))
    st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive

    ###############################
    ##############################
    #Historical cotton data
    #########################

    ##############################
    df_h = pd.read_csv('cotton_historical.csv')

    fig = go.Figure()
    # Add traces


    fig.add_trace(go.Scatter(
        x=df_h["Year"], 
        y=df_h["Bales"], 
        name="", 
        #text=df_cotton_arrivals['2021-22'],
        #texttemplate='%{text:.3s}', # to text shorten into 3 digits, use '%{text:.3s}'
        mode="markers+lines",
        #textposition="bottom right",
        #textfont=dict(family="fjalla one, sans-serif", color="#106ea0", size=20),
        marker=dict(size=12, color="#106ea0"),
        line=dict(width=5, color="#106ea0"),
        showlegend=False
    ))

    fig.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=1,  #image postion on chart
            sizex=0.15, sizey=0.15, #image size on chart
            xanchor="right", yanchor="bottom"
        ))
    fig.update_layout(
        autosize=False, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=40, l=40, r=40),
        #title="Cotton Production in Pakistan",
        #title_font=dict(size=30, color='#111111', family="fjalla one, sans-serif"),
        xaxis_title='', yaxis_title="No. of Bales",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
    )

    fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black')

    fig.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig.update_yaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig.update_yaxes(title_font=dict(family='Roboto', color='black', size=24))

    #fig_cd.update_xaxes(font=dict(color='#111111', size=24, family="roboto, sans-serif"))

    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    #adding range buttons

    fig.update_xaxes(
    rangeslider_visible = False, 
        rangeselector = dict(
        buttons = list([
        dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
        dict(count = 2, label = '2Y', step = 'year', stepmode = 'backward'),
        dict(count = 5, label = '5Y', step = 'year', stepmode = 'backward'),
        #dict(step = 'all')
        ])))



    #title
    fig.add_annotation(
                text="Cotton Production in Pakistan",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="x domain", yref="y domain",
                x=0, y=1.15, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig.add_annotation(
                text="since 1947-48 season",
                font=dict(family='roboto', color='black', size=24), 
                xref="x domain", yref="y domain",
                x=0, y=1.08, 
                showarrow=False,
                arrowhead=1)
    #datasource
    fig.add_annotation(
                text="Source: Pakistan Cotton Ginners Association/Karachi Cotton Association/National Textile University, Pakistan",
                font=dict(family='Roboto', color='#758D99', size=20), 
                xref="x domain", yref="y domain",
                x=0, y=-0.13, 
                showarrow=False,
                arrowhead=1)
    #Adding only the last date point value/text
    fig.add_trace(go.Scatter(x=[df_h['Year'].iloc[-1]],
                            y=[df_h['Bales'].iloc[-1]],
                            text=[df_h['Bales'].iloc[-1]],
                            name='',
                            mode='markers+text',
                            marker=dict(color='red', size=14),
                            textposition='top right',
                            textfont=dict(family="fjalla one, sans-serif", color="#006BA2", size=18),
                            texttemplate='%{text:.3s}', #text shorten into 3 digits
                            showlegend=False))

    #Adding value/text at year 2005, which is at index number 57
    fig.add_trace(go.Scatter(x=[df_h['Year'].iloc[57]],
                            y=[df_h['Bales'].iloc[57]],
                            text=[df_h['Bales'].iloc[57]],
                            name='',
                            mode='markers+text',
                            marker=dict(color='red', size=14),
                            textposition='middle right',
                            textfont=dict(family="fjalla one, sans-serif", color="#006BA2", size=18),
                            texttemplate='%{text:.3s}', #text shorten into 3 digits
                            showlegend=False))


    st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive

    ###########################
    ###########################
    #cotton map of Pakistan
    ###########################
    import json
    pak_districts = json.load(open("pakistan_districts.geojson", 'r'))

    district_id_map = {}
    for feature in pak_districts["features"]:
        feature["id"] = feature["properties"]["objectid"]
        district_id_map[feature['properties']['districts']] = feature['id']

    df['id']=df['District'].apply(lambda x:district_id_map[x])
    #st.title("Cotton Map of Pakistan")

    fig = go.Figure(go.Choroplethmapbox(geojson=pak_districts, locations=df.id, z=df.Bales,
                                        text= df['District'], 
                                        hoverinfo= 'text+z',
                                        reversescale=True,
                                                                            ))
    fig.update_layout(mapbox_style="stamen-terrain",
                    mapbox_zoom=5.0, mapbox_center = {"lat": 30.3753, "lon": 69.3451})
    fig.update_traces(text=df['District'])

    fig.update_layout(
        autosize=True, height=650, width=1400,
    )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    #####
    #st.plotly_chart(fig)

    ######################
    #######################
    st.title("Cotton Map of Pakistan")

    #satellite-streets
    #############

    fig = px.scatter_mapbox(df, 
                        lat="Lat", 
                        lon="Long", 
                        hover_name="District", 
                        hover_data=["District", "Bales"],
                        color_discrete_sequence=["Red"], 
                        size="Bales",
                        animation_frame="Year",
                        zoom=5,
                        height=300
                        )



    fig.update_layout(mapbox_style="open-street-map")


    fig.update_layout(
        autosize=True, height=700, width=1400,
    )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)

    ###########################
    ########################
    #monthly cotton imports




    ##############################
    #Cotton prices
    #############################
    import yfinance as yf

    from datetime import datetime, timedelta

    #data = yf.download(tickers=stock_price, period = ‘how_many_days’, interval = ‘how_long_between_each_check’, rounding= bool)
    #data = yf.download(tickers='CT=F', period = '5Y', interval = '1D', rounding= True)
    data = yf.download(tickers='CT=F', start = '2017-01-01', end = datetime.now().date(), rounding= True)

    #data 
    data= data.reset_index() # to show date as column header
    #data 

    ## getting the live ticker price

    # import stock_info module from yahoo_fin
    from yahoo_fin import stock_info as si

    #to get live price of ticker/cotton CT=F
    price = si.get_live_price('CT=F')
    prev_close = data.Close.iloc[-2] #iloc[-2] is second last row of res_df ; iloc[0] is first row 


    ##

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=data['Date'], 
                            y=data['Close'], 
                            name = '',
                            texttemplate='%{text:.2s}', # to  shorten text into 3 digits, use '%{text:.3s}'
                            ))
    fig.update_traces(hovertemplate='Date: %{x} <br>Price: %{y} cents per pound') #<br> adds space or shifts to next line; x & y is repected axis value; 

    fig.add_trace(go.Indicator(
                domain={"x": [0, 1], "y": [0.6, 1]},
                value=price,
                mode="number+delta",
                number={"font":{"size":50, "color":'#111111', "family":"roboto"}},
                title={"text": "Current Price in cents per pound"},
                title_font=dict(size=25, color='#111111', family="roboto"),
                delta={"reference": prev_close},
            ))

    fig.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=1,  #image postion on chart
            sizex=0.15, sizey=0.15, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    fig.update_yaxes(title_text = 'Cents Per Pound', tickprefix = '')
    #fig.update_xaxes(showspikes=True, spikecolor="red", spikesnap="cursor", spikemode="across", spikethickness=3) #xaxis spike on hover
    #fig.update_yaxes(showspikes=True, spikecolor="red", spikesnap="cursor", spikemode="across", spikethickness=3) #yais spike on hover

    fig.update_layout(
        autosize=True, height=650, width=1050,
        margin=dict(t=90, b=120, l=40, r=40),
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#111111', size=20, family="roboto, sans-serif"), 
        bargap=0.2,                             #value can be An int or float in the interval [0, 1]
    )

    fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black')

    fig.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig.update_yaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig.update_yaxes(title_font=dict(family='Roboto', color='black', size=24))

    #fig_cd.update_xaxes(font=dict(color='#111111', size=24, family="roboto, sans-serif"))

    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    fig.update_yaxes(title="Cents Per Pound",
        title_font=dict(size=25, color='#111111', family="roboto"),
        )

    fig.update_xaxes(
    rangeslider_visible = False, 
        rangeselector = dict(
        buttons = list([
        dict(count = 1, label = '1W', step = 'day', stepmode = 'backward'),
        dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
        dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
        dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
        dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
        dict(count = 2, label = '2Y', step = 'year', stepmode = 'backward'),
        dict(count = 5, label = '5Y', step = 'year', stepmode = 'backward'),
        #dict(step = 'all')
        ])))
    #title
    fig.add_annotation(
                text="Cotton Rates/ICE Futures",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="x domain", yref="y domain",
                x=0, y=1.19, 
                showarrow=False,
                arrowhead=1)


    fig.add_annotation(
                text="Source: Yahoo Finance/National Textile University",
                font=dict(family='Roboto', color='#111111', size=20), 
                xref="x domain", yref="y domain",
                x=0, y=-0.24, 
                showarrow=False,
                arrowhead=1)

    st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive

########################################


elif page == 'Overall Pakistan Trade':

    df = pd.read_csv('paktrade_pbs.csv')

    ##############

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
    image = Image.open('logo.png')                    
    #st.image(logo.png)
    fig.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=1,  #image postion on chart
            sizex=0.1, sizey=0.1, #image size on chart
            xanchor="right", yanchor="bottom"
        ))
    #layout
    fig.update_layout(
        autosize=False, height=650, width=1050,
        #legend_traceorder="reversed",
        margin=dict(t=80, b=110, l=40, r=40),
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
                x=0, y=-0.9, 
                showarrow=False,
                arrowhead=1)


    #legend
    fig.update_layout(legend=dict(
        orientation="h",
        font=dict(family='Roboto', color='#758D99', size=16), 
        yanchor="bottom",
        y=-0.16,
        xanchor="right",
        x=1))
    ######################
    #show figure in streamlit web app
    st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive
    ##############################
    ##############################

elif page == 'Raw Cotton Exports':
    #####################################
    #####################################
    # cotton chart US$
    df = pd.read_csv('monthly_textile_exports_pbs.csv')
    
    df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True) 

    df['year'] = df['date'].dt.year #creates a year column out of datetime columns
    df['month'] = df['date'].dt.month #creates a month column out of datetime columns
    
    df['year'] = df['year'].astype('string') #converting year column into string for filtering 
    df['month'] = df['month'].astype('string') #converting year column into string for filtering



    df['Fiscal Year'] = df['date'].dt.to_period('Q-JUN').dt.qyear.apply(lambda x: str(x-1) + "-" + str(x))
    #adding month column
    df['month'] = df['date'].dt.strftime('%b') #creating month names column
    #filtering data of fiscal year 2021-22
    df_cotton = df.loc[df['category'].isin(['Raw Cotton'])]

    #calculating year-to-date YTD exports
    df_cotton['Exports_YTD'] = df_cotton.groupby(['Fiscal Year'])['Exports_US$'].cumsum()

    df_cotton['pct_change_yoy'] = df_cotton.groupby(['month'])['Exports_YTD'].pct_change()*100
    #filtering data of fiscal year 2020-21
    df_cotton_2020_21 = df_cotton.loc[df_cotton['Fiscal Year'].isin(['2020-2021'])]
    df_cotton_2021_22 = df_cotton.loc[df_cotton['Fiscal Year'].isin(['2021-2022'])]



    fig_ytd = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.01, 
                        row_heights=[0.20,0.80])
    #fig_ytd = go.Figure()
    #fig_ytd = make_subplots(specs=[[{'secondary_y': True}]], rows=1, cols=1) # to make subplot with 1 row and 1 col

    # Add traces
    fig_ytd.add_trace(go.Bar(x=df_cotton_2020_21['month'], y=df_cotton_2020_21['Exports_YTD'],
                        name='Exports in 2020-21', 
                        text=df_cotton_2020_21['Exports_YTD'],
                        textposition='auto',
                        texttemplate='%{text:,}',
                        hovertemplate='Exports to date: %{y}'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_cotton_2021_22['month'], y=df_cotton_2021_22['Exports_YTD'],
                        mode='markers+lines+text',
                        marker=dict(size=16, color="Green"), 
                        name='Exports in 2021-22',
                        text=df_cotton_2021_22['Exports_YTD'],
                        textposition='bottom right',
                        texttemplate="%{text:,}",
                        line=dict(color='Green', width=4),
                        hovertemplate='Exports to date: %{y}B'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_cotton_2021_22['month'], 
                            y=df_cotton_2021_22['pct_change_yoy'], 
                            mode="lines+markers+text", 
                            marker=dict(size=16, color="Red"), 
                            name="%Change from previous year", 
                            text=df_cotton_2021_22['pct_change_yoy'],
                            textposition='middle right',
                            texttemplate="%{text:.3s}%",
                            line=dict(color='Red', width=1, dash='dash'),
                            hovertemplate='%{y}',
                            ), row=1, col=1 )
    #fig_ytd.update_yaxes(title_text="Cumulative Exports in US$")
    image = Image.open('logo.png')                    
    #st.image(logo.png)
    fig_ytd.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=-0.2,  #image postion on chart
            sizex=0.1, sizey=0.1, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    fig_ytd.update_layout(
        autosize=True, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=110, l=90, r=40),
        title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
        xaxis_title='', yaxis_title="",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
    )
    #updates axes
    fig_ytd.update_xaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_yaxes(visible=False, row=1, col=1 ) #range=[0, 100] if need to set y-axis range
    fig_ytd.update_yaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig_ytd.update_yaxes(title='Cumulative Exports (US$)', title_font=dict(family='Roboto', color='black', size=20), row=2, col=1)
    fig_ytd.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    ###############
    #title
    fig_ytd.add_annotation(
                text="Pakistan Raw Cotton Exports by Value",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="paper", yref="paper",
                x=0, y=1.18, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig_ytd.add_annotation(
                text="current year vs. previous year",
                font=dict(family='roboto', color='black', size=24), 
                xref="paper", yref="paper",
                x=0, y=1.10, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig_ytd.add_annotation(
                text="Source: Pakistan Bureau of Statistics",
                font=dict(family='Fjalla one', color='#758D99', size=20), 
                xref="paper", yref="paper",
                x=0, y=-0.2, 
                showarrow=False,
                arrowhead=1)

    fig_ytd.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    st.plotly_chart(fig_ytd, use_container_width=True) # to show Figure; container width true makes fig. size responsive

    #####################################
    #####################################
    # raw cotton chart volume

    #filtering data of fiscal year 2021-22
    #df_yarn = df.loc[df['category'].isin(['Cotton Yarn'])]

    #calculating year-to-date YTD exports
    df_cotton['vol_YTD'] = df_cotton.groupby(['Fiscal Year'])['volume'].cumsum()


    df_cotton['pct_change_yoy_vol'] = df_cotton.groupby(['month'])['vol_YTD'].pct_change()*100
    #filtering data of fiscal year 2020-21
    df_cotton_2020_21 = df_cotton.loc[df_cotton['Fiscal Year'].isin(['2020-2021'])]
    df_cotton_2021_22 = df_cotton.loc[df_cotton['Fiscal Year'].isin(['2021-2022'])]



    fig_ytd = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.01, 
                        row_heights=[0.20,0.80])
    #fig_ytd = go.Figure()
    #fig_ytd = make_subplots(specs=[[{'secondary_y': True}]], rows=1, cols=1) # to make subplot with 1 row and 1 col

    # Add traces
    fig_ytd.add_trace(go.Bar(x=df_cotton_2020_21['month'], y=df_cotton_2020_21['vol_YTD'],
                        name='Exports in 2020-21', 
                        text=df_cotton_2020_21['vol_YTD'],
                        textposition='auto',
                        texttemplate='%{text:,}',
                        hovertemplate='Exports to date: %{y}'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_cotton_2021_22['month'], y=df_cotton_2021_22['vol_YTD'],
                        mode='markers+lines+text',
                        marker=dict(size=16, color="Green"), 
                        name='Exports in 2021-22',
                        text=df_cotton_2021_22['vol_YTD'],
                        textposition='bottom right',
                        texttemplate="%{text:,}",
                        line=dict(color='Green', width=4),
                        hovertemplate='Exports to date: %{y}B'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_cotton_2021_22['month'], 
                            y=df_cotton_2021_22['pct_change_yoy_vol'], 
                            mode="lines+markers+text", 
                            marker=dict(size=16, color="Red"), 
                            name="%Change from previous year", 
                            text=df_cotton_2021_22['pct_change_yoy_vol'],
                            textposition='middle right',
                            texttemplate="%{text:.2s}%",
                            line=dict(color='Red', width=1, dash='dash'),
                            hovertemplate='%{y}',
                            ), row=1, col=1 )
    #fig_ytd.update_yaxes(title_text="Cumulative Exports in US$")
    image = Image.open('logo.png')                    
    #st.image(logo.png)
    fig_ytd.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=-0.2,  #image postion on chart
            sizex=0.1, sizey=0.1, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    fig_ytd.update_layout(
        autosize=True, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=110, l=90, r=40),
        title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
        xaxis_title='', yaxis_title="",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
    )
    #updates axes
    fig_ytd.update_xaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_yaxes(visible=False, row=1, col=1 ) #range=[0, 100] if need to set y-axis range

    fig_ytd.update_yaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig_ytd.update_yaxes(title='Cumulative Exports (Metric Tons)', title_font=dict(family='Roboto', color='black', size=20), row=2, col=1)
    fig_ytd.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    ###############
    #title
    fig_ytd.add_annotation(
                text="Pakistan Raw Cotton Exports by Volume",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="paper", yref="paper",
                x=0, y=1.18, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig_ytd.add_annotation(
                text="current year vs. previous year",
                font=dict(family='roboto', color='black', size=24), 
                xref="paper", yref="paper",
                x=0, y=1.10, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig_ytd.add_annotation(
                text="Source: Pakistan Bureau of Statistics",
                font=dict(family='Fjalla one', color='#758D99', size=20), 
                xref="paper", yref="paper",
                x=0, y=-0.2, 
                showarrow=False,
                arrowhead=1)

    fig_ytd.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    st.plotly_chart(fig_ytd, use_container_width=True) # to show Figure; container width true makes fig. size responsive

    #####################################
    #####################################
    # cotton chart export price

    df_cotton['pct_change_yoy_price'] = df_cotton.groupby(['month'])['unit_price'].pct_change()*100
    df_cotton_2020_21 = df_cotton.loc[df_cotton['Fiscal Year'].isin(['2020-2021'])]
    df_cotton_2021_22 = df_cotton.loc[df_cotton['Fiscal Year'].isin(['2021-2022'])]

    fig_ytd = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.01, 
                        row_heights=[0.20,0.80])
    #fig_ytd = go.Figure()
    #fig_ytd = make_subplots(specs=[[{'secondary_y': True}]], rows=1, cols=1) # to make subplot with 1 row and 1 col

    # Add traces
    fig_ytd.add_trace(go.Bar(x=df_cotton_2020_21['month'], y=df_cotton_2020_21['unit_price'],
                        name='Price in 2020-21', 
                        text=df_cotton_2020_21['unit_price'],
                        textposition='auto',
                        texttemplate='$%{text:.2f}',
                        hovertemplate='Exports price:$%{y}'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_cotton_2021_22['month'], y=df_cotton_2021_22['unit_price'],
                        mode='markers+lines+text',
                        marker=dict(size=16, color="Green"), 
                        name='Price in 2021-22',
                        text=df_cotton_2021_22['unit_price'],
                        textposition='bottom right',
                        texttemplate="$%{text:.2f}",
                        line=dict(color='Green', width=4),
                        hovertemplate='Exports price:$%{y}B'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_cotton_2021_22['month'], 
                            y=df_cotton_2021_22['pct_change_yoy_price'], 
                            mode="lines+markers+text", 
                            marker=dict(size=16, color="Red"), 
                            name="%Change from previous year", 
                            text=df_cotton_2021_22['pct_change_yoy_price'],
                            textposition='middle right',
                            texttemplate="%{text:.2}%",
                            line=dict(color='Red', width=1, dash='dash'),
                            hovertemplate='%{y}',
                            ), row=1, col=1 )
    #fig_ytd.update_yaxes(title_text="Cumulative Exports in US$")
    image = Image.open('logo.png')                    
    #st.image(logo.png)
    fig_ytd.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=-0.2,  #image postion on chart
            sizex=0.1, sizey=0.1, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    fig_ytd.update_layout(
        autosize=True, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=110, l=90, r=40),
        title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
        xaxis_title='', yaxis_title="",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
    )
    #updates axes
    fig_ytd.update_xaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_yaxes(visible=False, row=1, col=1 ) #range=[0, 100] if need to set y-axis range

    fig_ytd.update_yaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig_ytd.update_yaxes(title='US$ per Kg', title_font=dict(family='Roboto', color='black', size=20), row=2, col=1)
    fig_ytd.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    ###############
    #title
    fig_ytd.add_annotation(
                text="Pakistan Raw Cotton Average Export Price",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="paper", yref="paper",
                x=0, y=1.18, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig_ytd.add_annotation(
                text="current year vs. previous year",
                font=dict(family='roboto', color='black', size=24), 
                xref="paper", yref="paper",
                x=0, y=1.10, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig_ytd.add_annotation(
                text="Source: Pakistan Bureau of Statistics",
                font=dict(family='Fjalla one', color='#758D99', size=20), 
                xref="paper", yref="paper",
                x=0, y=-0.2, 
                showarrow=False,
                arrowhead=1)

    fig_ytd.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    #st.plotly_chart(fig_ytd, use_container_width=True) # to show Figure; container width true makes fig. size responsive

elif page == 'Cotton Yarn Exports':
    #####################################
    #####################################
    # yarn chart US$
    df = pd.read_csv('monthly_textile_exports_pbs.csv')
    
    df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True) 

    df['year'] = df['date'].dt.year #creates a year column out of datetime columns
    df['month'] = df['date'].dt.month #creates a month column out of datetime columns
    
    df['year'] = df['year'].astype('string') #converting year column into string for filtering 
    df['month'] = df['month'].astype('string') #converting year column into string for filtering



    df['Fiscal Year'] = df['date'].dt.to_period('Q-JUN').dt.qyear.apply(lambda x: str(x-1) + "-" + str(x))
    #adding month column
    df['month'] = df['date'].dt.strftime('%b') #creating month names column
    #filtering data of fiscal year 2021-22
    df_yarn = df.loc[df['category'].isin(['Cotton Yarn'])]

    #calculating year-to-date YTD exports
    df_yarn['Exports_YTD'] = df_yarn.groupby(['Fiscal Year'])['Exports_US$'].cumsum()

    df_yarn['pct_change_yoy'] = df_yarn.groupby(['month'])['Exports_YTD'].pct_change()*100
    #filtering data of fiscal year 2020-21
    df_yarn_2020_21 = df_yarn.loc[df_yarn['Fiscal Year'].isin(['2020-2021'])]
    df_yarn_2021_22 = df_yarn.loc[df_yarn['Fiscal Year'].isin(['2021-2022'])]



    fig_ytd = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.01, 
                        row_heights=[0.20,0.80])
    #fig_ytd = go.Figure()
    #fig_ytd = make_subplots(specs=[[{'secondary_y': True}]], rows=1, cols=1) # to make subplot with 1 row and 1 col

    # Add traces
    fig_ytd.add_trace(go.Bar(x=df_yarn_2020_21['month'], y=df_yarn_2020_21['Exports_YTD'],
                        name='Exports in 2020-21', 
                        text=df_yarn_2020_21['Exports_YTD'],
                        textposition='auto',
                        texttemplate='%{text:,}',
                        hovertemplate='Exports to date: %{y}'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_yarn_2021_22['month'], y=df_yarn_2021_22['Exports_YTD'],
                        mode='markers+lines+text',
                        marker=dict(size=16, color="Green"), 
                        name='Exports in 2021-22',
                        text=df_yarn_2021_22['Exports_YTD'],
                        textposition='top center',
                        texttemplate="%{text:,}",
                        line=dict(color='Green', width=4),
                        hovertemplate='Exports to date: %{y}B'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_yarn_2021_22['month'], 
                            y=df_yarn_2021_22['pct_change_yoy'], 
                            mode="lines+markers+text", 
                            marker=dict(size=16, color="Red"), 
                            name="%Change from previous year", 
                            text=df_yarn_2021_22['pct_change_yoy'],
                            textposition='middle right',
                            texttemplate="%{text:.2s}%",
                            line=dict(color='Red', width=1, dash='dash'),
                            hovertemplate='%{y}',
                            ), row=1, col=1 )
    #fig_ytd.update_yaxes(title_text="Cumulative Exports in US$")
    image = Image.open('logo.png')                    
    #st.image(logo.png)
    fig_ytd.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=-0.2,  #image postion on chart
            sizex=0.1, sizey=0.1, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    fig_ytd.update_layout(
        autosize=True, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=110, l=90, r=40),
        title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
        xaxis_title='', yaxis_title="",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
    )
    #updates axes
    fig_ytd.update_xaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_yaxes(visible=False, row=1, col=1 ) #range=[0, 100] if need to set y-axis range

    fig_ytd.update_yaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig_ytd.update_yaxes(title='Cumulative Exports (US$ Billion)', title_font=dict(family='Roboto', color='black', size=20), row=2, col=1)
    fig_ytd.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    ###############
    #title
    fig_ytd.add_annotation(
                text="Pakistan Cotton Yarn Exports by Value",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="paper", yref="paper",
                x=0, y=1.18, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig_ytd.add_annotation(
                text="current year vs. previous year",
                font=dict(family='roboto', color='black', size=24), 
                xref="paper", yref="paper",
                x=0, y=1.10, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig_ytd.add_annotation(
                text="Source: Pakistan Bureau of Statistics",
                font=dict(family='Fjalla one', color='#758D99', size=20), 
                xref="paper", yref="paper",
                x=0, y=-0.2, 
                showarrow=False,
                arrowhead=1)

    fig_ytd.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    st.plotly_chart(fig_ytd, use_container_width=True) # to show Figure; container width true makes fig. size responsive

    #####################################
    #####################################
    # yarn chart volume

    #filtering data of fiscal year 2021-22
    #df_yarn = df.loc[df['category'].isin(['Cotton Yarn'])]

    #calculating year-to-date YTD exports
    df_yarn['vol_YTD'] = df_yarn.groupby(['Fiscal Year'])['volume'].cumsum()


    df_yarn['pct_change_yoy_vol'] = df_yarn.groupby(['month'])['vol_YTD'].pct_change()*100
    #filtering data of fiscal year 2020-21
    df_yarn_2020_21 = df_yarn.loc[df_yarn['Fiscal Year'].isin(['2020-2021'])]
    df_yarn_2021_22 = df_yarn.loc[df_yarn['Fiscal Year'].isin(['2021-2022'])]



    fig_ytd = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.01, 
                        row_heights=[0.20,0.80])
    #fig_ytd = go.Figure()
    #fig_ytd = make_subplots(specs=[[{'secondary_y': True}]], rows=1, cols=1) # to make subplot with 1 row and 1 col

    # Add traces
    fig_ytd.add_trace(go.Bar(x=df_yarn_2020_21['month'], y=df_yarn_2020_21['vol_YTD'],
                        name='Exports in 2020-21', 
                        text=df_yarn_2020_21['vol_YTD'],
                        textposition='auto',
                        texttemplate='%{text:,}',
                        hovertemplate='Exports to date: %{y}'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_yarn_2021_22['month'], y=df_yarn_2021_22['vol_YTD'],
                        mode='markers+lines+text',
                        marker=dict(size=16, color="Green"), 
                        name='Exports in 2021-22',
                        text=df_yarn_2021_22['vol_YTD'],
                        textposition='top center',
                        texttemplate="%{text:,}",
                        line=dict(color='Green', width=4),
                        hovertemplate='Exports to date: %{y}B'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_yarn_2021_22['month'], 
                            y=df_yarn_2021_22['pct_change_yoy_vol'], 
                            mode="lines+markers+text", 
                            marker=dict(size=16, color="Red"), 
                            name="%Change from previous year", 
                            text=df_yarn_2021_22['pct_change_yoy_vol'],
                            textposition='middle right',
                            texttemplate="%{text:.2s}%",
                            line=dict(color='Red', width=1, dash='dash'),
                            hovertemplate='%{y}',
                            ), row=1, col=1 )
    #fig_ytd.update_yaxes(title_text="Cumulative Exports in US$")
    image = Image.open('logo.png')                    
    #st.image(logo.png)
    fig_ytd.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=-0.2,  #image postion on chart
            sizex=0.1, sizey=0.1, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    fig_ytd.update_layout(
        autosize=True, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=110, l=90, r=40),
        title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
        xaxis_title='', yaxis_title="",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
    )
    #updates axes
    fig_ytd.update_xaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_yaxes(visible=False, row=1, col=1 ) #range=[0, 100] if need to set y-axis range

    fig_ytd.update_yaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig_ytd.update_yaxes(title='Cumulative Exports (Metric Tons)', title_font=dict(family='Roboto', color='black', size=20), row=2, col=1)
    fig_ytd.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    ###############
    #title
    fig_ytd.add_annotation(
                text="Pakistan Cotton Yarn Exports by Volume",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="paper", yref="paper",
                x=0, y=1.18, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig_ytd.add_annotation(
                text="current year vs. previous year",
                font=dict(family='roboto', color='black', size=24), 
                xref="paper", yref="paper",
                x=0, y=1.10, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig_ytd.add_annotation(
                text="Source: Pakistan Bureau of Statistics",
                font=dict(family='Fjalla one', color='#758D99', size=20), 
                xref="paper", yref="paper",
                x=0, y=-0.2, 
                showarrow=False,
                arrowhead=1)

    fig_ytd.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    st.plotly_chart(fig_ytd, use_container_width=True) # to show Figure; container width true makes fig. size responsive

    #####################################
    #####################################
    # yarn chart export price

    df_yarn['pct_change_yoy_price'] = df_yarn.groupby(['month'])['unit_price'].pct_change()*100
    df_yarn_2020_21 = df_yarn.loc[df_yarn['Fiscal Year'].isin(['2020-2021'])]
    df_yarn_2021_22 = df_yarn.loc[df_yarn['Fiscal Year'].isin(['2021-2022'])]

    fig_ytd = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.01, 
                        row_heights=[0.20,0.80])
    #fig_ytd = go.Figure()
    #fig_ytd = make_subplots(specs=[[{'secondary_y': True}]], rows=1, cols=1) # to make subplot with 1 row and 1 col

    # Add traces
    fig_ytd.add_trace(go.Bar(x=df_yarn_2020_21['month'], y=df_yarn_2020_21['unit_price'],
                        name='Price in 2020-21', 
                        text=df_yarn_2020_21['unit_price'],
                        textposition='auto',
                        texttemplate='$%{text:.2f}',
                        hovertemplate='Exports price:$%{y}'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_yarn_2021_22['month'], y=df_yarn_2021_22['unit_price'],
                        mode='markers+lines+text',
                        marker=dict(size=16, color="Green"), 
                        name='Price in 2021-22',
                        text=df_yarn_2021_22['unit_price'],
                        textposition='bottom right',
                        texttemplate="$%{text:.2f}",
                        line=dict(color='Green', width=4),
                        hovertemplate='Exports price:$%{y}B'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_yarn_2021_22['month'], 
                            y=df_yarn_2021_22['pct_change_yoy_price'], 
                            mode="lines+markers+text", 
                            marker=dict(size=16, color="Red"), 
                            name="%Change from previous year", 
                            text=df_yarn_2021_22['pct_change_yoy_price'],
                            textposition='middle right',
                            texttemplate="%{text:.2s}%",
                            line=dict(color='Red', width=1, dash='dash'),
                            hovertemplate='%{y}',
                            ), row=1, col=1 )
    #fig_ytd.update_yaxes(title_text="Cumulative Exports in US$")
    image = Image.open('logo.png')                    
    #st.image(logo.png)
    fig_ytd.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=-0.2,  #image postion on chart
            sizex=0.1, sizey=0.1, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    fig_ytd.update_layout(
        autosize=True, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=110, l=90, r=40),
        title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
        xaxis_title='', yaxis_title="",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
    )
    #updates axes
    fig_ytd.update_xaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_yaxes(visible=False, row=1, col=1 ) #range=[0, 100] if need to set y-axis range

    fig_ytd.update_yaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig_ytd.update_yaxes(title='US$ per Kg', title_font=dict(family='Roboto', color='black', size=20), row=2, col=1)
    fig_ytd.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    ###############
    #title
    fig_ytd.add_annotation(
                text="Pakistan Cotton Yarn Average Export Price",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="paper", yref="paper",
                x=0, y=1.18, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig_ytd.add_annotation(
                text="current year vs. previous year",
                font=dict(family='roboto', color='black', size=24), 
                xref="paper", yref="paper",
                x=0, y=1.10, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig_ytd.add_annotation(
                text="Source: Pakistan Bureau of Statistics",
                font=dict(family='Fjalla one', color='#758D99', size=20), 
                xref="paper", yref="paper",
                x=0, y=-0.2, 
                showarrow=False,
                arrowhead=1)

    fig_ytd.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    st.plotly_chart(fig_ytd, use_container_width=True) # to show Figure; container width true makes fig. size responsive

elif page == 'Cotton Cloth Exports':
    #####################################
    #####################################
    # cloth chart US$
    df = pd.read_csv('monthly_textile_exports_pbs.csv')
    
    df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True) 

    df['year'] = df['date'].dt.year #creates a year column out of datetime columns
    df['month'] = df['date'].dt.month #creates a month column out of datetime columns
    
    df['year'] = df['year'].astype('string') #converting year column into string for filtering 
    df['month'] = df['month'].astype('string') #converting year column into string for filtering



    df['Fiscal Year'] = df['date'].dt.to_period('Q-JUN').dt.qyear.apply(lambda x: str(x-1) + "-" + str(x))
    #adding month column
    df['month'] = df['date'].dt.strftime('%b') #creating month names column
    #filtering data of fiscal year 2021-22
    df_cloth = df.loc[df['category'].isin(['Cotton Cloth'])]

    #calculating year-to-date YTD exports
    df_cloth['Exports_YTD'] = df_cloth.groupby(['Fiscal Year'])['Exports_US$'].cumsum()

    df_cloth['pct_change_yoy'] = df_cloth.groupby(['month'])['Exports_YTD'].pct_change()*100
    #filtering data of fiscal year 2020-21
    df_cloth_2020_21 = df_cloth.loc[df_cloth['Fiscal Year'].isin(['2020-2021'])]
    df_cloth_2021_22 = df_cloth.loc[df_cloth['Fiscal Year'].isin(['2021-2022'])]



    fig_ytd = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.01, 
                        row_heights=[0.20,0.80])
    #fig_ytd = go.Figure()
    #fig_ytd = make_subplots(specs=[[{'secondary_y': True}]], rows=1, cols=1) # to make subplot with 1 row and 1 col

    # Add traces
    fig_ytd.add_trace(go.Bar(x=df_cloth_2020_21['month'], y=df_cloth_2020_21['Exports_YTD'],
                        name='Exports in 2020-21', 
                        text=df_cloth_2020_21['Exports_YTD'],
                        textposition='auto',
                        texttemplate='%{text:,}',
                        hovertemplate='Exports to date: %{y}'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_cloth_2021_22['month'], y=df_cloth_2021_22['Exports_YTD'],
                        mode='markers+lines+text',
                        marker=dict(size=16, color="Green"), 
                        name='Exports in 2021-22',
                        text=df_cloth_2021_22['Exports_YTD'],
                        textposition='top center',
                        texttemplate="%{text:,}",
                        line=dict(color='Green', width=4),
                        hovertemplate='Exports to date: %{y}B'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_cloth_2021_22['month'], 
                            y=df_cloth_2021_22['pct_change_yoy'], 
                            mode="lines+markers+text", 
                            marker=dict(size=16, color="Red"), 
                            name="%Change from previous year", 
                            text=df_cloth_2021_22['pct_change_yoy'],
                            textposition='middle right',
                            texttemplate="%{text:.2s}%",
                            line=dict(color='Red', width=1, dash='dash'),
                            hovertemplate='%{y}',
                            ), row=1, col=1 )
    #fig_ytd.update_yaxes(title_text="Cumulative Exports in US$")
    image = Image.open('logo.png')                    
    #st.image(logo.png)
    fig_ytd.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=-0.2,  #image postion on chart
            sizex=0.1, sizey=0.1, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    fig_ytd.update_layout(
        autosize=True, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=110, l=90, r=40),
        title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
        xaxis_title='', yaxis_title="",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
    )
    #updates axes
    fig_ytd.update_xaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_yaxes(visible=False, row=1, col=1 ) #range=[0, 100] if need to set y-axis range

    fig_ytd.update_yaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig_ytd.update_yaxes(title='Cumulative Exports (US$)', title_font=dict(family='Roboto', color='black', size=20), row=2, col=1)
    fig_ytd.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    ###############
    #title
    fig_ytd.add_annotation(
                text="Pakistan Cotton Cloth Exports by Value",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="paper", yref="paper",
                x=0, y=1.18, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig_ytd.add_annotation(
                text="current year vs. previous year",
                font=dict(family='roboto', color='black', size=24), 
                xref="paper", yref="paper",
                x=0, y=1.10, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig_ytd.add_annotation(
                text="Source: Pakistan Bureau of Statistics",
                font=dict(family='Fjalla one', color='#758D99', size=20), 
                xref="paper", yref="paper",
                x=0, y=-0.2, 
                showarrow=False,
                arrowhead=1)

    fig_ytd.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    st.plotly_chart(fig_ytd, use_container_width=True) # to show Figure; container width true makes fig. size responsive

    #####################################
    #####################################
    # cloth chart volume

    #filtering data of fiscal year 2021-22
    #df_yarn = df.loc[df['category'].isin(['Cotton Yarn'])]

    #calculating year-to-date YTD exports
    df_cloth['vol_YTD'] = df_cloth.groupby(['Fiscal Year'])['volume'].cumsum()

    df_cloth['pct_change_yoy_vol'] = df_cloth.groupby(['month'])['vol_YTD'].pct_change()*100
    #filtering data of fiscal year 2020-21
    df_cloth_2020_21 = df_cloth.loc[df_cloth['Fiscal Year'].isin(['2020-2021'])]
    df_cloth_2021_22 = df_cloth.loc[df_cloth['Fiscal Year'].isin(['2021-2022'])]


    fig_ytd = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.01, 
                        row_heights=[0.20,0.80])
    #fig_ytd = go.Figure()
    #fig_ytd = make_subplots(specs=[[{'secondary_y': True}]], rows=1, cols=1) # to make subplot with 1 row and 1 col

    # Add traces
    fig_ytd.add_trace(go.Bar(x=df_cloth_2020_21['month'], y=df_cloth_2020_21['vol_YTD'],
                        name='Exports in 2020-21', 
                        text=df_cloth_2020_21['vol_YTD'],
                        textposition='auto',
                        texttemplate='%{text:,}',
                        hovertemplate='Exports to date: %{y}'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_cloth_2021_22['month'], y=df_cloth_2021_22['vol_YTD'],
                        mode='markers+lines+text',
                        marker=dict(size=16, color="Green"), 
                        name='Exports in 2021-22',
                        text=df_cloth_2021_22['vol_YTD'],
                        textposition='top center',
                        texttemplate="%{text:,}",
                        line=dict(color='Green', width=4),
                        hovertemplate='Exports to date: %{y}B'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_cloth_2021_22['month'], 
                            y=df_cloth_2021_22['pct_change_yoy_vol'], 
                            mode="lines+markers+text", 
                            marker=dict(size=16, color="Red"), 
                            name="%Change from previous year", 
                            text=df_cloth_2021_22['pct_change_yoy_vol'],
                            textposition='middle right',
                            texttemplate="%{text:.2s}%",
                            line=dict(color='Red', width=1, dash='dash'),
                            hovertemplate='%{y}',
                            ), row=1, col=1 )
    #fig_ytd.update_yaxes(title_text="Cumulative Exports in US$")
    image = Image.open('logo.png')                    
    #st.image(logo.png)
    fig_ytd.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=-0.2,  #image postion on chart
            sizex=0.1, sizey=0.1, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    fig_ytd.update_layout(
        autosize=True, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=110, l=90, r=40),
        title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
        xaxis_title='', yaxis_title="",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
    )
    #updates axes
    fig_ytd.update_xaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_yaxes(visible=False, row=1, col=1 ) #range=[0, 100] if need to set y-axis range

    fig_ytd.update_yaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig_ytd.update_yaxes(title='Cumulative Exports (Metric Tons)', title_font=dict(family='Roboto', color='black', size=20), row=2, col=1)
    fig_ytd.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    ###############
    #title
    fig_ytd.add_annotation(
                text="Pakistan Cotton Cloth Exports by Volume",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="paper", yref="paper",
                x=0, y=1.18, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig_ytd.add_annotation(
                text="current year vs. previous year",
                font=dict(family='roboto', color='black', size=24), 
                xref="paper", yref="paper",
                x=0, y=1.10, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig_ytd.add_annotation(
                text="Source: Pakistan Bureau of Statistics",
                font=dict(family='Fjalla one', color='#758D99', size=20), 
                xref="paper", yref="paper",
                x=0, y=-0.2, 
                showarrow=False,
                arrowhead=1)

    fig_ytd.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    st.plotly_chart(fig_ytd, use_container_width=True) # to show Figure; container width true makes fig. size responsive

    #####################################
    #####################################
   
elif page == 'Readymade Garments Exports':

    #####################################
    #####################################
    # garment chart value

    #importing csv file as dataframe
    df = pd.read_csv('monthly_textile_exports_pbs.csv')

    df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True) 

    df['year'] = df['date'].dt.year #creates a year column out of datetime columns
    df['month'] = df['date'].dt.month #creates a month column out of datetime columns
    
    df['year'] = df['year'].astype('string') #converting year column into string for filtering 
    df['month'] = df['month'].astype('string') #converting year column into string for filtering

    df['Fiscal Year'] = df['date'].dt.to_period('Q-JUN').dt.qyear.apply(lambda x: str(x-1) + "-" + str(x))
    #adding month column
    df['month'] = df['date'].dt.strftime('%b') #creating month names column

    df_garment = df.loc[df['category'].isin(['Garments'])]
    ##################################
    ##################################

    #calculating year-to-date YTD exports
    df_garment['Exports_YTD'] = df_garment.groupby(['Fiscal Year'])['Exports_US$'].cumsum()


    df_garment['pct_change_yoy'] = df_garment.groupby(['month'])['Exports_YTD'].pct_change()*100
    #filtering data of fiscal year 2020-21
    df_garment_2020_21 = df_garment.loc[df_garment['Fiscal Year'].isin(['2020-2021'])]
    df_garment_2021_22 = df_garment.loc[df_garment['Fiscal Year'].isin(['2021-2022'])]




    fig_ytd = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.01, 
                        row_heights=[0.20,0.80])
    #fig_ytd = go.Figure()
    #fig_ytd = make_subplots(specs=[[{'secondary_y': True}]], rows=1, cols=1) # to make subplot with 1 row and 1 col

    # Add traces
    fig_ytd.add_trace(go.Bar(x=df_garment_2020_21['month'], y=df_garment_2020_21['Exports_YTD'],
                        name='Exports in 2020-21', 
                        text=df_garment_2020_21['Exports_YTD'],
                        textposition='auto',
                        texttemplate='%{text:,}',
                        hovertemplate='Exports to date: %{y}'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_garment_2021_22['month'], y=df_garment_2021_22['Exports_YTD'],
                        mode='markers+lines+text',
                        marker=dict(size=16, color="Green"), 
                        name='Exports in 2021-22',
                        text=df_garment_2021_22['Exports_YTD'],
                        textposition='top center',
                        texttemplate="%{text:,}",
                        line=dict(color='Green', width=4),
                        hovertemplate='Exports to date: %{y}B'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_garment_2021_22['month'], 
                            y=df_garment_2021_22['pct_change_yoy'], 
                            mode="lines+markers+text", 
                            marker=dict(size=16, color="Red"), 
                            name="%Change from previous year", 
                            text=df_garment_2021_22['pct_change_yoy'],
                            textposition='middle right',
                            texttemplate="%{text:.2s}%",
                            line=dict(color='Red', width=1, dash='dash'),
                            hovertemplate='%{y}',
                            ), row=1, col=1 )
    #fig_ytd.update_yaxes(title_text="Cumulative Exports in US$")
    from PIL import Image
    image = Image.open('logo.png')                    
    #st.image(logo.png)
    fig_ytd.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=-0.2,  #image postion on chart
            sizex=0.1, sizey=0.1, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    fig_ytd.update_layout(
        autosize=True, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=110, l=90, r=40),
        title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
        xaxis_title='', yaxis_title="",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
    )
    #updates axes
    fig_ytd.update_xaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_yaxes(visible=False, row=1, col=1 ) #range=[0, 100] if need to set y-axis range

    fig_ytd.update_yaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig_ytd.update_yaxes(title='Cumulative Exports (US$ Billion)', title_font=dict(family='Roboto', color='black', size=20), row=2, col=1)
    fig_ytd.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    ###############
    #title
    fig_ytd.add_annotation(
                text="Pakistan Garment Exports by Value",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="paper", yref="paper",
                x=0, y=1.18, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig_ytd.add_annotation(
                text="current year vs. previous year",
                font=dict(family='roboto', color='black', size=24), 
                xref="paper", yref="paper",
                x=0, y=1.10, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig_ytd.add_annotation(
                text="Source: Pakistan Bureau of Statistics",
                font=dict(family='Fjalla one', color='#758D99', size=20), 
                xref="paper", yref="paper",
                x=0, y=-0.2, 
                showarrow=False,
                arrowhead=1)

    fig_ytd.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    st.plotly_chart(fig_ytd, use_container_width=True) # to show Figure; container width true makes fig. size responsive

    ##################################
    #calculating year-to-date YTD exports
    df_garment['Exports_YTD_vol'] = df_garment.groupby(['Fiscal Year'])['volume'].cumsum()


    df_garment['pct_change_yoy_vol'] = df_garment.groupby(['month'])['Exports_YTD_vol'].pct_change()*100
    #filtering data of fiscal year 2020-21
    df_garment_2020_21 = df_garment.loc[df_garment['Fiscal Year'].isin(['2020-2021'])]
    df_garment_2021_22 = df_garment.loc[df_garment['Fiscal Year'].isin(['2021-2022'])]




    fig_ytd = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.01, 
                        row_heights=[0.20,0.80])
    #fig_ytd = go.Figure()
    #fig_ytd = make_subplots(specs=[[{'secondary_y': True}]], rows=1, cols=1) # to make subplot with 1 row and 1 col

    # Add traces
    fig_ytd.add_trace(go.Bar(x=df_garment_2020_21['month'], y=df_garment_2020_21['Exports_YTD_vol'],
                        name='Exports in 2020-21', 
                        text=df_garment_2020_21['Exports_YTD_vol'],
                        textposition='auto',
                        texttemplate='%{text:,}',
                        hovertemplate='Exports to date: %{y}'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_garment_2021_22['month'], y=df_garment_2021_22['Exports_YTD_vol'],
                        mode='markers+lines+text',
                        marker=dict(size=16, color="Green"), 
                        name='Exports in 2021-22',
                        text=df_garment_2021_22['Exports_YTD_vol'],
                        textposition='top center',
                        texttemplate="%{text:,}",
                        line=dict(color='Green', width=4),
                        hovertemplate='Exports to date: %{y}B'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_garment_2021_22['month'], 
                            y=df_garment_2021_22['pct_change_yoy_vol'], 
                            mode="lines+markers+text", 
                            marker=dict(size=16, color="Red"), 
                            name="%Change from previous year", 
                            text=df_garment_2021_22['pct_change_yoy_vol'],
                            textposition='middle right',
                            texttemplate="%{text:.2s}%",
                            line=dict(color='Red', width=1, dash='dash'),
                            hovertemplate='%{y}',
                            ), row=1, col=1 )
    #fig_ytd.update_yaxes(title_text="Cumulative Exports in US$")
    image = Image.open('logo.png')                    
    #st.image(logo.png)
    fig_ytd.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=-0.2,  #image postion on chart
            sizex=0.1, sizey=0.1, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    fig_ytd.update_layout(
        autosize=True, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=110, l=90, r=40),
        title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
        xaxis_title='', yaxis_title="",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
    )
    #updates axes
    fig_ytd.update_xaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_yaxes(visible=False, row=1, col=1 ) #range=[0, 100] if need to set y-axis range

    fig_ytd.update_yaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig_ytd.update_yaxes(title='Cumulative Exports ()', title_font=dict(family='Roboto', color='black', size=20), row=2, col=1)
    fig_ytd.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    ###############
    #title
    fig_ytd.add_annotation(
                text="Pakistan Garments Exports by Volume",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="paper", yref="paper",
                x=0, y=1.18, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig_ytd.add_annotation(
                text="current year vs. previous year",
                font=dict(family='roboto', color='black', size=24), 
                xref="paper", yref="paper",
                x=0, y=1.10, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig_ytd.add_annotation(
                text="Source: Pakistan Bureau of Statistics",
                font=dict(family='Fjalla one', color='#758D99', size=20), 
                xref="paper", yref="paper",
                x=0, y=-0.2, 
                showarrow=False,
                arrowhead=1)

    fig_ytd.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    st.plotly_chart(fig_ytd, use_container_width=True) # to show Figure; container width true makes fig. size responsive


elif page == 'Knitwear Exports':

    #####################################
    #####################################
    #importing csv file as dataframe
    df = pd.read_csv('monthly_textile_exports_pbs.csv')

    df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True) 

    df['year'] = df['date'].dt.year #creates a year column out of datetime columns
    df['month'] = df['date'].dt.month #creates a month column out of datetime columns
    
    df['year'] = df['year'].astype('string') #converting year column into string for filtering 
    df['month'] = df['month'].astype('string') #converting year column into string for filtering

    df['Fiscal Year'] = df['date'].dt.to_period('Q-JUN').dt.qyear.apply(lambda x: str(x-1) + "-" + str(x))
    #adding month column
    df['month'] = df['date'].dt.strftime('%b') #creating month names column
    # knitwear chart value


    df_knitwear = df.loc[df['category'].isin(['Knitwear'])]

    #calculating year-to-date YTD exports
    df_knitwear['Exports_YTD'] = df_knitwear.groupby(['Fiscal Year'])['Exports_US$'].cumsum()


    df_knitwear['pct_change_yoy'] = df_knitwear.groupby(['month'])['Exports_YTD'].pct_change()*100
    #filtering data of fiscal year 2020-21
    df_knitwear_2020_21 = df_knitwear.loc[df_knitwear['Fiscal Year'].isin(['2020-2021'])]
    df_knitwear_2021_22 = df_knitwear.loc[df_knitwear['Fiscal Year'].isin(['2021-2022'])]




    fig_ytd = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.01, 
                        row_heights=[0.20,0.80])
    #fig_ytd = go.Figure()
    #fig_ytd = make_subplots(specs=[[{'secondary_y': True}]], rows=1, cols=1) # to make subplot with 1 row and 1 col

    # Add traces
    fig_ytd.add_trace(go.Bar(x=df_knitwear_2020_21['month'], y=df_knitwear_2020_21['Exports_YTD'],
                        name='Exports in 2020-21', 
                        text=df_knitwear_2020_21['Exports_YTD'],
                        textposition='auto',
                        texttemplate='%{text:,}',
                        hovertemplate='Exports to date: %{y}'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_knitwear_2021_22['month'], y=df_knitwear_2021_22['Exports_YTD'],
                        mode='markers+lines+text',
                        marker=dict(size=16, color="Green"), 
                        name='Exports in 2021-22',
                        text=df_knitwear_2021_22['Exports_YTD'],
                        textposition='top center',
                        texttemplate="%{text:,}",
                        line=dict(color='Green', width=4),
                        hovertemplate='Exports to date: %{y}B'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_knitwear_2021_22['month'], 
                            y=df_knitwear_2021_22['pct_change_yoy'], 
                            mode="lines+markers+text", 
                            marker=dict(size=16, color="Red"), 
                            name="%Change from previous year", 
                            text=df_knitwear_2021_22['pct_change_yoy'],
                            textposition='middle right',
                            texttemplate="%{text:.2s}%",
                            line=dict(color='Red', width=1, dash='dash'),
                            hovertemplate='%{y}',
                            ), row=1, col=1 )
    #fig_ytd.update_yaxes(title_text="Cumulative Exports in US$")
    from PIL import Image
    image = Image.open('logo.png')                    
    #st.image(logo.png)
    fig_ytd.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=-0.2,  #image postion on chart
            sizex=0.1, sizey=0.1, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    fig_ytd.update_layout(
        autosize=True, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=110, l=90, r=40),
        title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
        xaxis_title='', yaxis_title="",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
    )
    #updates axes
    fig_ytd.update_xaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_yaxes(visible=False, row=1, col=1 ) #range=[0, 100] if need to set y-axis range

    fig_ytd.update_yaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig_ytd.update_yaxes(title='Cumulative Exports (US$ Billion)', title_font=dict(family='Roboto', color='black', size=20), row=2, col=1)
    fig_ytd.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    ###############
    #title
    fig_ytd.add_annotation(
                text="Pakistan Knitwear Exports by Value",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="paper", yref="paper",
                x=0, y=1.18, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig_ytd.add_annotation(
                text="current year vs. previous year",
                font=dict(family='roboto', color='black', size=24), 
                xref="paper", yref="paper",
                x=0, y=1.10, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig_ytd.add_annotation(
                text="Source: Pakistan Bureau of Statistics",
                font=dict(family='Fjalla one', color='#758D99', size=20), 
                xref="paper", yref="paper",
                x=0, y=-0.2, 
                showarrow=False,
                arrowhead=1)

    fig_ytd.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    st.plotly_chart(fig_ytd, use_container_width=True) # to show Figure; container width true makes fig. size responsive

    ###############################################
    #############################################
    #calculating year-to-date YTD exports by volume
    df_knitwear['Exports_YTD_vol'] = df_knitwear.groupby(['Fiscal Year'])['volume'].cumsum()


    df_knitwear['pct_change_yoy_vol'] = df_knitwear.groupby(['month'])['Exports_YTD_vol'].pct_change()*100
    #filtering data of fiscal year 2020-21
    df_knitwear_2020_21 = df_knitwear.loc[df_knitwear['Fiscal Year'].isin(['2020-2021'])]
    df_knitwear_2021_22 = df_knitwear.loc[df_knitwear['Fiscal Year'].isin(['2021-2022'])]

    fig_ytd = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.01, 
                        row_heights=[0.20,0.80])
    #fig_ytd = go.Figure()
    #fig_ytd = make_subplots(specs=[[{'secondary_y': True}]], rows=1, cols=1) # to make subplot with 1 row and 1 col

    # Add traces
    fig_ytd.add_trace(go.Bar(x=df_knitwear_2020_21['month'], y=df_knitwear_2020_21['Exports_YTD_vol'],
                        name='Exports in 2020-21', 
                        text=df_knitwear_2020_21['Exports_YTD_vol'],
                        textposition='auto',
                        texttemplate='%{text:,}',
                        hovertemplate='Exports to date: %{y}'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_knitwear_2021_22['month'], y=df_knitwear_2021_22['Exports_YTD_vol'],
                        mode='markers+lines+text',
                        marker=dict(size=16, color="Green"), 
                        name='Exports in 2021-22',
                        text=df_knitwear_2021_22['Exports_YTD_vol'],
                        textposition='top center',
                        texttemplate="%{text:,}",
                        line=dict(color='Green', width=4),
                        hovertemplate='Exports to date: %{y}B'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_knitwear_2021_22['month'], 
                            y=df_knitwear_2021_22['pct_change_yoy_vol'], 
                            mode="lines+markers+text", 
                            marker=dict(size=16, color="Red"), 
                            name="%Change from previous year", 
                            text=df_knitwear_2021_22['pct_change_yoy_vol'],
                            textposition='middle right',
                            texttemplate="%{text:.2f}%",
                            line=dict(color='Red', width=1, dash='dash'),
                            hovertemplate='%{y}',
                            ), row=1, col=1 )
    #fig_ytd.update_yaxes(title_text="Cumulative Exports in US$")
    image = Image.open('logo.png')                    
    #st.image(logo.png)
    fig_ytd.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=-0.2,  #image postion on chart
            sizex=0.1, sizey=0.1, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    fig_ytd.update_layout(
        autosize=True, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=110, l=90, r=40),
        title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
        xaxis_title='', yaxis_title="",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
    )
    #updates axes
    fig_ytd.update_xaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_yaxes(visible=False, row=1, col=1 ) #range=[0, 100] if need to set y-axis range

    fig_ytd.update_yaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig_ytd.update_yaxes(title='Cumulative Exports (Dozens)', title_font=dict(family='Roboto', color='black', size=20), row=2, col=1)
    fig_ytd.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    ###############
    #title
    fig_ytd.add_annotation(
                text="Pakistan Knitwear Exports by Volume",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="paper", yref="paper",
                x=0, y=1.18, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig_ytd.add_annotation(
                text="current year vs. previous year",
                font=dict(family='roboto', color='black', size=24), 
                xref="paper", yref="paper",
                x=0, y=1.10, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig_ytd.add_annotation(
                text="Source: Pakistan Bureau of Statistics",
                font=dict(family='Fjalla one', color='#758D99', size=20), 
                xref="paper", yref="paper",
                x=0, y=-0.2, 
                showarrow=False,
                arrowhead=1)

    fig_ytd.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    st.plotly_chart(fig_ytd, use_container_width=True) # to show Figure; container width true makes fig. size responsive

elif page == 'Bedwear Exports':

    #####################################
    #####################################
    #importing csv file as dataframe
    df = pd.read_csv('monthly_textile_exports_pbs.csv')

    df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True) 

    df['year'] = df['date'].dt.year #creates a year column out of datetime columns
    df['month'] = df['date'].dt.month #creates a month column out of datetime columns
    
    df['year'] = df['year'].astype('string') #converting year column into string for filtering 
    df['month'] = df['month'].astype('string') #converting year column into string for filtering

    df['Fiscal Year'] = df['date'].dt.to_period('Q-JUN').dt.qyear.apply(lambda x: str(x-1) + "-" + str(x))
    #adding month column
    df['month'] = df['date'].dt.strftime('%b') #creating month names column
    #####################################
    # bedwear chart value


    df_bedwear = df.loc[df['category'].isin(['Bedwear'])]

    #calculating year-to-date YTD exports
    df_bedwear['Exports_YTD'] = df_bedwear.groupby(['Fiscal Year'])['Exports_US$'].cumsum()


    df_bedwear['pct_change_yoy'] = df_bedwear.groupby(['month'])['Exports_YTD'].pct_change()*100
    #filtering data of fiscal year 2020-21
    df_bedwear_2020_21 = df_bedwear.loc[df_bedwear['Fiscal Year'].isin(['2020-2021'])]
    df_bedwear_2021_22 = df_bedwear.loc[df_bedwear['Fiscal Year'].isin(['2021-2022'])]

    fig_ytd = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.01, 
                        row_heights=[0.20,0.80])
    #fig_ytd = go.Figure()
    #fig_ytd = make_subplots(specs=[[{'secondary_y': True}]], rows=1, cols=1) # to make subplot with 1 row and 1 col

    # Add traces
    fig_ytd.add_trace(go.Bar(x=df_bedwear_2020_21['month'], y=df_bedwear_2020_21['Exports_YTD'],
                        name='Exports in 2020-21', 
                        text=df_bedwear_2020_21['Exports_YTD'],
                        textposition='auto',
                        texttemplate='%{text:,}',
                        hovertemplate='Exports to date: %{y}'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_bedwear_2021_22['month'], y=df_bedwear_2021_22['Exports_YTD'],
                        mode='markers+lines+text',
                        marker=dict(size=16, color="Green"), 
                        name='Exports in 2021-22',
                        text=df_bedwear_2021_22['Exports_YTD'],
                        textposition='top center',
                        texttemplate="%{text:,}",
                        line=dict(color='Green', width=4),
                        hovertemplate='Exports to date: %{y}B'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_bedwear_2021_22['month'], 
                            y=df_bedwear_2021_22['pct_change_yoy'], 
                            mode="lines+markers+text", 
                            marker=dict(size=16, color="Red"), 
                            name="%Change from previous year", 
                            text=df_bedwear_2021_22['pct_change_yoy'],
                            textposition='middle right',
                            texttemplate="%{text:.2s}%",
                            line=dict(color='Red', width=1, dash='dash'),
                            hovertemplate='%{y}',
                            ), row=1, col=1 )
    #fig_ytd.update_yaxes(title_text="Cumulative Exports in US$")
    image = Image.open('logo.png')                    
    #st.image(logo.png)
    fig_ytd.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=-0.2,  #image postion on chart
            sizex=0.1, sizey=0.1, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    fig_ytd.update_layout(
        autosize=True, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=110, l=90, r=40),
        title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
        xaxis_title='', yaxis_title="",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
    )
    #updates axes
    fig_ytd.update_xaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_yaxes(visible=False, row=1, col=1 ) #range=[0, 100] if need to set y-axis range

    fig_ytd.update_yaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig_ytd.update_yaxes(title='Cumulative Exports (US$ Billion)', title_font=dict(family='Roboto', color='black', size=20), row=2, col=1)
    fig_ytd.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    ###############
    #title
    fig_ytd.add_annotation(
                text="Pakistan Bedwear Exports by Value",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="paper", yref="paper",
                x=0, y=1.18, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig_ytd.add_annotation(
                text="current year vs. previous year",
                font=dict(family='roboto', color='black', size=24), 
                xref="paper", yref="paper",
                x=0, y=1.10, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig_ytd.add_annotation(
                text="Source: Pakistan Bureau of Statistics",
                font=dict(family='Fjalla one', color='#758D99', size=20), 
                xref="paper", yref="paper",
                x=0, y=-0.2, 
                showarrow=False,
                arrowhead=1)

    fig_ytd.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    st.plotly_chart(fig_ytd, use_container_width=True) # to show Figure; container width true makes fig. size responsive

    #####################################
    #####################################
    # bedwear chart volume


    df_bedwear = df.loc[df['category'].isin(['Bedwear'])]

    #calculating year-to-date YTD exports
    df_bedwear['Exports_YTD_vol'] = df_bedwear.groupby(['Fiscal Year'])['volume'].cumsum()


    df_bedwear['pct_change_yoy_vol'] = df_bedwear.groupby(['month'])['Exports_YTD_vol'].pct_change()*100
    #filtering data of fiscal year 2020-21
    df_bedwear_2020_21 = df_bedwear.loc[df_bedwear['Fiscal Year'].isin(['2020-2021'])]
    df_bedwear_2021_22 = df_bedwear.loc[df_bedwear['Fiscal Year'].isin(['2021-2022'])]




    fig_ytd = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.01, 
                        row_heights=[0.20,0.80])
    #fig_ytd = go.Figure()
    #fig_ytd = make_subplots(specs=[[{'secondary_y': True}]], rows=1, cols=1) # to make subplot with 1 row and 1 col

    # Add traces
    fig_ytd.add_trace(go.Bar(x=df_bedwear_2020_21['month'], y=df_bedwear_2020_21['Exports_YTD_vol'],
                        name='Exports in 2020-21', 
                        text=df_bedwear_2020_21['Exports_YTD_vol'],
                        textposition='auto',
                        texttemplate='%{text:,}',
                        hovertemplate='Exports to date: %{y}'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_bedwear_2021_22['month'], y=df_bedwear_2021_22['Exports_YTD_vol'],
                        mode='markers+lines+text',
                        marker=dict(size=16, color="Green"), 
                        name='Exports in 2021-22',
                        text=df_bedwear_2021_22['Exports_YTD_vol'],
                        textposition='top center',
                        texttemplate="%{text:,}",
                        line=dict(color='Green', width=4),
                        hovertemplate='Exports to date: %{y}B'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_bedwear_2021_22['month'], 
                            y=df_bedwear_2021_22['pct_change_yoy_vol'], 
                            mode="lines+markers+text", 
                            marker=dict(size=16, color="Red"), 
                            name="%Change from previous year", 
                            text=df_bedwear_2021_22['pct_change_yoy_vol'],
                            textposition='middle right',
                            texttemplate="%{text:.2f}%",
                            line=dict(color='Red', width=1, dash='dash'),
                            hovertemplate='%{y}',
                            ), row=1, col=1 )
    #fig_ytd.update_yaxes(title_text="Cumulative Exports in US$")
    image = Image.open('logo.png')                    
    #st.image(logo.png)
    fig_ytd.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=-0.2,  #image postion on chart
            sizex=0.1, sizey=0.1, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    fig_ytd.update_layout(
        autosize=True, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=110, l=90, r=40),
        title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
        xaxis_title='', yaxis_title="",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
    )
    #updates axes
    fig_ytd.update_xaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_yaxes(visible=False, row=1, col=1 ) #range=[0, 100] if need to set y-axis range

    fig_ytd.update_yaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig_ytd.update_yaxes(title='Cumulative Exports (Metric Tons)', title_font=dict(family='Roboto', color='black', size=20), row=2, col=1)
    fig_ytd.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    ###############
    #title
    fig_ytd.add_annotation(
                text="Pakistan Bedwear Exports by Volume",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="paper", yref="paper",
                x=0, y=1.18, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig_ytd.add_annotation(
                text="current year vs. previous year",
                font=dict(family='roboto', color='black', size=24), 
                xref="paper", yref="paper",
                x=0, y=1.10, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig_ytd.add_annotation(
                text="Source: Pakistan Bureau of Statistics",
                font=dict(family='Fjalla one', color='#758D99', size=20), 
                xref="paper", yref="paper",
                x=0, y=-0.2, 
                showarrow=False,
                arrowhead=1)

    fig_ytd.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    st.plotly_chart(fig_ytd, use_container_width=True) # to show Figure; container width true makes fig. size responsive

    ################
elif page == 'Towel Exports':

    #####################################
    #####################################
    #importing csv file as dataframe
    df = pd.read_csv('monthly_textile_exports_pbs.csv')

    df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True) 

    df['year'] = df['date'].dt.year #creates a year column out of datetime columns
    df['month'] = df['date'].dt.month #creates a month column out of datetime columns
    
    df['year'] = df['year'].astype('string') #converting year column into string for filtering 
    df['month'] = df['month'].astype('string') #converting year column into string for filtering

    df['Fiscal Year'] = df['date'].dt.to_period('Q-JUN').dt.qyear.apply(lambda x: str(x-1) + "-" + str(x))
    #adding month column
    df['month'] = df['date'].dt.strftime('%b') #creating month names column
    #####################################
    # bedwear chart value


    df_towels = df.loc[df['category'].isin(['Towels'])]

    #calculating year-to-date YTD exports
    df_towels['Exports_YTD'] = df_towels.groupby(['Fiscal Year'])['Exports_US$'].cumsum()


    df_towels['pct_change_yoy'] = df_towels.groupby(['month'])['Exports_YTD'].pct_change()*100
    #filtering data of fiscal year 2020-21
    df_towels_2020_21 = df_towels.loc[df_towels['Fiscal Year'].isin(['2020-2021'])]
    df_towels_2021_22 = df_towels.loc[df_towels['Fiscal Year'].isin(['2021-2022'])]

    fig_ytd = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.01, 
                        row_heights=[0.20,0.80])
    #fig_ytd = go.Figure()
    #fig_ytd = make_subplots(specs=[[{'secondary_y': True}]], rows=1, cols=1) # to make subplot with 1 row and 1 col

    # Add traces
    fig_ytd.add_trace(go.Bar(x=df_towels_2020_21['month'], y=df_towels_2020_21['Exports_YTD'],
                        name='Exports in 2020-21', 
                        text=df_towels_2020_21['Exports_YTD'],
                        textposition='auto',
                        texttemplate='%{text:,}',
                        hovertemplate='Exports to date: %{y}'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_towels_2021_22['month'], y=df_towels_2021_22['Exports_YTD'],
                        mode='markers+lines+text',
                        marker=dict(size=16, color="Green"), 
                        name='Exports in 2021-22',
                        text=df_towels_2021_22['Exports_YTD'],
                        textposition='top center',
                        texttemplate="%{text:,}",
                        line=dict(color='Green', width=4),
                        hovertemplate='Exports to date: %{y}B'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_towels_2021_22['month'], 
                            y=df_towels_2021_22['pct_change_yoy'], 
                            mode="lines+markers+text", 
                            marker=dict(size=16, color="Red"), 
                            name="%Change from previous year", 
                            text=df_towels_2021_22['pct_change_yoy'],
                            textposition='middle right',
                            texttemplate="%{text:.2s}%",
                            line=dict(color='Red', width=1, dash='dash'),
                            hovertemplate='%{y}',
                            ), row=1, col=1 )
    #fig_ytd.update_yaxes(title_text="Cumulative Exports in US$")
    image = Image.open('logo.png')                    
    #st.image(logo.png)
    fig_ytd.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=-0.2,  #image postion on chart
            sizex=0.1, sizey=0.1, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    fig_ytd.update_layout(
        autosize=True, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=110, l=90, r=40),
        title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
        xaxis_title='', yaxis_title="",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
    )
    #updates axes
    fig_ytd.update_xaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_yaxes(visible=False, row=1, col=1 ) #range=[0, 100] if need to set y-axis range

    fig_ytd.update_yaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig_ytd.update_yaxes(title='Cumulative Exports (US$)', title_font=dict(family='Roboto', color='black', size=20), row=2, col=1)
    fig_ytd.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    ###############
    #title
    fig_ytd.add_annotation(
                text="Pakistan Towels Exports by Value",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="paper", yref="paper",
                x=0, y=1.18, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig_ytd.add_annotation(
                text="current year vs. previous year",
                font=dict(family='roboto', color='black', size=24), 
                xref="paper", yref="paper",
                x=0, y=1.10, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig_ytd.add_annotation(
                text="Source: Pakistan Bureau of Statistics",
                font=dict(family='Fjalla one', color='#758D99', size=20), 
                xref="paper", yref="paper",
                x=0, y=-0.2, 
                showarrow=False,
                arrowhead=1)

    fig_ytd.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    st.plotly_chart(fig_ytd, use_container_width=True) # to show Figure; container width true makes fig. size responsive

    #####################################
    #####################################
    # bedwear chart volume



    #calculating year-to-date YTD exports
    df_towels['Exports_YTD_vol'] = df_towels.groupby(['Fiscal Year'])['volume'].cumsum()
    df_towels['pct_change_yoy_vol'] = df_towels.groupby(['month'])['Exports_YTD_vol'].pct_change()*100
    #filtering data of fiscal year 2020-21
    df_towels_2020_21 = df_towels.loc[df_towels['Fiscal Year'].isin(['2020-2021'])]
    df_towels_2021_22 = df_towels.loc[df_towels['Fiscal Year'].isin(['2021-2022'])]




    fig_ytd = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.01, 
                        row_heights=[0.20,0.80])
    #fig_ytd = go.Figure()
    #fig_ytd = make_subplots(specs=[[{'secondary_y': True}]], rows=1, cols=1) # to make subplot with 1 row and 1 col

    # Add traces
    fig_ytd.add_trace(go.Bar(x=df_towels_2020_21['month'], y=df_towels_2020_21['Exports_YTD_vol'],
                        name='Exports in 2020-21', 
                        text=df_towels_2020_21['Exports_YTD_vol'],
                        textposition='auto',
                        texttemplate='%{text:,}',
                        hovertemplate='Exports to date: %{y}'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_towels_2021_22['month'], y=df_towels_2021_22['Exports_YTD_vol'],
                        mode='markers+lines+text',
                        marker=dict(size=16, color="Green"), 
                        name='Exports in 2021-22',
                        text=df_towels_2021_22['Exports_YTD_vol'],
                        textposition='top center',
                        texttemplate="%{text:,}",
                        line=dict(color='Green', width=4),
                        hovertemplate='Exports to date: %{y}B'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_towels_2021_22['month'], 
                            y=df_towels_2021_22['pct_change_yoy_vol'], 
                            mode="lines+markers+text", 
                            marker=dict(size=16, color="Red"), 
                            name="%Change from previous year", 
                            text=df_towels_2021_22['pct_change_yoy_vol'],
                            textposition='middle right',
                            texttemplate="%{text:.2f}%",
                            line=dict(color='Red', width=1, dash='dash'),
                            hovertemplate='%{y}',
                            ), row=1, col=1 )
    #fig_ytd.update_yaxes(title_text="Cumulative Exports in US$")
    image = Image.open('logo.png')                    
    #st.image(logo.png)
    fig_ytd.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=-0.2,  #image postion on chart
            sizex=0.1, sizey=0.1, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    fig_ytd.update_layout(
        autosize=True, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=110, l=90, r=40),
        title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
        xaxis_title='', yaxis_title="",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
    )
    #updates axes
    fig_ytd.update_xaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_yaxes(visible=False, row=1, col=1 ) #range=[0, 100] if need to set y-axis range

    fig_ytd.update_yaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig_ytd.update_yaxes(title='Cumulative Exports (Metric Tons)', title_font=dict(family='Roboto', color='black', size=20), row=2, col=1)
    fig_ytd.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    ###############
    #title
    fig_ytd.add_annotation(
                text="Pakistan Towels Exports by Volume",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="paper", yref="paper",
                x=0, y=1.18, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig_ytd.add_annotation(
                text="current year vs. previous year",
                font=dict(family='roboto', color='black', size=24), 
                xref="paper", yref="paper",
                x=0, y=1.10, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig_ytd.add_annotation(
                text="Source: Pakistan Bureau of Statistics",
                font=dict(family='Fjalla one', color='#758D99', size=20), 
                xref="paper", yref="paper",
                x=0, y=-0.2, 
                showarrow=False,
                arrowhead=1)

    fig_ytd.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    st.plotly_chart(fig_ytd, use_container_width=True) # to show Figure; container width true makes fig. size responsive

else:
    index=0
    #st.title("Pakistan Textile Exports")

    #importing csv file as dataframe
    df = pd.read_csv('monthly_textile_exports_pbs.csv')
    #df # to see dataframe
    #df
    #convert date columns into datetime format
    #to convert big numbers to M, B,

    df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True) 

    df['year'] = df['date'].dt.year #creates a year column out of datetime columns
    df['month'] = df['date'].dt.month #creates a month column out of datetime columns
    
    df['year'] = df['year'].astype('string') #converting year column into string for filtering 
    df['month'] = df['month'].astype('string') #converting year column into string for filtering

    #grouping all categories of exports in monthly frequency, preserving datetime index
    df_monthly_sum = df.groupby(pd.Grouper(key = 'date', freq='1M')).sum().reset_index()
    #adding 'Fiscal Year' columns
    df_monthly_sum['Fiscal Year'] = df_monthly_sum['date'].dt.to_period('Q-JUN').dt.qyear.apply(lambda x: str(x-1) + "-" + str(x))
    #adding month column
    df_monthly_sum['month'] = df_monthly_sum['date'].dt.strftime('%b') #creating month names column

    #calculating year-to-date YTD exports
    df_monthly_sum['Exports_YTD'] = df_monthly_sum.groupby(['Fiscal Year'])['Exports_US$'].cumsum()
    df_monthly_sum['pct_change_yoy'] = df_monthly_sum.groupby(['month'])['Exports_YTD'].pct_change()*100


    #filtering data of fiscal year 2021-22
    df_2021_22 = df_monthly_sum.loc[df_monthly_sum['Fiscal Year'].isin(['2021-2022'])]
    #filtering data of fiscal year 2020-21
    df_2020_21 = df_monthly_sum.loc[df_monthly_sum['Fiscal Year'].isin(['2020-2021'])]

    
    #######################################
    ######################################

    ########################################
    #Year to date chart of fiscal year
    #########################################

    fig_ytd = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.01, 
                        row_heights=[0.20,0.80])
    #fig_ytd = go.Figure()
    #fig_ytd = make_subplots(specs=[[{'secondary_y': True}]], rows=1, cols=1) # to make subplot with 1 row and 1 col

    # Add traces
    fig_ytd.add_trace(go.Bar(x=df_2020_21['month'], y=df_2020_21['Exports_YTD'],
                        name='Exports in 2020-21', 
                        text=df_2020_21['Exports_YTD'],
                        textposition='auto',
                        texttemplate='%{text:,}',
                        hovertemplate='Exports to date: %{y}'
                        ), row=2, col=1)
    fig_ytd.add_trace(go.Scatter(x=df_2021_22['month'], y=df_2021_22['Exports_YTD'],
                        mode='markers+lines+text',
                        marker=dict(size=16, color="Green"), 
                        name='Exports in 2021-22',
                        text=df_2021_22['Exports_YTD'],
                        textposition='top center',
                        texttemplate="%{text:,}",
                        line=dict(color='Green', width=4),
                        hovertemplate='Exports to date: %{y}B'
                        ), row=2, col=1)


    fig_ytd.add_trace(go.Scatter(x=df_2021_22['month'], 
                            y=df_2021_22['pct_change_yoy'], 
                            mode="lines+markers+text", 
                            marker=dict(size=16, color="Red"), 
                            name="%Change from previous year", 
                            text=df_2021_22['pct_change_yoy'],
                            textposition='middle right',
                            texttemplate="%{text:.2s}%",
                            line=dict(color='Red', width=1, dash='dash'),
                            hovertemplate='%{y}',
                            ), row=1, col=1 )
    image = Image.open('logo.png')                    
    fig_ytd.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=-0.2,  #image postion on chart
            sizex=0.1, sizey=0.1, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    fig_ytd.update_layout(
        autosize=True, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=110, l=90, r=40),
        title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
        xaxis_title='', yaxis_title="",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
    )
    #updates axes
    fig_ytd.update_xaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_yaxes(visible=False, row=1, col=1 ) #range=[0, 100] if need to set y-axis range

    fig_ytd.update_yaxes(showline=True, linewidth=2, linecolor='black', row=2, col=1 )
    fig_ytd.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
    fig_ytd.update_yaxes(title='Cumulative Exports (US$ Billion)', title_font=dict(family='Roboto', color='black', size=20), row=2, col=1)
    fig_ytd.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    ###############
    #title
    fig_ytd.add_annotation(
                text="Total Textile Exports from Pakistan",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="paper", yref="paper",
                x=0, y=1.18, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig_ytd.add_annotation(
                text="current year vs. previous year",
                font=dict(family='roboto', color='black', size=24), 
                xref="paper", yref="paper",
                x=0, y=1.10, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig_ytd.add_annotation(
                text="Source: Pakistan Bureau of Statistics",
                font=dict(family='Fjalla one', color='#758D99', size=20), 
                xref="paper", yref="paper",
                x=0, y=-0.2, 
                showarrow=False,
                arrowhead=1)

    fig_ytd.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    st.plotly_chart(fig_ytd, use_container_width=True) # to show Figure; container width true makes fig. size responsive

#################################
###############################
#summary of current year

    #adding 'Fiscal Year' columns
    df['Fiscal Year'] = df['date'].dt.to_period('Q-JUN').dt.qyear.apply(lambda x: str(x-1) + "-" + str(x))
    #adding month column
    df['month'] = df['date'].dt.strftime('%b') #creating month names column

    #calculating year-to-date YTD exports
    df = df.groupby(['Fiscal Year', 'category'])['Exports_US$'].sum().reset_index()
    

    df['pct_change_yoy'] = df.groupby(['category'])['Exports_US$'].pct_change()*100
    

    #filtering data of fiscal year 2021-22
    df_2021_22 = df.loc[df['Fiscal Year'].isin(['2021-2022'])]
    #filtering data of fiscal year 2020-21
    df_2020_21 = df.loc[df['Fiscal Year'].isin(['2020-2021'])]

    fig = go.Figure()
    # fig = make_subplots(rows=1, cols=1) # to make subplot with 1 row and 1 col
    fig.add_trace(go.Bar(x=df_2021_22['Exports_US$'],
                            y=df_2021_22['category'],
                            text=df_2021_22['Exports_US$'],
                            textposition='auto',
                            texttemplate='$%{text:,}',
                            hovertemplate='%{x}',
                            name='Exports US$',
                            orientation='h', 
                        ))

    fig.update_layout(
        autosize=True, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=80, l=90, r=40),
        title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
        xaxis_title='', yaxis_title="",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
    )
    #updates axes
    fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black')
    fig.update_xaxes(title='Exports in US$ Billion', title_font=dict(family='Roboto', color='black', size=20))
    fig.update_yaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=20))
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    fig.update_yaxes({'categoryorder':'total ascending'})

    ###############
    #title
    fig.add_annotation(
                text="Category-wise Textile Exports from Pakistan",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="paper", yref="paper",
                x=-0.1, y=1.18, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig.add_annotation(
                text="current financial year to date",
                font=dict(family='roboto', color='black', size=24), 
                xref="paper", yref="paper",
                x=-0.1, y=1.09, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig.add_annotation(
                text="Source: Pakistan Bureau of Statistics",
                font=dict(family='Fjalla one', color='#758D99', size=20), 
                xref="paper", yref="paper",
                x=-0.1, y=-0.15, 
                showarrow=False,
                arrowhead=1)

    image = Image.open('logo.png')                    
    fig.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=-0.15,  #image postion on chart
            sizex=0.1, sizey=0.1, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive

    #########################
    # 2020-21

    fig = go.Figure()
    # fig = make_subplots(rows=1, cols=1) # to make subplot with 1 row and 1 col
    fig.add_trace(go.Bar(x=df_2020_21['Exports_US$'],
                            y=df_2020_21['category'],
                            text=df_2020_21['Exports_US$'],
                            textposition='auto',
                            texttemplate='$%{text:,}',
                            hovertemplate='%{x}',
                            name='Exports US$',
                            orientation='h', 
                        ))

    fig.update_layout(
        autosize=True, height=650, width=1050,
        legend_traceorder="reversed",
        margin=dict(t=90, b=80, l=90, r=40),
        title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
        xaxis_title='', yaxis_title="",
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
    )
    #updates axes
    fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black')
    fig.update_xaxes(title='Exports in US$ Billion', title_font=dict(family='Roboto', color='black', size=20))
    fig.update_yaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=20))
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
    fig.update_yaxes({'categoryorder':'total ascending'})

    ###############
    #title
    fig.add_annotation(
                text="Category-wise Textile Exports from Pakistan",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="paper", yref="paper",
                x=-0.1, y=1.18, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig.add_annotation(
                text="Financial year 2020-21",
                font=dict(family='roboto', color='black', size=24), 
                xref="paper", yref="paper",
                x=-0.1, y=1.09, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig.add_annotation(
                text="Source: Pakistan Bureau of Statistics",
                font=dict(family='Fjalla one', color='#758D99', size=20), 
                xref="paper", yref="paper",
                x=-0.1, y=-0.15, 
                showarrow=False,
                arrowhead=1)

    image = Image.open('logo.png')                    
    fig.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=1, y=-0.15,  #image postion on chart
            sizex=0.1, sizey=0.1, #image size on chart
            xanchor="right", yanchor="bottom"
        ))

    st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive

    ####################################
    # pie chart
        ## creating df containing only yearly aggregate of exports
    
    df_yearly = df.groupby(['Fiscal Year']).agg(**{'Exports_US$_sum': ('Exports_US$', 'sum')}).reset_index()
    #groupby year, then category



    # setting first name as index column
    df_yearly.set_index("Fiscal Year", inplace = True)
    #getting exact value of exports in each year
    exports_2020_21=df_yearly.loc['2020-2021']['Exports_US$_sum']
    exports_2021_22=df_yearly.loc['2021-2022']['Exports_US$_sum']
    import plotly.express as px 

    fig = px.pie(df_2020_21, values='Exports_US$', 
                        names='category', 
                        color='category',
                        labels={"category":"Category"},
                        hole=0.7, 
                        template='plotly'
                        )

    fig.update_traces(textposition='outside', textinfo='value+percent+label',
                            marker=dict(line=dict(color='#111111', width=0.5)), #color and size of lines between slices
                            pull=[0, 0, 0, 0], opacity=1, rotation=170,
                            automargin=True) #increasing value of pull from 0-1 will pull a slice out

    fig.update_layout(
        autosize=True, height=700, width=1100,
        margin=dict(t=90, b=0, l=40, r=20),
        title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
        plot_bgcolor='#ededed',
        paper_bgcolor='#ffffff',
        font=dict(color='#111111', size=16, family="roboto, sans-serif"),    #font of lablels of axises
    )

    #title
    fig.add_annotation(
                text="Pakistan Textile Exports",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="paper", yref="paper",
                x=-0.35, y=1.17, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig.add_annotation(
                text="Financial year 2020-21",
                font=dict(family='roboto', color='black', size=24), 
                xref="paper", yref="paper",
                x=-0.35, y=1.09, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig.add_annotation(
                text="Source: Pakistan Bureau of Statistics",
                font=dict(family='Fjalla one', color='#758D99', size=20), 
                xref="paper", yref="paper",
                x=1.3, y=-0.2, 
                showarrow=False,
                arrowhead=1)

    image = Image.open('logo.png')                    
    fig.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=-0.2, y=-0.2,  #image postion on chart
            sizex=0.15, sizey=0.15, #image size on chart
            xanchor="right", yanchor="bottom"
        ))
    fig.add_annotation( #number = str("{:,}".format(number)) , to fomat with comma separator
                text="Total: $" + str("{:,}".format(exports_2020_21)), #variable value is printed inside piechart only as string
                font=dict(color='#111111', size=36, family="roboto, sans-serif"),
                showarrow=False,
                arrowhead=1)

    fig.update_layout(legend=dict(
    yanchor="top",
    y=0.6,
    xanchor="left",
    x=1
    ))

    st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive
######################

    fig = px.pie(df_2021_22, values='Exports_US$', 
                        names='category', 
                        color='category',
                        labels={"category":"Category"},
                        hole=0.7, 
                        template='plotly'
                        )

    fig.update_traces(textposition='outside', textinfo='value+percent+label',
                            marker=dict(line=dict(color='#111111', width=0.5)), #color and size of lines between slices
                            pull=[0, 0, 0, 0], opacity=1, rotation=170,
                            automargin=True) #increasing value of pull from 0-1 will pull a slice out

    fig.update_layout(
        autosize=True, height=700, width=1100,
        margin=dict(t=90, b=0, l=40, r=20),
        title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
        plot_bgcolor='#ededed',
        paper_bgcolor='#ffffff',
        font=dict(color='#111111', size=16, family="roboto, sans-serif"),    #font of lablels of axises
    )

    #title
    fig.add_annotation(
                text="Pakistan Textile Exports",
                font=dict(family='Fjalla one', color='#006BA2', size=36), 
                xref="paper", yref="paper",
                x=-0.35, y=1.17, 
                showarrow=False,
                arrowhead=1)

    #subtitle
    fig.add_annotation(
                text="Financial year 2021-22 to date",
                font=dict(family='roboto', color='black', size=24), 
                xref="paper", yref="paper",
                x=-0.35, y=1.09, 
                showarrow=False,
                arrowhead=1)
    #data reference
    fig.add_annotation(
                text="Source: Pakistan Bureau of Statistics",
                font=dict(family='Fjalla one', color='#758D99', size=20), 
                xref="paper", yref="paper",
                x=1.3, y=-0.2, 
                showarrow=False,
                arrowhead=1)

    image = Image.open('logo.png')                    
    fig.add_layout_image(
        dict(
            source=image,
            xref="paper", yref="paper",
            x=-0.2, y=-0.2,  #image postion on chart
            sizex=0.15, sizey=0.15, #image size on chart
            xanchor="right", yanchor="bottom"
        ))
    fig.add_annotation( #number = str("{:,}".format(number)) , to fomat with comma separator
                text="Total: $" + str("{:,}".format(exports_2021_22)), #variable value is printed inside piechart only as string
                font=dict(color='#111111', size=36, family="roboto, sans-serif"),
                showarrow=False,
                arrowhead=1)

    fig.update_layout(legend=dict(
    yanchor="top",
    y=0.6,
    xanchor="left",
    x=1
    ))

    #st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive