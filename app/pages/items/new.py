from app.kit.html import Attr, Element, InputType, Page, Tag
from app.kit.layouts import Base


class NewItemsPage(Page):
    def __init__(self) -> None:
        self.doc = Base.model_copy()
        self.doc.title = "faststack-python-example! - new item"
        self.doc.body = [
            Element(
                tag=Tag.div,
                attrs={Attr._id: "newItemTarget"},
                children=[
                    Element(
                        tag=Tag.h1,
                        innerHTML="new item",
                        attrs={Attr._class: "text-4xl pb-2"},
                    ),
                    Element(
                        tag=Tag.form,
                        attrs={
                            Attr.hx_post: "/items",
                            Attr.hx_ext: "json-enc",
                            Attr.hx_target: "#newItemTarget",
                            Attr.hx_swap: "outerHTML",
                            Attr.hx_replace_url: "/items",
                        },
                        children=[
                            Element(
                                tag=Tag.input,
                                attrs={
                                    Attr._type: InputType.text.value,
                                    "name": "name",
                                    Attr.placeholder: "the item name",
                                    Attr.required: "",
                                    Attr._class: "bg-transparent border-b-2 "
                                    "border-blue-500"
                                    " focus:outline-none focus:border-blue-700",
                                },
                            ),
                            Element(
                                tag=Tag.br,
                            ),
                            Element(
                                tag=Tag.input,
                                attrs={
                                    Attr._type: InputType.number.value,
                                    "name": "count",
                                    Attr.placeholder: "how many?",
                                    Attr.required: "",
                                    Attr._class: "bg-transparent border-b-2 "
                                    "border-blue-500"
                                    " focus:outline-none focus:border-blue-700",
                                },
                            ),
                            Element(
                                tag=Tag.br,
                            ),
                            Element(
                                tag=Tag.input,
                                attrs={
                                    Attr._type: InputType.text.value,
                                    "name": "description",
                                    Attr.placeholder: "some more details...",
                                    Attr._class: "bg-transparent border-b-2 "
                                    "border-blue-500"
                                    " focus:outline-none focus:border-blue-700",
                                },
                            ),
                            Element(
                                tag=Tag.br,
                            ),
                            Element(
                                tag=Tag.input,
                                attrs={
                                    Attr._type: InputType.submit.value,
                                    Attr.value: "Create",
                                    Attr._class: "bg-blue-500 hover:bg-blue-700 "
                                    "text-white font-bold py-2 px-4 rounded",
                                },
                            ),
                        ],
                    ),
                ],
            ),
        ]
