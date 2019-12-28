import codecademylib
import pandas as pd

# Load the data into a dataframe
inventory = pd.read_csv('inventory.csv')

# Select the first ten rows belonging to Staten Island
staten_island = inventory.head(10)

# Select the products that are sold at Staten Island
product_request = staten_island['product_description']

# Select all rows where location is equal to Brooklyn and product_type is equal to seeds
seed_request = inventory[(inventory.location == 'Brooklyn') &
                         (inventory.product_type == 'seeds')]
# Add a column callled inventory which is true if quantity is greater than 0 and False ortherwise
inventory['in_stock'] = inventory.apply(lambda
                                    row: True if row.quantity > 0 else False, axis = 1)

# Create a column called total_value that is equal to price multiplied by quantity
inventory['total_value'] = inventory.apply(lambda
                                        row: row.quantity * row.price,
                                        axis = 1)


#  Create a new column in inventory called full_description
combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)
inventory['full_description'] = inventory.apply(combine_lambda, axis = 1)
print(inventory.head(10))
