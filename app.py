import streamlit as st 
from tematy import ruch 

st.set_page_config(page_title='fizyka',page_icon='🚗')

st.title('Fizyka-projekt edukacyjny')

wybrany_temat=st.sidebar.selectbox(
    'Wybierz temat',
    ['Ruch cial']
)

if wybrany_temat =='Ruch cial':
    ruch.pokaz()

