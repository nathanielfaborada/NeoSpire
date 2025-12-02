import random
from highrise.models import Item

SHIRTS = [
    "shirt-n_starteritems2019tankwhite",
    "shirt-n_starteritems2019tankblack",
    "shirt-n_starteritems2019raglanwhite",
    "shirt-n_starteritems2019raglanblack",
    "shirt-n_starteritems2019pulloverwhite",
    "shirt-n_starteritems2019pulloverblack",
]


def random_outfit():
    """Return a list of Highrise Item objects."""
    outfit = [
        Item(type="shirt", id=random.choice(SHIRTS))]
    return outfit
