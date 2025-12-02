import random

SHIRTS = {
    "shirt-n_starteritems2019tankwhite": {"item_name": "Tank - White"},
    "shirt-n_starteritems2019tankblack": {"item_name": "Tank - Black"},
    "shirt-n_starteritems2019raglanwhite": {"item_name": "Raglan - White"},
    "shirt-n_starteritems2019raglanblack": {"item_name": "Raglan - Black"},
    "shirt-n_starteritems2019pulloverwhite": {"item_name": "Pullover - White"},
    "shirt-n_starteritems2019pulloverblack": {"item_name": "Pullover - Black"},
    "shirt-n_room32019jerseywhite": {"item_name": "White Vintage Jersey"},
    "shirt-n_room12019buttondownblack": {"item_name": "Black Button Down"},
    "shirt-n_flashysuit": {"item_name": "Flashy Suit"},
}
def random_outfit():
    """Return a full random outfit dictionary."""
    outfit = {}

    outfit.update(random.choice(list(SHIRTS.items()))[1])
    
    return outfit
