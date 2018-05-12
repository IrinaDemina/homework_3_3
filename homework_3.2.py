import requests
# AUTH_URL = "https://oauth.vk.com/authorize"
# APP_ID = 6475174
# auth_data = {
#     "client_id": APP_ID,
#     "display": "page",
#     "scope": "friends",
#     "response_type": "token",
#     "v": "5.74"
# }


def find_common_friends(first, second):
    TOKEN = "c91670ecbbfea58b50966022cafd08e03deacbe80f1a05a3d1e65e925995c616c3db5c108d2968d6d38b1"
    response = requests.get(
        "https://api.vk.com/method/friends.getMutual",
        params=dict(
            v="5.74",
            access_token=TOKEN,
            source_uid=first,
            target_uid=second
        )
    )
    result = response.json().get("response", [])
    return result


def main():
    VK_URL = "https://vk.com/id"
    first = input("Введите ID первого друга: ")
    second = input("Введите ID второго друга: ")
    find_common_friends(first, second)
    result_list = find_common_friends(first, second)

    for id in result_list:
        link = "".join((VK_URL, str(id)))
        print("ID: {}; адрес: {}".format(id, link))
main()
