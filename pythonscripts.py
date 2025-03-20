# 1. MOVIES DATASET

import pandas as pd #importing the dataset

df_movies = pd.read_csv("movies.csv") #loading the dataset
df_movies.info() # cheking the dataset and observing what we have to clean 

df_movies = df_movies.drop_duplicates() # for droping the duplicates
df_movies = df_movies.dropna() #removing rows that contain null values

df_movies.to_csv("cleaned_movies.csv", index=False) # Saving cleaned dataset

# Movies dataset cleaned and save







# 2. USERS DATASET
import pandas as pd #importing dataset

df_users = pd.read_csv("users.csv") # Loading dataset


df_users = df_users.drop_duplicates() # Removing duplicates
 
df_users.drop(columns=['email'], inplace=True) # for Droping unnecessary columns

df_users = df_users[(df_users['age'] >= 10) & (df_users['age'] <= 100)] # Remove invalid ages (e.g., negative or unrealistic values)

df_users.to_csv("cleaned_users.csv", index=False) # Saving cleaned dataset

#Users dataset cleaned and saved







# 3. RATINGS DATASET
#cleaning ratings dataset
import pandas as pd #importing pandas library

df_ratings = pd.read_csv("ratings.csv") # Loading dataset


df['review_date'] = pd.to_datetime(df['review_date'], errors='coerce') # Converting 'review_date' to datetime format

df_ratings = df_ratings.drop_duplicates() # Removng duplicates


df_ratings = df_ratings[(df_ratings['rating'] >= 0) & (df_ratings['rating'] <= 10)] # making sure ratings are within valid range (0-10)

df_ratings.to_csv("cleaned_ratings.csv", index=False) # Saving cleaned dataset

#Ratings dataset cleaned and saved//







# 4. WATCH HYSTORY DATASET
import pandas as pd #importing the library

df_watch_history = pd.read_csv("watch_history.csv") # Loading dataset

df_watch_history = df_watch_history.drop_duplicates() # Removing duplicates


df_watch_history = df_watch_history[df_watch_history['watch_duration'] > 0] #We found that there are negative watch hourse which makes no sence so Removing negative watch durations

devices = ["Smartphone", "Laptop", "Tablet", "Smart TV", "Desktop", "Gaming Console"] ## there is invalid device "washing machine" which makes no sense so Removing invalid devices
df_watch_history = df_watch_history[df_watch_history['device_type'].isin(devices)]

df_watch_history.to_csv("cleaned_watch_history.csv", index=False) # Saving cleaned dataset

# Watch history dataset cleaned and saved
# All the required dataset are cleaned 