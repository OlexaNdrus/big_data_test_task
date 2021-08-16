import pandas as pd
import numpy as np


products_csv = 'test-task_dataset_summer_products.csv'

def main_body(csv_file):
    products_df = pd.read_csv(csv_file)
    products_df = products_df[['price', 'rating_five_count', 'rating_count', 'origin_country']]
    products_df.replace(r'^\s*$', np.nan, regex=True)

    agg_df = products_df.groupby(
        products_df['origin_country'].fillna('empty')).\
        agg({'price': 'mean', 'rating_five_count':'sum', 'rating_count':'sum'}). \
        reset_index().\
        replace({'origin_country': {'empty': np.nan}})

    agg_df['five_percentage'] = (agg_df['rating_five_count'] / agg_df['rating_count'] * 100).fillna(0).round(2)

    agg_df.to_csv(path_or_buf='result.csv', index=False)
    return agg_df

if __name__ == '__main__':
    print(main_body(products_csv))
