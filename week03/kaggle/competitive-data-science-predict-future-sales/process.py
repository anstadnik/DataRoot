# # Import libraries
import pandas as pd
%matplotlib


# # Load data
train = pd.read_csv('./data/sales_train.csv')
item_categories = pd.read_csv('./data/item_categories.csv')
items = pd.read_csv('./data/items.csv')
shops = pd.read_csv('./data/shops.csv')
test = pd.read_csv('./data/test.csv')

# # Look at data
print('Train columns:')
print(train.columns, end='\n\n')
print('Item_categories columns:')
print(item_categories.columns, end='\n\n')
print('Items columns:')
print(items.columns, end='\n\n')
print('Shops columns:')
print(shops.columns, end='\n\n')
print('Test columns:')
print(test.columns, end='\n\n')

# # Remove things that appears only in one set
test_shops = test.shop_id.unique()
train = train[train.shop_id.isin(test_shops)]
test_items = test.item_id.unique()
train = train[train.item_id.isin(test_items)]

##

# train['date'] = pd.to_datetime(train['date'].head())
# print(train['date'].describe())
# #
# print(test.head())
# print(train.head())
# # End
