'''
'''
import pytest

from app import create_app


@pytest.fixture(scope='class')
def test_app_instance():
    app = create_app(use_test_env=True)
    app.app_context().push()
    yield app
    del app


@pytest.fixture(scope='class')
def dev_app_instance():
    app = create_app()
    app.app_context().push()
    yield app
    del app


@pytest.mark.usefixtures('test_app_instance')
class TestAppConfigInTestEnv:
    def test_testing_config_value(self, test_app_instance):
        assert test_app_instance.config['TESTING'] is True

    def test_secret_key_config_value(self, test_app_instance):
        assert test_app_instance.config['SECRET_KEY'] is not None


@pytest.mark.usefixtures('dev_app_instance')
class TestAppConfigInDevelopmentEnv:
    def test_testing_config_value(self, dev_app_instance):
        assert dev_app_instance.config['TESTING'] is False

    def test_debug_config_value(self, dev_app_instance):
        assert dev_app_instance.config['DEBUG'] is True

    def test_secret_key_config_value(self, dev_app_instance):
        assert dev_app_instance.config['SECRET_KEY'] is not None
