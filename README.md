# Movie_Recommender_System

#### Movie Recommender is a practically applicable program which is used in real life. My python project takes TMDB movie data consisting of almost 5000 movies. The program takes a movie as input which a user likes and recommends 5 closely resembling movies alongwith their posters. 

### I am attaching a screenshot of the final API which runs on my localhost.

![Screenshot (67)](https://user-images.githubusercontent.com/87764530/173776686-98c4fedc-31f5-4593-be62-d1d6a4d6f480.png)


The project was divided into 3 parts:

#### 1. Data Cleaning:
      The TMDB movie database is loaded and cleaned to usable format and redundant features are removed for the processing. 

#### 2. Score Generation
      After the data has been cleaned, we convert it to the form of a tags where each tag is unique and consists all the required features for a single movie. Text 
      Vectorization is applied and tags are converted to numerical format and similarity function is generated.
      
#### 3. Creating API
      Streamlit library is used to create an API, where the final function takes in a movie name and searches for 5 closest vectors. A personalized API key is used to 
      fetch movie poster from the internet using the 'movie_id'. Both movie name and poster are returned. Currently, it is only hosted on my localhost.
