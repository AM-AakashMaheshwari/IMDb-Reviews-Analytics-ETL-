
def map_sentiment(rating):
    if pd.isna(rating):
        return 'Neutral'
    elif rating >= 7:
        return 'Positive'
    elif rating <= 4:
        return 'Negative'
    else:
        return 'Neutral'

def generate_fact_review(df):
    df['sentiment_category'] = df['review_rating'].apply(map_sentiment)
    df['review_word_count'] = df['review'].str.split().str.len()
    df['review_title_word_count'] = df['review_title'].str.split().str.len()
    return df[[
        'imdb_id', 'review_title', 'review_rating', 'review',
        'review_word_count', 'review_title_word_count', 'sentiment_category'
    ]].rename(columns={'imdb_id': 'movie_id'})

def generate_dim_movie(df):
    movie_agg = df.groupby(['id', 'title', 'rating', 'year'], as_index=False).agg(
        review_count=('review_rating', 'count'),
        avg_review_rating=('review_rating', 'mean'),
        avg_review_length=('review_word_count', 'mean')
    )
    movie_agg['rating_gap'] = movie_agg['avg_review_rating'] - movie_agg['rating']
    return movie_agg.rename(columns={
        'id': 'movie_id',
        'rating': 'imdb_rating',
        'year': 'release_year'
    })

def generate_genre_tables(imdb_list):
    genre_df = imdb_list[['id', 'genre']].copy()
    genre_df['genre'] = genre_df['genre'].str.split(', ')
    genre_exploded = genre_df.explode('genre').rename(columns={'id': 'movie_id', 'genre': 'genre_name'})
    dim_genre = pd.DataFrame(genre_exploded['genre_name'].unique(), columns=['genre_name']).reset_index()
    dim_genre = dim_genre.rename(columns={'index': 'genre_id'})
    movie_genre_map = genre_exploded.merge(dim_genre, on='genre_name')[['movie_id', 'genre_id']]
    return dim_genre, movie_genre_map

def generate_dim_yearly_summary(df):
    yearly = df.groupby('year', as_index=False).agg(
        movie_count=('id', 'nunique'),
        avg_imdb_rating=('rating', 'mean'),
        avg_user_rating=('review_rating', 'mean')
    )
    sentiments = df.groupby(['year', 'sentiment_category']).size().unstack(fill_value=0).reset_index()
    return yearly.merge(sentiments, on='year', how='left')
    



