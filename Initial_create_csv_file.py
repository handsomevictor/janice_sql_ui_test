import os
import pandas as pd

def create_csv_file():
    # create customers.csv
    # customer_id,name,email
    # 1,Victor,victor@example.com
    # 2,Janice,janice@example.com
    # 3,Sana,sana@example.com

    data = {
        'customer_id': [1, 2, 3],
        'name': ['Victor', 'Janice', 'Sana'],
        'email': ['victor@example.com', 'janice@example.com', 'sana@example.com']
    }

    df = pd.DataFrame(data)
    df.to_csv(os.path.join(os.getcwd(), 'database', 'customers.csv'), index=False)

    # orders.csv
    # order_id,customer_id,order_date
    # 1,1,2025-01-01
    # 2,2,2025-01-02
    # 3,3,2025-01-03

    data = {
        'order_id': [1, 2, 3],
        'customer_id': [1, 2, 3],
        'order_date': ['2025-01-01', '2025-01-02', '2025-01-03']
    }

    df = pd.DataFrame(data)
    df.to_csv(os.paths.join(os.getcwd(), 'database', 'orders.csv'), index=False)

    # order_items.csv
    # item_id,order_id,product_name,quantity
    # 1,1,Laptop,1
    # 2,1,Mouse,2
    # 3,2,Keyboard,1
    # 4,3,Monitor,1

    data = {
        'item_id': [1, 2, 3, 4],
        'order_id': [1, 1, 2, 3],
        'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
        'quantity': [1, 2, 1, 1]
    }

    df = pd.DataFrame(data)
    df.to_csv(os.path.join(os.getcwd(), 'database', 'order_items.csv'), index=False)


if __name__ == '__main__':
    create_csv_file()