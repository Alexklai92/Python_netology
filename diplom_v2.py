import time
import requests
import json

TOKEN = ''


class User:
    def __init__(self, token, u_id, u_user):
        self.u_id = u_id
        self.token = token
        if u_user:
            self.u_id = self.get_user_id()

    def __repr__(self):
        return f'https://vk.com/id{self.u_id}'

    def get_user_id(self):
        params = {
            'v': '5.92',
            'access_token': self.token,
            'user_ids': self.u_id,
        }
        response = requests.get(
            'https://api.vk.com/method/users.get',
            params
        )
        result = response.json()['response'][0]['id']
        return result

    def get_params(self, u_id):
        if type(u_id) == int:
            return {
                'v': '5.92',
                'access_token': self.token,
                'user_id': u_id,
                'extended': 1
            }

    def get_groups(self):
        params = self.get_params(self.u_id)
        response = requests.get(
            'https://api.vk.com/method/groups.get',
            params
        )
        return response.json()

    def get_friends(self):
        params = self.get_params(self.u_id)
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params
        )
        resp_list = response.json()
        friend_list = list()
        for g in resp_list['response']['items']:
            a = User(TOKEN, g, False)
            friend_list.append(a)
        return friend_list

    @staticmethod
    def write_file(file, text):
        with open(file, 'w', encoding='utf-8') as f:
            f.write(''.join(text))
        return ''.join(text)

    def unicum_group(self, second_value):
        result_json = list()
        user_groups = self.get_groups()['response']['items']
        unic_group = set()
        for u_groups in user_groups:
            unic_group.add(u_groups['id'])
        output_result = set.difference(unic_group, second_value)
        for value in user_groups:
            for value_1 in output_result:
                if value['id'] == value_1:
                    spy_game_result = {'id': value['id'], 'name': value['name'], 'screen_name': value['screen_name']}
                    result_json.append(spy_game_result)
        result_json = json.dumps(result_json, ensure_ascii=False)
        return result_json

    def spy_game(self):
        f_list = self.get_friends()
        friend_index = 0
        friend_group = set()
        while friend_index < len(f_list):
            test = f_list[friend_index].get_groups()
            try:
                for group in test['response']['items']:
                    friend_group.add(group['id'])
                print(f'Ходим по друзьям {friend_index + 1} из {len(f_list)}')
                friend_index += 1
            except KeyError:
                if test['error']['error_code'] == 6:
                    time.sleep(1)
                else:
                    friend_index += 1
        self.write_file('vk_groups.json', self.unicum_group(friend_group))


target = 'eshmargunov'
user = User(TOKEN, target, True)
user.spy_game()
