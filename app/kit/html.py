from abc import ABC
from enum import Enum, unique
from typing import Any, Dict, List, Optional, Union

from fastapi.responses import HTMLResponse
from pydantic import BaseModel


@unique
class Tag(Enum):
    a = "a"
    abbr = "abbr"
    address = "address"
    area = "area"
    article = "article"
    aside = "aside"
    audio = "audio"
    b = "b"
    base = "base"
    bdi = "bdi"
    bdo = "bdo"
    blockquote = "blockquote"
    body = "body"
    br = "br"
    button = "button"
    canvas = "canvas"
    caption = "caption"
    cite = "cite"
    code = "code"
    col = "col"
    colgroup = "colgroup"
    data = "data"
    datalist = "datalist"
    dd = "dd"
    _del = "del"
    details = "details"
    dfn = "dfn"
    dialog = "dialog"
    div = "div"
    dl = "dl"
    dt = "dt"
    em = "em"
    embed = "embed"
    fieldset = "fieldset"
    figcaption = "figcaption"
    footer = "footer"
    form = "form"
    h1 = "h1"
    h2 = "h2"
    h3 = "h3"
    h4 = "h4"
    h5 = "h5"
    h6 = "h6"
    head = "head"
    header = "header"
    hgroup = "hgroup"
    hr = "hr"
    html = "html"
    i = "i"
    iframe = "iframe"
    img = "img"
    input = "input"
    ins = "ins"
    kbd = "kbd"
    label = "label"
    legend = "legend"
    li = "li"
    link = "link"
    main = "main"
    map = "map"
    mark = "mark"
    menu = "menu"
    meta = "meta"
    meter = "meter"
    nav = "nav"
    noscript = "noscript"
    _object = "object"
    ol = "ol"
    optgroup = "optgroup"
    option = "option"
    output = "output"
    p = "p"
    picture = "picture"
    pre = "pre"
    progress = "progress"
    q = "q"
    rp = "rp"
    rt = "rt"
    ruby = "ruby"
    s = "s"
    samp = "samp"
    script = "script"
    search = "search"
    section = "section"
    select = "select"
    slot = "slot"
    small = "small"
    source = "source"
    span = "span"
    strong = "strong"
    style = "style"
    sub = "sub"
    summary = "summary"
    sup = "sup"
    table = "table"
    tbody = "tbody"
    td = "td"
    template = "template"
    textarea = "textarea"
    tfoot = "tfoot"
    th = "th"
    thead = "thead"
    time = "time"
    title = "title"
    tr = "tr"
    track = "track"
    u = "u"
    ul = "ul"
    var = "var"
    video = "video"
    wbr = "wbr"
    xmp = "xmp"


@unique
class Attr(Enum):
    #
    #   Global Attributes
    #
    accesskey = "accesskey"
    autocapitalize = "autocapitalize"
    autofocus = "autofocus"
    _class = "_class"
    contenteditable = "contenteditable"
    data = "data-*"
    _dir = "dir"
    draggable = "draggable"
    enterkeyhint = "enterkeyhint"
    exportparts = "exportparts"
    hidden = "hidden"
    _id = "id"
    inert = "inert"
    inputmode = "inputmode"
    _is = "is"
    itemid = "itemid"
    itemprop = "itemprop"
    itemref = "itemref"
    itemscope = "itemscope"
    itemtype = "itemtype"
    lang = "lang"
    nonce = "nonce"
    part = "part"
    popover = "popover"
    slot = "slot"
    spellcheck = "spellcheck"
    style = "style"
    tabindex = "tabindex"
    title = "title"
    translate = "translate"
    #
    #   Attributes
    #
    accept = "accept"
    autocomplete = "autocomplete"
    capture = "capture"
    crossorigin = "crossorigin"
    dirname = "dirname"
    disabled = "disabled"
    elementtiming = "elementtiming"
    _for = "for"
    _max = "max"
    maxlength = "maxlength"
    _min = "min"
    minlength = "minlength"
    multiple = "multiple"
    pattern = "pattern"
    placeholder = "placeholder"
    readonly = "readonly"
    rel = "rel"
    required = "required"
    size = "size"
    step = "step"


@unique
class InputType(Enum):
    button = "button"
    checkbox = "checkbox"
    color = "color"
    date = "date"
    datetime_local = "datetime-local"
    email = "email"
    file = "file"
    hidden = "hidden"
    image = "image"
    month = "month"
    number = "number"
    password = "password"
    radio = "radio"
    range = "range"
    reset = "reset"
    search = "search"
    submit = "submit"
    tel = "tel"
    text = "text"
    time = "time"
    url = "url"
    week = "week"


class Element(BaseModel):
    tag: Tag
    attrs: Optional[Dict[Attr | str, Any]] = None
    innerHTML: Optional[Union[str, "Element"]] = None
    children: Optional[List[Union[str, "Element"]]] = None

    async def render(self) -> str:
        attrs = "".join(
            [
                f'{k.value}="{v}"' if isinstance(k, Attr) else f'{k}="{v}"'
                for k, v in (self.attrs or {}).items()
            ]
        )
        if self.children:
            innerHTML = "".join(
                [
                    await el.render() if isinstance(el, Element) else el
                    for el in self.children
                ]
            )
        elif self.innerHTML:
            innerHTML = (
                await self.innerHTML.render()
                if isinstance(self.innerHTML, Element)
                else self.innerHTML
            )
        else:
            innerHTML = ""
        return f"<{self.tag.value} {attrs}>{innerHTML}</{self.tag.value}>"


class Doc(BaseModel):
    title: str = "faststack"
    lang: str = "en"
    charset: str = "utf-8"
    _class: str = "scroll-smooth"
    head: List[Element] = [
        Element(
            tag=Tag.meta,
            attrs={"charset": "utf-8"},
        ),
        Element(
            tag=Tag.meta,
            attrs={
                "name": "viewport",
                "content": "width=device-width, initial-scale=1.0",
            },
        ),
    ]
    body: List[Element] = []

    async def render(self) -> str:
        head = "\n".join([await el.render() for el in self.head])
        body = "\n".join([await el.render() for el in self.body])
        return f"""<!DOCTYPE html>
<html lang='{self.lang}' class='{self._class}'>
    <head>
        <meta charset='{self.charset}'>
        <title>{self.title}</title>
        {head}
    </head>
    <body>
        {body}
    </body>
</html>"""

    async def render_html(self) -> HTMLResponse:
        return HTMLResponse(await self.render())


class Page(ABC):
    def __init__(self, doc: Doc) -> None:
        self.doc = doc
