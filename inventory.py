def add_item(inventory, item):
    if item == "":
        return ValueError
    if inventory["locked"] == True:
        return inventory
    inventory["items"] = inventory["items"]+[item]
    if len(inventory["items"]) > inventory["capacity"]:
        return ValueError
    return inventory

def remove_item(inventory, item):
    if inventory["locked"] == True:
        return inventory
    if item in inventory["items"]:
        inventory["items"].remove(item)
        return inventory
    else:
        return ValueError

def get_item_count(inventory):
    return len(inventory["items"])