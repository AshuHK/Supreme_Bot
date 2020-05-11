import datetime 

INTRO = """This is a Supreme bot that may or may not work. Little testing has 
been done to check if this will not be caught by Supreme's bot
detection. DO NOT USE THIS FOR PURCHASING AS YOU MAY BE BANNED FOR 
USING THIS SOFTWARE. 
Contact AshuK650 on Github for any concerns with this code"""

file_obj = open("keys.txt") 
print(INTRO)
product_url = str(input("Copy and Paste Product URL: "))

if "https://www." not in product_url: 
    product_url = "https://www." + product_url

current_datetime = datetime.datetime.now() 

keys = {} 
keys["product_url"] = product_url

for line in file_obj: 
    line_list = line.split(":")
    keys[line_list[0].strip()] = line_list[1].strip()
    
    if line_list[0] == "exp_year": 
        card_year = int(line_list[1]) 
        card_year -= current_datetime.year
        
        keys[line_list[0].strip()] = card_year + 1 

