import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px





st.set_page_config(
    layout='wide',
    page_icon='❤️',
    page_title='Pokemon Dashboard'
)




@st.cache_data
def load_data():
    file= 'Pokemon.csv'
    data= pd.read_csv(file)
    return data

def main():

    st.markdown('''
           <style>
                .stApp{
                    background-color: #111;
                }
                </style>
                
                
                
                ''',unsafe_allow_html=True)
    
    st.image('WhatsApp Image 2024-09-09 at 19.56.27_70903aee.jpg', use_column_width=True)
    st.title('Pokemon Dashboard')
    with st.spinner('Loading Pokemons...'):
        df= load_data()
        st.snow()
        st.balloons()

    rows,columns=df.shape
    col_names=df.columns.tolist()

    c1,c2,c3= st.columns(3)
    c1.subheader(f'Total Rows:{rows}')
    c2.subheader(f'Total Columns :{columns}')
    c3.subheader(f'columns:{','.join(col_names)}')

if __name__ =='__main__':
    main()