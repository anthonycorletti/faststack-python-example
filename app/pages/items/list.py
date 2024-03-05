from app.kit.html import Attr, Element, Page, Tag
from app.layouts.base import Base


class ListItemsPage(Page):
    def __init__(self) -> None:
        self.doc = Base.model_copy()
        self.doc.title = "faststack-python-example!"
        self.doc.body = [
            Element(
                tag=Tag.h1,
                attrs={Attr._id: "title"},
                innerHTML="faststack-python-example - list items",
            ),
            Element(
                tag=Tag.p,
                children=[
                    "This is a list of items.",
                ],
            ),
        ]
