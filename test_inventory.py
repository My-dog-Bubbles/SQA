import pytest
from inventory import add_item, remove_item, get_item_count

def test_add_item_empty_string(inventory):
    with pytest.raises(ValueError):
        result = add_item(inventory, "")
        assert ValueError

def test_add_item_at_compacity(inventory):
    item = "marcus is not r"
    inventory["capacity"] = 0
    inventory["items"] = ["your mom"]
    with pytest.raises(ValueError):
        result = add_item(inventory, item)
        assert ValueError

def test_add_item_locked_inventory(inventory):
    inventory["locked"] = True
    og_items = inventory.copy()
    result = add_item(inventory, "item")
    assert result == og_items

def test_remove_item_not_in_inventory(inventory):
    with pytest.raises(ValueError):
        remove_item(inventory, "your mom")
        assert ValueError

def test_remove_item_in_inventory(inventory):
    inventory["items"] = ["your mom"]
    result = remove_item(inventory, "your mom")
    assert result["items"] == []

def test_remove_item_locked_inventory(inventory):
    inventory["locked"] = True
    inventory["items"] = ["your mom"]
    og_items = inventory.copy()
    result = remove_item(inventory, "your mom")
    assert result == og_items

def test_get_item_count_zero_items(inventory):
    result = get_item_count(inventory)
    assert result == 0

def test_get_item_count_locked_inventory(inventory):
    inventory["locked"] = True
    inventory["items"] = ["your mom"]
    result = get_item_count(inventory)
    assert result == 1
