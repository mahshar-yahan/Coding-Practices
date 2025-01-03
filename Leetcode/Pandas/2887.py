import pandas as pd

data = {
    "name": ["Product A", "Product B", "Product C", "Product D"],
    "quantity": [10, None, 5, None],
    "price": [100, 200, 150, 250]
}

products = pd.DataFrame(data)

products["quantity"] = products["quantity"].fillna(0)

products["quantity"] = products["quantity"].astype(int)

print(products)