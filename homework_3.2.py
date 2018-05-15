import requests


def find_common_friends(first, second):
    TOKEN = "0e3f6e0f8a84edefa32612b259b0072823692821427d3ad51a6ec6a16b55d274a3cf640a056bbc763ff26"
    response = requests.get(
        "https://api.vk.com/method/friends.getMutual",
        params=dict(
            v="5.74",
            access_token=TOKEN,
            source_uid=first,
            target_uid=second
        )
    )
    return response.json().get("response", [])


def main():
    VK_URL = "https://vk.com/id"
    first = input("Введите ID первого друга: ")
    second = input("Введите ID второго друга: ")
    result_list = find_common_friends(first, second)

    for id in result_list:
        link = "".join((VK_URL, str(id)))
        print("ID: {}; адрес: {}".format(id, link))
main()
