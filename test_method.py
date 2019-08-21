from unittest import TestCase
import requests


class TestTornadoRequest(TestCase):
    base_url = 'http://10.36.174.23:8000'

    def test_index_post(self):
        url = self.base_url + '/'
        # 发起post请求，表单参数使用data来指定
        resp = requests.post(url, data={
            'name': 'disen',
            'city': ['西安', '上海']
        })
        print(resp.text)

    def test_index_put_get(self):
        url = self.base_url + '/'
        resp = requests.put(url, data={
            'name': '张奥',
            'age': 33
        })
        print(resp.text)

    def test_index_get_get(self):
        url = self.base_url + '/'

        #  查询参数
        resp = requests.get(url, data={
            'name': '张奥',
            'city': ['33', '22']
        })

        # 当参数没有给对时，会出现400的错误
        print(resp.text)


class TestCookieRequest(TestCase):
    url = 'http://10.36.174.23:9000/cookie'

    def test_search(self):
        resp = requests.get('http://10.36.174.23:9000/search', params={
            'wd': 'python'
        })
        print(resp.text)
        # print(resp.cookies)
        for key, cookie in resp.cookies.items():
            print(key, resp.cookies.get(key))

    def test_get(self):
        resp = requests.get(self.url)
        print(resp)

    def test_delete(self):
        resp = requests.delete(self.url, params={
            'name': 'token'
        })
        print(resp.text)


class TestOrderRequest(TestCase):
    url = 'http://10.36.174.23:9000/order/1/3'

    def test_get(self):
        resp = requests.get(self.url)
        print(resp.text)

    def test_post(self):
        resp = requests.post(self.url)
        print(resp.text)


class TestUserRequest(TestCase):
    url = 'http://10.36.174.23:9000/user'

    def test_login(self):
        resp = requests.get(self.url,
                            json={'name': 'jack',
                                  'pwd': '123'
                                  })
        if resp.request.headers.get('Content-Type').startswith('application/json'):
            # 读取响应数据
            print(resp.json())
        else:
            print(resp.text)

    def test_register(self):
        resp = requests.post(self.url,
                             json={
                                 'name': 'liming',
                                 'pwd': '456',
                                 'phone': '18693489523'
                             })
        if resp.request.headers.get('Content-Type').startswith('application/json'):
            print(resp.json())
        else:
            print(resp.text)

    def test_update(self):
        resp = requests.put(self.url,
                            json={
                                'id': 1,
                                'name': 'zhangao'
                            })
        if resp.request.headers.ger('Content-Type').startswith('application/json'):
            print(resp.json())
        else:
            print(resp.text)

    def test_delete(self):
        resp = requests.delete(self.url,
                               json={
                                   'id': 1
                               })
        print(resp.json())
