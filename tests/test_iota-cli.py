from iota import Iota
from pytest import raises
from IotaCli.main import MyAppTest
import pprint

def test_IotaCli():
    # test IotaCli without any subcommands or arguments
    with MyAppTest() as app:
        app.run()
        assert app.exit_code == 0


def test_IotaCli_debug():
    # test that debug mode is functional
    argv = ['--debug']
    with MyAppTest(argv=argv) as app:
        app.run()
        assert app.debug is True


def test_command1():
    # test command1 without arguments
    argv = ['command1']
    with MyAppTest(argv=argv) as app:
        app.run()
        data,output = app.last_rendered
        assert data['foo'] == 'bar'
        assert output.find('Foo => bar')


    # test command1 with arguments
    argv = ['command1', '--foo', 'not-bar']
    with MyAppTest(argv=argv) as app:
        app.run()
        data,output = app.last_rendered
        assert data['foo'] == 'not-bar'
        assert output.find('Foo => not-bar')


def test_connect_api():
    argv = ['connect']
    with MyAppTest(argv=argv) as app:
        app.run()
        data, output = app.last_rendered
        assert data[]