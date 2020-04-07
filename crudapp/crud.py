from db_actions import get_all_products, get_product_by_name, get_products_by_price, delete_product, post_product

def print_table_of_contents():
  print("""
  Please select an option (1-5) below to get started:
  1. See all products
  2. Find product by name
  3. List products at certain price
  4. Insert a product
  5. Delete a product
  """)

print_table_of_contents()
selection = 0

while True:
  try:
    selection = int(input())
  except ValueError:
    print('Invalid selection!')
    print_table_of_contents()
  else:
    if 1 <= selection <= 5:
      break
    else:
      print('Invalid selection!')
      print_table_of_contents()

if selection == 1:
  docs = get_all_products()

  for doc in docs:
    print(doc)

elif selection == 2:
  print('Enter the name of the product')
  name_to_try = str(input())

  doc = get_product_by_name(name_to_try)
  print(doc)

elif selection == 3:
  print('Enter the price you want to search')
  price_to_try = float(input())

  doc = get_products_by_price(price_to_try)
  print(doc)

elif selection == 4:
  print('Please input the product to add')
  product_to_add = str(input())

  response = post_product(product_to_add)
  print(response)

elif selection == 5:
  print('Please input the name of the product to delete')
  product_to_delete = str(input())

  response = delete_product(product_to_delete)
  print(response)