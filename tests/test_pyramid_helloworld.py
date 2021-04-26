from pyramid_helloworld import hello_world


def test_hello_world():
    assert hello_world(None).text == "Hello World!"
