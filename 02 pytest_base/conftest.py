import os
import smtplib
import tempfile

import  pytest

@pytest.fixture(scope="module")
def smtp_connection(request):
    print('-----------')
    print(request.module)
    server = getattr(request.module, "smtpserver", "smtp.gmail.com")
    smtp_connection = smtplib.SMTP(server, 587, timeout=5)
    yield smtp_connection
    print(f"finalizing {smtp_connection} ({server})")
    smtp_connection.close()


@pytest.fixture
def cleandir():
    with tempfile.TemporaryDirectory() as newpath:
        old_cwd = os.getcwd()
        os.chdir(newpath)
        yield
        os.chdir(old_cwd)



@pytest.fixture(params=['one', 'two', 'three'])
def parametrized_username(request):
    return request.param

@pytest.fixture
def non_parametrized_username(request):
    return 'username'


