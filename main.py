def run_etl(imdb_list_path, imdb_reviews_path):
    imdb_list = extract_csv(imdb_list_path)
    imdb_reviews = clean_columns(extract_csv(imdb_reviews_path, drop_index=False))

    df_joined = imdb_reviews.merge(imdb_list, left_on='imdb_id', right_on='id', how='inner')
    fact_review = generate_fact_review(df_joined.copy())
    dim_movie = generate_dim_movie(df_joined.copy())
    dim_genre, movie_genre_map = generate_genre_tables(imdb_list.copy())
    dim_yearly_summary = generate_dim_yearly_summary(df_joined.copy())

    return dim_movie, fact_review, dim_genre, movie_genre_map, dim_yearly_summary

if __name__ == "__main__":
    # Sample execution paths
    list_path = "data/raw/imdb_list.csv"
    reviews_path = "data/raw/imdb_reviews.csv"
    results = run_etl(list_path, reviews_path)
    print("ETL complete.")


