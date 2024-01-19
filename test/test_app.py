from src.app import main


def test_should_return_input_length_ten():
    assert len(main(10)) == 10


def test_should_return_input_length_twenty():
    assert len(main(20)) == 20


def test_should_return_in_order():
    assert main(2) == [1, 2]
