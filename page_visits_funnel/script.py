import pandas as pd


# Import the dataframes 
visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

# Inspect the columns of each dataframe
# print(visits.head())
# print(carts.head())
# print(checkout.head())
# print(purchase.head())

# Combine visits and cart using a left merge
visits_and_cart = pd.merge(visits, cart, how='left')

# Print the size of the merged dataframe
print('The size of the merged dataframe is {}'.format(len(visits_and_cart)))

# Print the number of null timestamps for the column cart_time
didnt_cart = visits_and_cart[visits_and_cart.cart_time.isnull()]
print(len(didnt_cart))

# Print the percent of users who visited Cool T-Shirts Inc. and ended up not placing a t-shirt in their cart
number_of_visits = len(visits_and_cart.visit_time)
percentage_didnt_cart = len(didnt_cart)/float(number_of_visits)
print(percentage_didnt_cart)

# Print the percent of users who placed a t-shirt in their cart but ended up not making the checkout
cart_and_checkout = pd.merge(cart, checkout, how='left')
didnt_checkout = len(cart_and_checkout[cart_and_checkout.checkout_time.isnull()])
number_of_cart = len(cart_and_checkout.cart_time)
percentage_didnt_checkout = didnt_checkout/float(number_of_cart)
print(percentage_didnt_checkout)

# Merge all four dataframes
all_data = visits.merge(cart, how='left').\
              merge(checkout, how='left').\
							merge(purchase, how='left')

# Print the number of users who made the check out but ended up not buying a t-shirt
didnt_purchased = len(all_data[(~all_data.checkout_time.isnull()) & (all_data.purchase_time.isnull())]
                     )
number_of_checkout = len(all_data[~all_data.checkout_time.isnull()])
percentage_didnt_purchased = didnt_purchased/float(number_of_checkout)
print(percentage_didnt_purchased)


# Which step of the funnel is weakest (i.e., has the highest percentage of users not completing it)?
# ==> step1, because aproximately 81% visited the site but didnt place anything in their cart

# Calculate the average time from initial visit to final purchase
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
print(all_data.time_to_purchase.mean())




