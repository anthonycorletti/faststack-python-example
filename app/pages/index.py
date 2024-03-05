from app.kit.html import Attr, Element, Page, Tag
from app.layouts.base import Base


class IndexPage(Page):
    def __init__(self) -> None:
        self.doc = Base.model_copy()
        self.doc.title = "faststack-python-example!"
        self.doc.body = [
            Element(
                tag=Tag.h1,
                attrs={Attr._id: "title"},
                innerHTML="faststack-python-example! - index",
            ),
            Element(
                tag=Tag.p,
                children=[
                    "This is a FastAPI project that uses the ",
                    Element(
                        tag=Tag.a,
                        attrs={
                            "href": "https://fastapi.tiangolo.com",
                            "target": "blank",
                        },
                        children=["fastapi"],
                    ),
                    " framework.",
                ],
            ),
            Element(
                tag=Tag.p,
                children=[
                    "You can view our items ",
                    Element(
                        tag=Tag.a,
                        attrs={
                            "href": "/items",
                        },
                        children=["here"],
                    ),
                    ".",
                ],
            ),
        ]
