import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
keys = ServiceAccountCredentials.from_json_keyfile_name("keys.json", scope)
client = gspread.authorize(keys)


# Sales Target
sheet = client.open("dwm").worksheet("Sales Target")  # Open the spreadhseet
item_type = sheet.col_values(2)
month = sheet.col_values(1)
target = sheet.col_values(3)

item_type = item_type[1:]
month = month[1:]
target = target[1:]

for i in range(0, len(month), 1):
    month[i] = month[i][3:]

for i in range(0, len(target), 1):
    target[i] = int(int(target[i])/10)


# Order details
sheet = client.open("dwm").worksheet("Order details")
amount = sheet.col_values(2)
profit = sheet.col_values(3)
cat = sheet.col_values(5)
quant = sheet.col_values(4)
order = sheet.col_values(1)
order = order[1:]
amount = amount[1:]


profit = profit[1:]

cat = cat[1:]
quant = quant[1:]
for i in range(len(quant)):
    quant[i] = int(quant[i])
for i in range(len(order)):
    order[i] = order[i][2:]
    order[i] = int(order[i]) - 25601


# List of order details
sheet = client.open("dwm").worksheet("List of Orders")
date = sheet.col_values(2)
date = date[1:]
state = sheet.col_values(4)
state = state[1:]
ord = sheet.col_values(1)
ord = ord[1:]
for i in range(len(ord)):
    ord[i] = ord[i][2:]
    ord[i] = int(ord[i])-25601
