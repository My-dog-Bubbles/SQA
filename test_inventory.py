import pytest
from inventory import add_item, remove_item, get_item_count

def test_add_item_empty_string(inventory):
    with pytest.raises(ValueError):
        result = add_item(inventory, "")
        assert ValueError

def test_add_item_at_compacity(inventory):
    item = "marcus is not r"
    result = add_item(inventory, item)
    with pytest.raises(ValueError):
        len(item) >= inventory["capacity"]
        assert ValueError

# def test_add_item_locked_inventory(inventory): # IDK how I would test this
#     inventory["locked"] = True
#     result = add_item(inventory, "item")

def test_remove_item_not_in_inventory(inventory):
    inventory["items"] = ["your mom"]
    with pytest.raises(ValueError):
        remove_item(inventory, "your mom")
        assert ValueError

# def test_remove_item_locked_inventory(inventory): # IDK how I would test this
#     inventory["locked"] = True
#     inventory["items"] = ["your mom"]
#     result = add_item(inventory, "your mom")

def test_get_item_count_zero_items(inventory):
    result = get_item_count(inventory)
    assert len(result["items"]) == 0

def test_get_item_count_locked_inventory(inventory):
    inventory["locked"] = True
    inventory["items"] = ["your mom"]
    result = get_item_count(inventory)
    assert result == 1
