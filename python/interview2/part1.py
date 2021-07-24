import requests
import openpyxl

ENDPOINT_CURRENCY = 'https://***'
ENDPOINT_REFRESH_TOKEN = 'https://***'
CLIENT_ID = '****************************************************************'

refresh_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyNzMwNTA4NywianRp" \
    "IjoiNjk3MGMyOTJlMzE0NDM3MGI5YzUxNjEyNzM0NjIyNTYiLCJ1c2VyX2lkIjoyOX0.2VvVzo12u0nDyiZNKZGON982jZ8GA4Vu08NCBQplEW0"


# реквест для обновления токена доступа
def request_access_token(data, headers):
    r = requests.post(ENDPOINT_REFRESH_TOKEN, data=data, headers=headers)
    return r.json()["access"]


# реквест в ендпоинт с данными валют
def request_currency_data(headers):
    r = requests.get(ENDPOINT_CURRENCY, headers=headers)
    return r.json()["results"]


def generate_xlsx_file(data):
    xlsx = openpyxl.Workbook()
    sheet = xlsx.active

    # добавляем заголовок
    sheet_data = [list(data[0].keys())]

    # добавляем данные
    for row in data:
        sheet_data.append(list(row.values()))

    # пишем в файл
    for row in sheet_data:
        sheet.append(row)
    xlsx.save('currency_data.xlsx')
    xlsx.close()


# обновляем токен, отправляем реквест за данными валют, генерируем файл
access_token = request_access_token({'refresh': refresh_token}, {'Client-ID': CLIENT_ID})
currency_data = request_currency_data({'Authorization': 'Bearer ' + access_token, 'Client-ID': CLIENT_ID})
generate_xlsx_file(currency_data)

