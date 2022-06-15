from soupsieve import select
import streamlit as st
import pickle
import pandas as pd
import requests
import base64

main_bg = "C:\\Users\\Aryan Ahuja\\OneDrive\\Pictures\\Saved Pictures\\light-back.jpg"
main_bg_ext = "jpg"
st.markdown(
    f'''
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
    .sidebar .sidebar-content {{
         background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
    </style>
    ''',
    unsafe_allow_html=True
)
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=016b26fea3df0c34d3471293fafeaa62&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title("Movie Recommender System")
st.caption("You will be recommended with similar movies.")
# with st.form(key='my_form'):
#     username = st.text_input("Movie")

#     st.form_submit_button("Submit")
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key = lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)   
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movie_posters

option = st.selectbox(
     'Select Movie',
     movies['title'].values)

# st.write('You selected:', option)

if st.button('Recommend'):
    names, posters = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])                