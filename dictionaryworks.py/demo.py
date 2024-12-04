product={"id":100, "title":"iphone","price":100000,"brand":"apple"}

product["price"]=50000

product["warrenty"]="yes"


if "offer" in product:

    product["offer"]=10

else:

    product["offer"]=20

print(product)

# print(product["id"])
# print(product["brand"])
# print(product[  "price"])
# print(product["title"])