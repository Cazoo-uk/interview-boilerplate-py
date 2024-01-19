from src.app import main


def test_should_return_input_length_ten():
    assert len(main(10)) == 10


def test_should_return_input_length_twenty():
    assert len(main(20)) == 20


def test_should_return_in_order():
    assert main(2) == [1, 2]


def test_should_return_cazoo_for_third_item():
    assert main(3) == [1, 2, "Cazoo!"]


def test_should_return_cazoo_for_third_item_up_to_five():
    assert main(5) == [1, 2, "Cazoo!", 4, 5]


def test_should_return_cazoo_for_third_item_up_to_six():
    assert main(5) == [1, 2, "Cazoo!", 4, 5, "Cazoo!"]