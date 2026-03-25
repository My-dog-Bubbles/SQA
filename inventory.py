def add_item(inventory, item):
    if item == "":
        raise ValueError
    if inventory["locked"]:
        return inventory
    if len(inventory["items"])+1 > inventory["capacity"]:
        raise ValueError
    return inventory


def remove_item(inventory, item):
    if inventory["locked"]:
        return inventory
    if item in inventory["items"]:
        inventory["items"].remove(item)
        return inventory
    else:
        raise ValueError


def get_item_count(inventory):
    return len(inventory["items"])
