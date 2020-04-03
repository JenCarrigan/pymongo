from pymongo import MongoClient

# setup the mongo connection
client = MongoClient()

# get the db and the collection we'll be working with
db = client.python
collection = db.products

def get_all_products():
  docs = collection.find({})

  for doc in docs:
    print(doc)

def get_product_by_name(name):
  doc = collection.find_one({"name": name})
  print(doc)

def get_products_by_price(price):
  docs = collection.find({"price": price})

  for doc in docs:
    print(doc)

def post_product(product):
  productId = collection.insert_one(product).inserted_id
  print(f"{product} has been inserted with ID of {productId}")

def delete_product(name):
  collection.delete_one({"name": name})
  print(f"deleted {name}")

