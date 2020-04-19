import requests
import json
'''
Swagger API call v 0.5
'''
# задали базовый урл
base_url = 'https://petstore.swagger.io/v2'

# получаем информацию о питомце по ид
def pet(petid):
    api_url = f"{base_url}/pet/{petid}"
    r = requests.get(api_url)
    return r
# для обновления информации нам надо послать ИД, имя и статус
def pet_upd(petid, name, status="available"):
    api_url = f"{base_url}/pet/{petid}"
    # словарь с параметрами
    api_data = {
        'petId':petid,
        'name':name,
        'status':status
        }
    r = requests.post(api_url, api_data)
    return r
#создаем новый заказ
def store_order(uid, petid, quantity):
    api_url = f"{base_url}/store/order"
    # словарь с параметрами
    api_data = {
        'id':uid,
        "petId": petid,
        "quantity": quantity,
        "shipDate": "2020-04-08T07:56:05.832Z",
        "status": "placed",
        "complete": "true"
        }
    r = requests.post(api_url, json=api_data)
    #print (r.request.body)
    return r 

#получаем информацию о заказе по id
def order(orderId):
    api_url = f"{base_url}/store/order/{orderId}"
    r = requests.get(api_url)
    return r

# выводим и анализируем результат
def req_info(r):
    try:
        answer = r.json()
    # если случилась ошибка декодирования
    except json.decoder.JSONDecodeError:
        answer = r.content
    # узнаем статус-код
    print("Status Code:",r.status_code)
    # и печатаем что там в ответе
    print(answer)

if __name__ == '__main__':
    # с ид 1 должно быть все ок -200
    r = pet(1)
    req_info(r)
    # тут должно быть 404
    r = pet(0)
    req_info(r)
    # по документаци при неверном ид должен возвращаться статус 400
    r = pet(5.01)
    req_info(r)

    print("UPD")
    # апд. по апи
    r = pet_upd(1, "dog")
    req_info(r)

    print('new_order')
    r = store_order(1, 1, 10)
    req_info(r)

    # тут нам должно выдатать наш new_order и статус 200
    print("Чекаем заказы")
    r = order(1)
    req_info(r)
    # тут должно быть 404, такого заказа нет
    r = order(10500)
    req_info(r)
    # по документации должна быть ошибка 400 (Invalid ID supplied)
    r = order(10.500)
    req_info(r)
