create table if not exists violins.violins_data (
    name text,
    price FLOAT,
    average_rating FLOAT,
    number_of_reviews FLOAT,        
    stock FLOAT,
    description text,         
    image text,         
    category text,         
    date TIMESTAMP default CURRENT_TIMESTAMP
);