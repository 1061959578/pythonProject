# conding: utf-8
# @Time : 2025/12/19下午3:08
# @Author : shiqing.duan
import requests


class Test_base_request():




    def test_get_no_params(self):
        response = requests.get('https://httpbin.org/get')
        assert response.status_code == 200


    def test_post_no_params(self):
        response = requests.post('https://httpbin.org/post')
        assert response.status_code == 200

    def test_get_params(self):
        params = {
            'name': 'shiqing.duan',
            'age': 30,
            'city': 'shenzheng',
            'skills': ['python', 'java']  # 会自动处理列表
        }
        url = 'https://httpbin.org/get'
        response = requests.get(url, params=params)
        assert response.status_code == 200

    def test_post_form_data(self):
        form_data = {
            'username': 'testuser',
            'password': 'testpass',
            'remember': 'true'
        }
        url = 'https://httpbin.org/post'
        response = requests.post(url, data=form_data)
        assert response.status_code == 200

    def test_post_json_data(self):
        json_data = {
            'name': 'John Doe',
            'age': 30,
            'email': 'john@example.com',
            'hobbies': ['reading', 'gaming']
        }
        url = 'https://httpbin.org/post'

        response = requests.post(url, json=json_data)
        assert response.status_code == 200

    def test_post_raw_data(self):
        raw_data = 'This is raw text data'
        url = 'https://httpbin.org/post'
        response = requests.post(url, data=raw_data)
        assert response.status_code == 200

    def test_post_file_data(self):
        with open('test.txt', 'rb') as test_file:
            file_data = {'file':test_file}
            response = requests.post('https://httpbin.org/post', files=file_data)
            print(response.status_code)
            data = response.json()
            files = data['files']
            assert files['file'] == "'这是一个测试文件的内容'"

