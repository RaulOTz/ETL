from datetime import datetime
def transform_data(data):
    transformed_data = {
        "symbol": data["symbol"],
        "price": data["price"],
        "fetched_at": datetime.now()
    }

    return transformed_data