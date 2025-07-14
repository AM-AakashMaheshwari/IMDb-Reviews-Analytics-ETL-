import pandas as pd

#reading movies from imdb movie files
# def read_movie_list():
#     movies_list_df= pd.read_csv("Data/raw/imdb_list.csv")
#     return movies_list_df



# #reading reviews from imdb movie reviews file into a dataframe
# def read_review_list():
#     movies_review_list_df= pd.read_csv("Data/raw/imdb_reviews.csv")
#     return movies_review_list_df


def extract_csv(path, drop_index=True):
    df = pd.read_csv(path)
    if drop_index and 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
    return df

def clean_columns(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df
