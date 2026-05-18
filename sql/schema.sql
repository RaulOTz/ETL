CREATE TABLE IF NOT EXISTS btc_prices (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(20),
    price NUMERIC,
    fetched_at TIMESTAMP
);
