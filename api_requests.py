import requests
import os
from dotenv import load_dotenv
import json
# import telegram


class APIRequests:
    def __init__(self):
        load_dotenv("F:/random/.env")

    def send_telegram_message(self, message):
        chat_id = os.getenv("chat_id")
        telegram_api = os.getenv("telegram_weather_api")
        # send_text = 'https://api.telegram.org/bot' + telegram_api + '/sendPhoto?chat_id=' + chat_id + \
        #             message
        send_text = 'https://api.telegram.org/bot' + telegram_api + '/sendMessage?chat_id=' + chat_id + \
                    '&parse_mode=Markdown&text=' + message
        return requests.get(send_text)


    def post_pixel(self, date, hours):
        pixela_api = os.getenv("pixela_api")
        username = os.getenv("pixela_un")
        headers = {
            "X-USER-TOKEN": pixela_api
        }
        pixel_params = {
            "date": date,
            "quantity": hours,
        }
        url = f'https://pixe.la/v1/users/{username}/graphs/hourscoded'
        r = requests.post(url, json=pixel_params, headers=headers)
        print(r.text)
        image_url = f'https://pixe.la/v1/users/{username}/graphs/hourscoded?mode=short&appearance=dark'
        # return requests.get(image_url)
        return image_url

    def print_json_structure(self, json_response):
        formatted_response = json.dumps(json_response, indent=2)
        print(formatted_response)


# api = APIRequests()
# api.print_json_structure(api.get_stock_data("AMD"))
