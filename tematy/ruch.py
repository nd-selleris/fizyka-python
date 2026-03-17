import streamlit as st
from silnik.obliczenia import oblicz_predkosc_srednia, oblicz_droge 


def pokaz():
    st.header('Ruch cial')
    st.write('Ruch jednostajny i niejednostajny')

    st.markdown('### Wzor')
    st.latex(r'v = \frac{s}{t}')

    droga = st.number_input('Droga(km)', min_value=0.0, value=100.0, step=10.0)
    czas=st.number_input('Czas (h)', min_value=0.1, value=2.0, step=0.5)

    if st.button('Oblicz predkosc srednia'):
        wynik=oblicz_predkosc_srednia(droga,czas)
        st.success(f'Predkosc srednia: {wynik:.2f} km/h')

        st.markdown('### Oblicz droge')
        predkosc = st.number_input('Predkosc (km/h)',min_value=0.0,value=50.0,step=0.5)
        czas2 = st.number_input('Czas ruchu (h)', min_value=0.0, value=2.0,step=0.5,key='czas2')

        if st.button('Oblicz droge'):
            wynik_droga=oblicz_droge(predkosc,czas2)
            st.success(f'Droga: {wynik_droga:.2f} km')
        
        st.markdown('### Przyklad')
    
    st.write('Samochod przejechal 100km w 2 godziny,wiec jego predkosc srednia wynosi 50km/h.')

             