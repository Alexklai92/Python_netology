import time
import requests
import json

TOKEN = '' #AUTH TOKEN

class User:
    def __init__(self, token, id):
        self.id = id
        self.token = token

    def __repr__(self):
        return f'https://vk.com/id{self.id}'

    def get_ids(self, ):
        params = {
            'v': '5.92',
            'access_token': self.token,
            'user_ids': self.id,
        }
        response = requests.get(
            'https://api.vk.com/method/users.get',
            params
        )
        a = response.json()['response'][0]['id']
        #return response.json()['response'][0]['id']
        return a

    def get_params(self, id):
        if type(id) == int:
            return {
                'v': '5.92',
                'access_token': self.token,
                'user_id': self.id,
                'extended': 1
            }
        else:
            return {
                'v': '5.92',
                'access_token': self.token,
                'user_id': self.get_ids(),
                'fields': 'name',
                'extended': 1
            }

    def get_groups(self):
        """
        Поиск групп у пользователя
        :return:
        """
        params = self.get_params(self.id)
        response = requests.get(
            'https://api.vk.com/method/groups.get',
            params
        )
        return response.json()

    def get_friends(self):
        """
        Поиск друзей у пользователя
        :return:
        """
        params = self.get_params(self.id)
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params
        )
        resp_list = response.json()
        friends_list = list()
        for g in resp_list['response']['items']:
            if type(g) == int:
                a = User(TOKEN, g)
            else:
                a = User(TOKEN, g['id'])
            friends_list.append(a)
        return friends_list

    def checked_friends_groups(self):
        """
        Поиск групп у друзей пользователя
        :return:
        """
        f_list = self.get_friends()
        friend_groups = list()
        print(f_list)
        count = 0
        for i in f_list:
            for g in i.get_groups():
                if g == 'response':
                    j = i.get_groups()['response']['items']
                    for id_group in j:
                        friend_groups.append(id_group['id'])
                        count += 1
                    print(f'... пробегаем по группам, уже нашли {count} групп')
                else:
                    print(i, i.get_groups()['error']['error_msg'])
            time.sleep(1)
        return friend_groups

    def spy_games(self):
        """
        Поиск уникальных групп пользователя
        (в которых состоит только он среди всех своих друзей)
        :return:
        """
        self.user = user
        spy_games_list = user.get_groups()['response']['items']
        spy_group_id = list()
        for id in spy_games_list:
            spy_group_id.append(id['id'])
        spy_group_id = set(spy_group_id)
        unic_group = set.difference(spy_group_id, set(self.checked_friends_groups()))
        json_output_unic_group = list()
        print('Уникальные группы пользователя')
        for group in unic_group:
            for i in spy_games_list:
                if i['id'] == group:
                    group_fields = {'id': i['id'], 'names': i['name']}
                    json_output_unic_group.append(group_fields)
        output = json.dumps(json_output_unic_group, ensure_ascii=False)
        print(output)

spy_id = input()
user = User(TOKEN, spy_id)
#user = User(TOKEN, 'eshmargunov')
user.spy_games()