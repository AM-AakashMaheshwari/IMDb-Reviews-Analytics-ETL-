def create_table_sql():
    return {
        'dim_movie': """
        CREATE TABLE dim_movie (
            movie_id VARCHAR(20) PRIMARY KEY,
            title VARCHAR(255),
            imdb_rating FLOAT,
            release_year INT,
            review_count INT,
            avg_review_rating FLOAT,
            avg_review_length INT,
            rating_gap FLOAT
        )""",

        'fact_review': """
        CREATE TABLE fact_review (
            review_id INT IDENTITY(1,1) PRIMARY KEY,
            movie_id VARCHAR(20),
            review_title VARCHAR(255),
            review_rating FLOAT,
            review TEXT,
            review_word_count INT,
            review_title_word_count INT,
            sentiment_category VARCHAR(20)
        )""",

        'dim_genre': """
        CREATE TABLE dim_genre (
            genre_id INT PRIMARY KEY,
            genre_name VARCHAR(50)
        )""",

        'movie_genre_map': """
        CREATE TABLE movie_genre_map (
            movie_id VARCHAR(20),
            genre_id INT,
            PRIMARY KEY (movie_id, genre_id)
        )""",

        'dim_yearly_summary': """
        CREATE TABLE dim_yearly_summary (
            release_year INT PRIMARY KEY,
            movie_count INT,
            avg_imdb_rating FLOAT,
            avg_user_rating FLOAT,
            Positive INT,
            Neutral INT,
            Negative INT
        )"""
    }