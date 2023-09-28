import requests
import json
from config import ID, API_KEY, TOKEN, URL
main_trello_end_point = URL
trello_key = API_KEY
trello_token = TOKEN
application_list_id = ID

def create_trello_card(card_name, card_desc):
    create_card_end_point = main_trello_end_point + 'cards'
    jsonObject = {"key": trello_key,
               "token": trello_token,
               "idList": application_list_id,
               "name": f"Отдел {card_name}",
               "desc": card_desc}

    new_card = requests.post(create_card_end_point, json=jsonObject)

    print(json.loads(new_card.text))


def check_board_card():
    params = {
        "key":trello_key,
        "token":trello_token,
    }


def main():
    create_trello_card(str(input("Введите отдел :")), str(input("Введите проблему: ")))


if __name__ == "__main__":
    while True:
        main()
