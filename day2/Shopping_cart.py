
#Sorting

Products=[
			{"pid":101,"name":"MacBook4","cost":100000,"brand":"Apple","category":"Electronics","rating":4.5,"discount":40},
			{"pid":102,"name":"ZenBook2","cost":70000,"brand":"ASUS","category":"Electronics","rating":4.4,"discount":20},
			{"pid":103,"name":"EliteBook","cost":90000,"brand":"HP","category":"Electronics","rating":4.2,"discount":20},
			{"pid":104,"name":"ThinkPad3","cost":75000,"brand":"Lenovo","category":"Electronics","rating":4.1,"discount":10},
			{"pid":105,"name":"LatitudeU","cost":50000,"brand":"Toshiba","category":"Electronics","rating":3.9,"discount":0},
			{"pid":201,"name":"Blue CropTop","cost":1000,"brand":"Global Desi","category":"Clothing","rating":4.2,"discount":20},
			{"pid":202,"name":"Orange Kurta","cost":1299,"brand":"Haute Curry","category":"Clothing","rating":4.1,"discount":30},
			{"pid":203,"name":"Blue Jeggings","cost":899,"brand":"HRX","category":"Clothing","rating":4.1,"discount":15},
			{"pid":204,"name":"Brown Leather Jacket","cost":4999,"brand":"Zara","category":"Clothing","rating":4.7,"discount":50},
			{"pid":301,"name":"IWatch series4","cost":50000,"brand":"Apple","category":"Watches","rating":4.6,"discount":25},
			{"pid":302,"name":"Digital Wseries2","cost":4000,"brand":"Gshock","category":"Watches","rating":3.8,"discount":15},
			{"pid":303,"name":"Gentleman Series","cost":30000,"brand":"Daniel Wellington","category":"Watches","rating":4.9,"discount":35}
		]



print("1.SortbyCost Low to High")
print("2.SortbyCost High To Low")
print("3.SortbyRating")
print("4.SortbyDisount High to Low")
print("5.SortbyDiscount Low to High")

dict1={
    "1":["cost",False],
    "2":["cost",True],
    "3":["rating",False],
    "4":["discount",True],
    "5":["discount",False]
}

choice=(input("Enter Choice"))
Sortby=lambda element: element[dict1[choice][0]]
Products.sort(key=Sortby,reverse=dict1[choice][1])

print("Sorted!")
for i in Products:
	print(i['name'])




#Filtering


product = [
			{"pid":101,"name":"MacBook4","cost":100000,"brand":"Apple","category":"Electronics","rating":4.5,"discount":40},
			{"pid":102,"name":"ZenBook2","cost":70000,"brand":"ASUS","category":"Electronics","rating":4.4,"discount":20},
			{"pid":103,"name":"EliteBook","cost":90000,"brand":"HP","category":"Electronics","rating":4.2,"discount":20},
			{"pid":104,"name":"ThinkPad3","cost":75000,"brand":"Lenovo","category":"Electronics","rating":4.1,"discount":10},
			{"pid":105,"name":"LatitudeU","cost":50000,"brand":"Toshiba","category":"Electronics","rating":3.9,"discount":0},
			{"pid":201,"name":"Blue CropTop","cost":1000,"brand":"Global Desi","category":"Clothing","rating":4.2,"discount":20},
			{"pid":202,"name":"Orange Kurta","cost":1299,"brand":"Haute Curry","category":"Clothing","rating":4.1,"discount":30},
			{"pid":203,"name":"Blue Jeggings","cost":899,"brand":"HRX","category":"Clothing","rating":4.1,"discount":15},
			{"pid":204,"name":"Brown Leather Jacket","cost":4999,"brand":"Zara","category":"Clothing","rating":4.7,"discount":50},
			{"pid":301,"name":"IWatch series4","cost":50000,"brand":"Apple","category":"Watches","rating":4.6,"discount":25},
			{"pid":302,"name":"Digital Wseries2","cost":4000,"brand":"Gshock","category":"Watches","rating":3.8,"discount":15},
			{"pid":303,"name":"Gentleman Series","cost":30000,"brand":"Daniel Wellington","category":"Watches","rating":4.9,"discount":35}
]


def myfilter(key, value):
    return filter(lambda el: el[key] == value, product)


keys = {
    1: "category",
    2: "name",
    3: "brand"
}

values = {
    1: ("Electronics", "Clothes", "Watches"),
    2: ("MacBook4", "Blue CropTop", "Digital Wseries2", "Blue Jeggings"),
    3: ("HP", "Haute Curry", "Apple", "Daniel Wellington", "ASUS")
}

print("""Enter Filter Option - 
1: Category
2: Name
3: Brand """)
c1 = int(input())
print("Enter Filter Option - ")

index = 1  # for serial number of next loop

for i in values[c1]:
    print(index, i)
    index += 1

c2 = int(input())
key1 = keys[c1]
value1 = values[c1][c2 - 1]
# print(key1, value1) for checking purpose
demo = myfilter(key1, value1)
for i in list(demo):
    print("Id {pid}".format(**i))
    print("Name {name}".format(**i))
    print("Cost {cost}".format(**i))
    print("Brand {brand}".format(**i))
    print("Category {category}".format(**i))
    print("Rating {rating}".format(**i))
    print("Discount {discount}".format(**i))
    print("-----------")




