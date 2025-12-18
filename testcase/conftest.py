
import pytest
import requests


class TestHttpBin():
    # post 请求测试
    def test_get_no_param(self):
        response = requests.get('https://httpbin.org/get')
        assert response.status_code == 200
        pass