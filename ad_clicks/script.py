import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
# Examine the first 10 rows of ad_clicks
#print(ad_clicks.head(10))
# Discover how many views came from each utm_source
#print(ad_clicks.groupby('utm_source').user_id.count().reset_index())

# Create a new column called is_click, which is True if ad_click_timestamp is not null and False otherwise.
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
#print(ad_clicks)

# Get the number of clicked ads by utm_source and display them in a pivot table
click_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
clicks_pivot = click_by_source.pivot(
  columns='is_click',
  index='utm_source',
  values='user_id'
).reset_index()

# Get the percentage of users who clicked on the ads from each utm_source
clicks_pivot['percent_clicked'] = clicks_pivot[True]/(clicks_pivot[True] + clicks_pivot[False])

# Checking if the same amount of people were submited to test A and Test B
AB_testing = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
#print(AB_testing)

# Checking if a greater percentage of users clicked on Ad A or Ad B
distribution = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

distribution_pivot = distribution.pivot(
	columns='is_click',
  index='experimental_group',
  values='user_id'
).reset_index()
distribution_pivot['percentage_clicked'] = distribution_pivot[True]/(distribution_pivot[True] + distribution_pivot[False])
#print(distribution_pivot)

# Calculate the percentage of users who clicked on the ad by day for each group(A or B)
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

a_clicks = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
a_clicks_pivot = a_clicks.pivot(
  columns='is_click',
  index='day',
  values='user_id'
)
a_clicks_pivot['percentage_clicked'] = a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False])
print(a_clicks_pivot)
b_clicks = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
b_clicks_pivot = b_clicks.pivot(
  columns='is_click',
  index='day',
  values='user_id'
)
b_clicks_pivot['percentage_clicked'] = b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False])
print(b_clicks_pivot)
