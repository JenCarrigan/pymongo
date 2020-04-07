from pymongo import MongoClient
import json

# setup the mongo connection
client = MongoClient()

# get the db and the collection we'll be working with
db = client.python
collection = db.products

def get_all_products():
  # docs = list(collection.find({}))
  docs = collection.find({})

  # regular way with for loop to remove ids
  # go through each document object
  # go through each item object
  # don't return id information

  # list_ = []
  # for doc in docs:
  #   for key, val in doc.items():
  #     if key != '_id':
  #       lst.append({key: val})
  # return list_

  # with list comprehension
  return [{key: val for key, val in doc.items() if key != '_id'} for doc in docs]

def get_product_by_name(name):
  doc = collection.find_one({"name": name})

  if doc != None:
    # dictionary comprehension
    return {key: val for key, val in doc.items() if key != '_id'}
  else:
    return 'A product with that name does not exist.'

def get_products_by_price(price):
  docs = collection.find({"price": price})

  if docs != None:
    return [{key: val for key, val in doc.items() if key != '_id'} for doc in docs]
  else:
    return 'No products with that price exist.'

def post_product(product):
  print(product)
  p = json.loads(product)

  productId = collection.insert_one(p).inserted_id
  return 'Product has been put in database.'

def delete_product(name):
  collection.delete_one({"name": name})
  return 'The product has been deleted.'

