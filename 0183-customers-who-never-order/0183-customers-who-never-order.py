import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    not_order = [id for id in customers['id'] if id not in list(orders['customerId'])]
    #print(not_order)
    customer_not_order = pd.DataFrame(customers[customers['id'].isin(not_order)]['name'])
    #print(customer_not_order)
    customer_not_order.rename(columns={'name':'Customers'},inplace=True)
    return customer_not_order