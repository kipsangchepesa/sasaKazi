import streamlit as st
import requests


title = st.text_input('Type the name of the movie')
if title:
    try:
        url = f"https://imdb8.p.rapidapi.com/auto-complete/?t=(title)&apikey='3267deb8f0msha76f7bd59b2679dp137579jsn76c993d3d935"
        re = requests.get(url)
        re = re.json()
        col1, col2 = st.columns([1,2])
        with col1:
            st.image(re['Image'])
        with col2:
            st.subheader(re['Title'])
            st.caption(f"Genre: {re['Genre']} Year: {re['Year']}")
            st.write(re['Plot'])
            st.text(f"Rating: {re['imdbRating']}")
            st.progress(float(re['imdbRating'])/10)

    except:
        st.error('There is no movie with such a name')