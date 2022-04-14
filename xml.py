from bs4 import BeautifulSoup
# reading data in items.xml
with open('items.xml', 'r') as f:
    data = f.read()
# passing data inside the beautifulsoup parser
bs_data = BeautifulSoup(data, "xml")
# finding all instances of tag item
bs_item = bs_data.find_all('item')
print(bs_item)

# using find() to get a tag with specified attribute
bs_name = bs_data.find('item', {'name':'item1'})
print(bs_name)

# extracting the text stored in a tag
text = bs_name.get_text()
print(text)

# extracting the data stored in a specific attribute of a tag
value = bs_name.get('price')
print(value)