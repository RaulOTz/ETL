from db import get_connection

def load_data(data):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO btc_prices (
            symbol,
            price,
            fetched_at
        )
        VALUES (%s, %s, %s)
    """

    cursor.execute(
        query, 
        (
            data["symbol"],
            data["price"],
            data["fetched_at"]
        )
    )

    conn.commit()

    cursor.close()
    conn.close()