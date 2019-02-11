import requests

TOKEN = '' #Введите сюда свой токен, выкладывать в интернет свой токен, я не могу = )

class User:
    def __init__(self, token, id):
        self.token = token
        self.id = id

    def __and__(self, other):
        return self.get_friends(self.id, other.id)

    def __repr__(self):
        return f'https://vk.com/id{self.id}'

    def get_params(self, source_uid, target_uid):
        return {
            'v': '5.92',
            'access_token': self.token,
            'source_uid': source_uid,
            'target_uid': target_uid,
        }

    def get_friends(self, source_uid, target_uid):
        params = self.get_params(source_uid, target_uid)
        response = requests.get(
            'https://api.vk.com/method/friends.getMutual',
            params
        )
        list_test = response.json()

        test_list = list()
        for i in list_test['response']:
            a = User(TOKEN, i)
            #print(a)
            test_list.append(a)
        return f'Список общих друзей: {test_list}'

user = User(TOKEN, 483667681)
user1 = User(TOKEN, 154734856)
print(user)
print(user & user1)