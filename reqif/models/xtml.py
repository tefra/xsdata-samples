from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import ForwardRef

from xsdata.models.datatype import XmlDateTime

from reqif.models.org.w3.xml.pkg_1998.namespace import (
    LangValue,
    SpaceValue,
)

__NAMESPACE__ = "http://www.w3.org/1999/xhtml"


class XhtmlColTypeAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class XhtmlColTypeValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class XhtmlColgroupTypeAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class XhtmlColgroupTypeValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class XhtmlObjectTypeDeclare(Enum):
    DECLARE = "declare"


class XhtmlParamTypeValuetype(Enum):
    DATA = "data"
    REF = "ref"
    OBJECT = "object"


class XhtmlTableTypeFrame(Enum):
    VOID = "void"
    ABOVE = "above"
    BELOW = "below"
    HSIDES = "hsides"
    LHS = "lhs"
    RHS = "rhs"
    VSIDES = "vsides"
    BOX = "box"
    BORDER = "border"


class XhtmlTableTypeRules(Enum):
    NONE = "none"
    GROUPS = "groups"
    ROWS = "rows"
    COLS = "cols"
    ALL = "all"


class XhtmlTbodyTypeAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class XhtmlTbodyTypeValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class XhtmlTdTypeAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class XhtmlTdTypeScope(Enum):
    ROW = "row"
    COL = "col"
    ROWGROUP = "rowgroup"
    COLGROUP = "colgroup"


class XhtmlTdTypeValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class XhtmlTfootTypeAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class XhtmlTfootTypeValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class XhtmlThTypeAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class XhtmlThTypeScope(Enum):
    ROW = "row"
    COL = "col"
    ROWGROUP = "rowgroup"
    COLGROUP = "colgroup"


class XhtmlThTypeValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class XhtmlTheadTypeAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class XhtmlTheadTypeValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class XhtmlTrTypeAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class XhtmlTrTypeValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


@dataclass(kw_only=True)
class XhtmlBrType:
    class Meta:
        name = "xhtml.br.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class XhtmlColType:
    class Meta:
        name = "xhtml.col.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    span: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        },
    )
    width: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d*\*",
        },
    )
    align: None | XhtmlColTypeAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    valign: None | XhtmlColTypeValign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class XhtmlHrType:
    class Meta:
        name = "xhtml.hr.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class XhtmlParamType:
    class Meta:
        name = "xhtml.param.type"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    value: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valuetype: XhtmlParamTypeValuetype = field(
        default=XhtmlParamTypeValuetype.DATA,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class XhtmlInlPresType:
    class Meta:
        name = "xhtml.InlPres.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": ForwardRef("XhtmlEmType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("XhtmlStrongType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("XhtmlDfnType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": ForwardRef("XhtmlCodeType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("XhtmlSampType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("XhtmlKbdType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": ForwardRef("XhtmlVarType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("XhtmlCiteType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("XhtmlAbbrType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("XhtmlAcronymType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class XhtmlAddressType:
    class Meta:
        name = "xhtml.address.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": ForwardRef("XhtmlEmType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("XhtmlStrongType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("XhtmlDfnType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": ForwardRef("XhtmlCodeType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("XhtmlSampType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("XhtmlKbdType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": ForwardRef("XhtmlVarType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("XhtmlCiteType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("XhtmlAbbrType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("XhtmlAcronymType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class XhtmlColgroupType:
    class Meta:
        name = "xhtml.colgroup.type"

    col: list[XhtmlColType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    span: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        },
    )
    width: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d*\*",
        },
    )
    align: None | XhtmlColgroupTypeAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    valign: None | XhtmlColgroupTypeValign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class B(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass(kw_only=True)
class Big(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass(kw_only=True)
class I(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass(kw_only=True)
class Small(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass(kw_only=True)
class Sub(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass(kw_only=True)
class Sup(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass(kw_only=True)
class Tt(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass(kw_only=True)
class XhtmlEditType:
    class Meta:
        name = "xhtml.edit.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cite: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    datetime: None | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "h1",
                    "type": ForwardRef("XhtmlH1Type"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h2",
                    "type": ForwardRef("XhtmlH2Type"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h3",
                    "type": ForwardRef("XhtmlH3Type"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h4",
                    "type": ForwardRef("XhtmlH4Type"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h5",
                    "type": ForwardRef("XhtmlH5Type"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h6",
                    "type": ForwardRef("XhtmlH6Type"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ul",
                    "type": ForwardRef("XhtmlUlType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ol",
                    "type": ForwardRef("XhtmlOlType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dl",
                    "type": ForwardRef("XhtmlDlType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "p",
                    "type": ForwardRef("XhtmlPType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "div",
                    "type": ForwardRef("XhtmlDivType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "pre",
                    "type": ForwardRef("XhtmlPreType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "blockquote",
                    "type": ForwardRef("XhtmlBlockquoteType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "address",
                    "type": XhtmlAddressType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "hr",
                    "type": XhtmlHrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "table",
                    "type": ForwardRef("XhtmlTableType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": ForwardRef("XhtmlEmType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("XhtmlStrongType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("XhtmlDfnType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": ForwardRef("XhtmlCodeType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("XhtmlSampType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("XhtmlKbdType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": ForwardRef("XhtmlVarType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("XhtmlCiteType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("XhtmlAbbrType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("XhtmlAcronymType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlEditType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlEditType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlEditType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlEditType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlEditType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlEditType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlEditType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass


@dataclass(kw_only=True)
class Del(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass(kw_only=True)
class Ins(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass(kw_only=True)
class XhtmlAbbrType:
    class Meta:
        name = "xhtml.abbr.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": ForwardRef("XhtmlEmType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("XhtmlStrongType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("XhtmlDfnType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": ForwardRef("XhtmlCodeType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("XhtmlSampType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("XhtmlKbdType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": ForwardRef("XhtmlVarType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("XhtmlCiteType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("XhtmlAbbrType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("XhtmlAcronymType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlAbbrType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlAbbrType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlAbbrType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlAbbrType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlAbbrType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlAbbrType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlAbbrType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlAbbrType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlAbbrType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlBlockquoteType:
    class Meta:
        name = "xhtml.blockquote.type"

    h1: list[XhtmlH1Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    h2: list[XhtmlH2Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    h3: list[XhtmlH3Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    h4: list[XhtmlH4Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    h5: list[XhtmlH5Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    h6: list[XhtmlH6Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    ul: list[XhtmlUlType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    ol: list[XhtmlOlType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    dl: list[XhtmlDlType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    p: list[XhtmlPType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    div: list[XhtmlDivType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    pre: list[XhtmlPreType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    blockquote: list[XhtmlBlockquoteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    address: list[XhtmlAddressType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    hr: list[XhtmlHrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    table: list[XhtmlTableType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    ins: list[XhtmlEditType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    del_value: list[XhtmlEditType] = field(
        default_factory=list,
        metadata={
            "name": "del",
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cite: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class XhtmlH1Type:
    class Meta:
        name = "xhtml.h1.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": ForwardRef("XhtmlEmType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("XhtmlStrongType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("XhtmlDfnType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": ForwardRef("XhtmlCodeType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("XhtmlSampType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("XhtmlKbdType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": ForwardRef("XhtmlVarType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("XhtmlCiteType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("XhtmlAbbrType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("XhtmlAcronymType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlH1Type.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlH1Type.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlH1Type.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlH1Type.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlH1Type.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlH1Type.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlH1Type.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlH1Type.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlH1Type.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlH2Type:
    class Meta:
        name = "xhtml.h2.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": ForwardRef("XhtmlEmType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("XhtmlStrongType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("XhtmlDfnType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": ForwardRef("XhtmlCodeType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("XhtmlSampType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("XhtmlKbdType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": ForwardRef("XhtmlVarType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("XhtmlCiteType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("XhtmlAbbrType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("XhtmlAcronymType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlH2Type.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlH2Type.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlH2Type.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlH2Type.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlH2Type.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlH2Type.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlH2Type.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlH2Type.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlH2Type.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlH3Type:
    class Meta:
        name = "xhtml.h3.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": ForwardRef("XhtmlEmType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("XhtmlStrongType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("XhtmlDfnType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": ForwardRef("XhtmlCodeType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("XhtmlSampType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("XhtmlKbdType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": ForwardRef("XhtmlVarType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("XhtmlCiteType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("XhtmlAbbrType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("XhtmlAcronymType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlH3Type.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlH3Type.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlH3Type.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlH3Type.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlH3Type.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlH3Type.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlH3Type.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlH3Type.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlH3Type.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlH4Type:
    class Meta:
        name = "xhtml.h4.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": ForwardRef("XhtmlEmType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("XhtmlStrongType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("XhtmlDfnType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": ForwardRef("XhtmlCodeType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("XhtmlSampType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("XhtmlKbdType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": ForwardRef("XhtmlVarType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("XhtmlCiteType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("XhtmlAbbrType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("XhtmlAcronymType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlH4Type.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlH4Type.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlH4Type.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlH4Type.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlH4Type.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlH4Type.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlH4Type.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlH4Type.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlH4Type.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlH5Type:
    class Meta:
        name = "xhtml.h5.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": ForwardRef("XhtmlEmType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("XhtmlStrongType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("XhtmlDfnType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": ForwardRef("XhtmlCodeType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("XhtmlSampType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("XhtmlKbdType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": ForwardRef("XhtmlVarType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("XhtmlCiteType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("XhtmlAbbrType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("XhtmlAcronymType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlH5Type.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlH5Type.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlH5Type.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlH5Type.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlH5Type.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlH5Type.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlH5Type.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlH5Type.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlH5Type.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlH6Type:
    class Meta:
        name = "xhtml.h6.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": ForwardRef("XhtmlEmType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("XhtmlStrongType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("XhtmlDfnType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": ForwardRef("XhtmlCodeType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("XhtmlSampType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("XhtmlKbdType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": ForwardRef("XhtmlVarType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("XhtmlCiteType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("XhtmlAbbrType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("XhtmlAcronymType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlH6Type.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlH6Type.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlH6Type.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlH6Type.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlH6Type.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlH6Type.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlH6Type.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlH6Type.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlH6Type.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlPType:
    class Meta:
        name = "xhtml.p.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": ForwardRef("XhtmlEmType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("XhtmlStrongType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("XhtmlDfnType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": ForwardRef("XhtmlCodeType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("XhtmlSampType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("XhtmlKbdType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": ForwardRef("XhtmlVarType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("XhtmlCiteType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("XhtmlAbbrType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("XhtmlAcronymType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlPType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlPType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlPType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlPType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlPType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlPType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlPType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlPType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlPType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlPreType:
    class Meta:
        name = "xhtml.pre.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": ForwardRef("XhtmlEmType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("XhtmlStrongType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("XhtmlDfnType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": ForwardRef("XhtmlCodeType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("XhtmlSampType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("XhtmlKbdType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": ForwardRef("XhtmlVarType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("XhtmlCiteType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("XhtmlAbbrType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("XhtmlAcronymType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlPreType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlPreType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlPreType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlPreType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlPreType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlAcronymType:
    class Meta:
        name = "xhtml.acronym.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": ForwardRef("XhtmlEmType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("XhtmlStrongType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("XhtmlDfnType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": ForwardRef("XhtmlCodeType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("XhtmlSampType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("XhtmlKbdType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": ForwardRef("XhtmlVarType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("XhtmlCiteType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": XhtmlAbbrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("XhtmlAcronymType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlAcronymType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlAcronymType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlAcronymType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlAcronymType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlAcronymType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlAcronymType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlAcronymType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlAcronymType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlAcronymType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlDivType:
    class Meta:
        name = "xhtml.div.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "h1",
                    "type": XhtmlH1Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h2",
                    "type": XhtmlH2Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h3",
                    "type": XhtmlH3Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h4",
                    "type": XhtmlH4Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h5",
                    "type": XhtmlH5Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h6",
                    "type": XhtmlH6Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ul",
                    "type": ForwardRef("XhtmlUlType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ol",
                    "type": ForwardRef("XhtmlOlType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dl",
                    "type": ForwardRef("XhtmlDlType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "p",
                    "type": ForwardRef("XhtmlPType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "div",
                    "type": ForwardRef("XhtmlDivType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "pre",
                    "type": XhtmlPreType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "blockquote",
                    "type": XhtmlBlockquoteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "address",
                    "type": XhtmlAddressType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "hr",
                    "type": XhtmlHrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "table",
                    "type": ForwardRef("XhtmlTableType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": ForwardRef("XhtmlEmType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("XhtmlStrongType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("XhtmlDfnType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": ForwardRef("XhtmlCodeType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("XhtmlSampType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("XhtmlKbdType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": ForwardRef("XhtmlVarType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("XhtmlCiteType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("XhtmlAbbrType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("XhtmlAcronymType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlDivType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlDivType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlDivType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlDivType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlDivType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlDivType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlDivType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlDivType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlDivType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass


@dataclass(kw_only=True)
class XhtmlCiteType:
    class Meta:
        name = "xhtml.cite.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": ForwardRef("XhtmlEmType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("XhtmlStrongType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("XhtmlDfnType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": ForwardRef("XhtmlCodeType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("XhtmlSampType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("XhtmlKbdType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": ForwardRef("XhtmlVarType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("XhtmlCiteType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": XhtmlAbbrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": XhtmlAcronymType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlCiteType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlCiteType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlCiteType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlCiteType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlCiteType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlCiteType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlCiteType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlCiteType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlCiteType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlCodeType:
    class Meta:
        name = "xhtml.code.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": ForwardRef("XhtmlEmType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("XhtmlStrongType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("XhtmlDfnType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": ForwardRef("XhtmlCodeType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("XhtmlSampType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("XhtmlKbdType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": ForwardRef("XhtmlVarType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": XhtmlCiteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": XhtmlAbbrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": XhtmlAcronymType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlCodeType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlCodeType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlCodeType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlCodeType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlCodeType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlCodeType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlCodeType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlCodeType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlCodeType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlDfnType:
    class Meta:
        name = "xhtml.dfn.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": ForwardRef("XhtmlEmType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("XhtmlStrongType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("XhtmlDfnType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": XhtmlCodeType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("XhtmlSampType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("XhtmlKbdType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": ForwardRef("XhtmlVarType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": XhtmlCiteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": XhtmlAbbrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": XhtmlAcronymType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlDfnType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlDfnType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlDfnType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlDfnType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlDfnType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlDfnType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlDfnType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlDfnType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlDfnType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlEmType:
    class Meta:
        name = "xhtml.em.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": ForwardRef("XhtmlEmType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("XhtmlStrongType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": XhtmlDfnType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": XhtmlCodeType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("XhtmlSampType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("XhtmlKbdType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": ForwardRef("XhtmlVarType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": XhtmlCiteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": XhtmlAbbrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": XhtmlAcronymType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlEmType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlEmType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlEmType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlEmType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlEmType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlEmType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlEmType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlEmType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlEmType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlKbdType:
    class Meta:
        name = "xhtml.kbd.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": XhtmlEmType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("XhtmlStrongType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": XhtmlDfnType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": XhtmlCodeType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("XhtmlSampType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("XhtmlKbdType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": ForwardRef("XhtmlVarType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": XhtmlCiteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": XhtmlAbbrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": XhtmlAcronymType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlKbdType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlKbdType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlKbdType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlKbdType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlKbdType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlKbdType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlKbdType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlKbdType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlKbdType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlSampType:
    class Meta:
        name = "xhtml.samp.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": XhtmlEmType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("XhtmlStrongType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": XhtmlDfnType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": XhtmlCodeType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("XhtmlSampType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": XhtmlKbdType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": ForwardRef("XhtmlVarType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": XhtmlCiteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": XhtmlAbbrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": XhtmlAcronymType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlSampType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlSampType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlSampType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlSampType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlSampType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlSampType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlSampType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlSampType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlSampType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlStrongType:
    class Meta:
        name = "xhtml.strong.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": XhtmlEmType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("XhtmlStrongType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": XhtmlDfnType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": XhtmlCodeType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": XhtmlSampType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": XhtmlKbdType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": ForwardRef("XhtmlVarType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": XhtmlCiteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": XhtmlAbbrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": XhtmlAcronymType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlStrongType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlStrongType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlStrongType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlStrongType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlStrongType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlStrongType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlStrongType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlStrongType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlStrongType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlVarType:
    class Meta:
        name = "xhtml.var.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": XhtmlEmType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": XhtmlStrongType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": XhtmlDfnType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": XhtmlCodeType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": XhtmlSampType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": XhtmlKbdType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": ForwardRef("XhtmlVarType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": XhtmlCiteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": XhtmlAbbrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": XhtmlAcronymType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlVarType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlVarType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlVarType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlVarType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlVarType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlVarType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlVarType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlVarType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlVarType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlQType:
    class Meta:
        name = "xhtml.q.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cite: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": XhtmlEmType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": XhtmlStrongType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": XhtmlDfnType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": XhtmlCodeType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": XhtmlSampType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": XhtmlKbdType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": XhtmlVarType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": XhtmlCiteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": XhtmlAbbrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": XhtmlAcronymType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": ForwardRef("XhtmlQType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlQType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlQType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlQType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlQType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlQType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlQType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlQType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlQType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlQType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlSpanType:
    class Meta:
        name = "xhtml.span.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": ForwardRef("XhtmlSpanType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": XhtmlEmType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": XhtmlStrongType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": XhtmlDfnType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": XhtmlCodeType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": XhtmlSampType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": XhtmlKbdType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": XhtmlVarType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": XhtmlCiteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": XhtmlAbbrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": XhtmlAcronymType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": XhtmlQType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlSpanType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlSpanType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlSpanType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlSpanType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlSpanType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlSpanType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlSpanType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": ForwardRef("XhtmlAType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlSpanType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlSpanType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlAType:
    class Meta:
        name = "xhtml.a.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charset: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rel: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    rev: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    accesskey: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        },
    )
    tabindex: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": XhtmlSpanType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": XhtmlEmType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": XhtmlStrongType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": XhtmlDfnType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": XhtmlCodeType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": XhtmlSampType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": XhtmlKbdType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": XhtmlVarType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": XhtmlCiteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": XhtmlAbbrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": XhtmlAcronymType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": XhtmlQType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlAType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlAType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlAType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlAType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlAType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlAType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlAType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlAType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlAType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlDdType:
    class Meta:
        name = "xhtml.dd.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "h1",
                    "type": XhtmlH1Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h2",
                    "type": XhtmlH2Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h3",
                    "type": XhtmlH3Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h4",
                    "type": XhtmlH4Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h5",
                    "type": XhtmlH5Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h6",
                    "type": XhtmlH6Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ul",
                    "type": ForwardRef("XhtmlUlType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ol",
                    "type": ForwardRef("XhtmlOlType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dl",
                    "type": ForwardRef("XhtmlDlType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "p",
                    "type": XhtmlPType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "div",
                    "type": XhtmlDivType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "pre",
                    "type": XhtmlPreType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "blockquote",
                    "type": XhtmlBlockquoteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "address",
                    "type": XhtmlAddressType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "hr",
                    "type": XhtmlHrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "table",
                    "type": ForwardRef("XhtmlTableType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": XhtmlSpanType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": XhtmlEmType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": XhtmlStrongType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": XhtmlDfnType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": XhtmlCodeType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": XhtmlSampType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": XhtmlKbdType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": XhtmlVarType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": XhtmlCiteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": XhtmlAbbrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": XhtmlAcronymType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": XhtmlQType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlDdType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlDdType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlDdType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlDdType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlDdType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlDdType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlDdType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": XhtmlAType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlDdType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlDdType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass


@dataclass(kw_only=True)
class XhtmlDtType:
    class Meta:
        name = "xhtml.dt.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": XhtmlSpanType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": XhtmlEmType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": XhtmlStrongType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": XhtmlDfnType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": XhtmlCodeType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": XhtmlSampType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": XhtmlKbdType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": XhtmlVarType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": XhtmlCiteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": XhtmlAbbrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": XhtmlAcronymType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": XhtmlQType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlDtType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlDtType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlDtType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlDtType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlDtType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlDtType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlDtType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": XhtmlAType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlDtType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlDtType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlDlType:
    class Meta:
        name = "xhtml.dl.type"

    dt: list[XhtmlDtType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    dd: list[XhtmlDdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class XhtmlLiType:
    class Meta:
        name = "xhtml.li.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "h1",
                    "type": XhtmlH1Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h2",
                    "type": XhtmlH2Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h3",
                    "type": XhtmlH3Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h4",
                    "type": XhtmlH4Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h5",
                    "type": XhtmlH5Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h6",
                    "type": XhtmlH6Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ul",
                    "type": ForwardRef("XhtmlUlType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ol",
                    "type": ForwardRef("XhtmlOlType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dl",
                    "type": XhtmlDlType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "p",
                    "type": XhtmlPType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "div",
                    "type": XhtmlDivType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "pre",
                    "type": XhtmlPreType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "blockquote",
                    "type": XhtmlBlockquoteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "address",
                    "type": XhtmlAddressType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "hr",
                    "type": XhtmlHrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "table",
                    "type": ForwardRef("XhtmlTableType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": XhtmlSpanType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": XhtmlEmType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": XhtmlStrongType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": XhtmlDfnType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": XhtmlCodeType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": XhtmlSampType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": XhtmlKbdType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": XhtmlVarType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": XhtmlCiteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": XhtmlAbbrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": XhtmlAcronymType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": XhtmlQType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlLiType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlLiType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlLiType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlLiType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlLiType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlLiType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlLiType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": XhtmlAType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlLiType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlLiType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass


@dataclass(kw_only=True)
class XhtmlOlType:
    class Meta:
        name = "xhtml.ol.type"

    li: list[XhtmlLiType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "min_occurs": 1,
        },
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class XhtmlUlType:
    class Meta:
        name = "xhtml.ul.type"

    li: list[XhtmlLiType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "min_occurs": 1,
        },
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class XhtmlObjectType:
    class Meta:
        name = "xhtml.object.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    declare: None | XhtmlObjectTypeDeclare = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    classid: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    codebase: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    data: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    codetype: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    archive: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    standby: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    height: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    width: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    tabindex: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "param",
                    "type": XhtmlParamType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h1",
                    "type": XhtmlH1Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h2",
                    "type": XhtmlH2Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h3",
                    "type": XhtmlH3Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h4",
                    "type": XhtmlH4Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h5",
                    "type": XhtmlH5Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h6",
                    "type": XhtmlH6Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ul",
                    "type": XhtmlUlType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ol",
                    "type": XhtmlOlType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dl",
                    "type": XhtmlDlType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "p",
                    "type": XhtmlPType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "div",
                    "type": XhtmlDivType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "pre",
                    "type": XhtmlPreType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "blockquote",
                    "type": XhtmlBlockquoteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "address",
                    "type": XhtmlAddressType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "hr",
                    "type": XhtmlHrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "table",
                    "type": ForwardRef("XhtmlTableType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": XhtmlSpanType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": XhtmlEmType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": XhtmlStrongType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": XhtmlDfnType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": XhtmlCodeType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": XhtmlSampType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": XhtmlKbdType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": XhtmlVarType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": XhtmlCiteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": XhtmlAbbrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": XhtmlAcronymType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": XhtmlQType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlObjectType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlObjectType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlObjectType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlObjectType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlObjectType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlObjectType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlObjectType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": XhtmlAType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": ForwardRef("XhtmlObjectType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlObjectType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlObjectType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass


@dataclass(kw_only=True)
class XhtmlCaptionType:
    class Meta:
        name = "xhtml.caption.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": XhtmlSpanType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": XhtmlEmType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": XhtmlStrongType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": XhtmlDfnType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": XhtmlCodeType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": XhtmlSampType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": XhtmlKbdType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": XhtmlVarType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": XhtmlCiteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": XhtmlAbbrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": XhtmlAcronymType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": XhtmlQType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlCaptionType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlCaptionType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlCaptionType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlCaptionType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlCaptionType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlCaptionType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlCaptionType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": XhtmlAType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": XhtmlObjectType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlCaptionType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlCaptionType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlHeadingType:
    class Meta:
        name = "xhtml.heading.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": XhtmlSpanType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": XhtmlEmType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": XhtmlStrongType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": XhtmlDfnType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": XhtmlCodeType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": XhtmlSampType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": XhtmlKbdType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": XhtmlVarType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": XhtmlCiteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": XhtmlAbbrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": XhtmlAcronymType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": XhtmlQType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlHeadingType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlHeadingType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlHeadingType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlHeadingType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlHeadingType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlHeadingType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlHeadingType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": XhtmlAType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": XhtmlObjectType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlHeadingType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlHeadingType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass


@dataclass(kw_only=True)
class XhtmlTdType:
    class Meta:
        name = "xhtml.td.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    abbr: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    axis: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    headers: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    scope: None | XhtmlTdTypeScope = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rowspan: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        },
    )
    colspan: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        },
    )
    align: None | XhtmlTdTypeAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    valign: None | XhtmlTdTypeValign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "h1",
                    "type": XhtmlH1Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h2",
                    "type": XhtmlH2Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h3",
                    "type": XhtmlH3Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h4",
                    "type": XhtmlH4Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h5",
                    "type": XhtmlH5Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h6",
                    "type": XhtmlH6Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ul",
                    "type": XhtmlUlType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ol",
                    "type": XhtmlOlType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dl",
                    "type": XhtmlDlType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "p",
                    "type": XhtmlPType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "div",
                    "type": XhtmlDivType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "pre",
                    "type": XhtmlPreType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "blockquote",
                    "type": XhtmlBlockquoteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "address",
                    "type": XhtmlAddressType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "hr",
                    "type": XhtmlHrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "table",
                    "type": ForwardRef("XhtmlTableType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": XhtmlSpanType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": XhtmlEmType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": XhtmlStrongType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": XhtmlDfnType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": XhtmlCodeType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": XhtmlSampType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": XhtmlKbdType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": XhtmlVarType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": XhtmlCiteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": XhtmlAbbrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": XhtmlAcronymType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": XhtmlQType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlTdType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlTdType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlTdType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlTdType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlTdType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlTdType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlTdType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": XhtmlAType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": XhtmlObjectType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlTdType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlTdType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass


@dataclass(kw_only=True)
class XhtmlThType:
    class Meta:
        name = "xhtml.th.type"

    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    abbr: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    axis: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    headers: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    scope: None | XhtmlThTypeScope = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rowspan: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        },
    )
    colspan: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        },
    )
    align: None | XhtmlThTypeAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    valign: None | XhtmlThTypeValign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "h1",
                    "type": XhtmlH1Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h2",
                    "type": XhtmlH2Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h3",
                    "type": XhtmlH3Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h4",
                    "type": XhtmlH4Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h5",
                    "type": XhtmlH5Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h6",
                    "type": XhtmlH6Type,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ul",
                    "type": XhtmlUlType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ol",
                    "type": XhtmlOlType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dl",
                    "type": XhtmlDlType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "p",
                    "type": XhtmlPType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "div",
                    "type": XhtmlDivType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "pre",
                    "type": XhtmlPreType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "blockquote",
                    "type": XhtmlBlockquoteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "address",
                    "type": XhtmlAddressType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "hr",
                    "type": XhtmlHrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "table",
                    "type": ForwardRef("XhtmlTableType"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": XhtmlSpanType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": XhtmlEmType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": XhtmlStrongType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": XhtmlDfnType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": XhtmlCodeType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": XhtmlSampType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": XhtmlKbdType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": XhtmlVarType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": XhtmlCiteType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": XhtmlAbbrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": XhtmlAcronymType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": XhtmlQType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("XhtmlThType.Tt"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("XhtmlThType.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": ForwardRef("XhtmlThType.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": ForwardRef("XhtmlThType.Big"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": ForwardRef("XhtmlThType.Small"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("XhtmlThType.Sub"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("XhtmlThType.Sup"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": XhtmlAType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": XhtmlObjectType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": ForwardRef("XhtmlThType.Ins"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": ForwardRef("XhtmlThType.Del"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Big(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Small(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sub(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Sup(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class Ins(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Del(XhtmlEditType):
        pass

    @dataclass(kw_only=True)
    class Tt(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class I(XhtmlInlPresType):
        pass

    @dataclass(kw_only=True)
    class B(XhtmlInlPresType):
        pass


@dataclass(kw_only=True)
class XhtmlTrType:
    class Meta:
        name = "xhtml.tr.type"

    th: list[XhtmlThType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    td: list[XhtmlTdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: None | XhtmlTrTypeAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    valign: None | XhtmlTrTypeValign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class XhtmlTbodyType:
    class Meta:
        name = "xhtml.tbody.type"

    tr: list[XhtmlTrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "min_occurs": 1,
        },
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: None | XhtmlTbodyTypeAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    valign: None | XhtmlTbodyTypeValign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class XhtmlTfootType:
    class Meta:
        name = "xhtml.tfoot.type"

    tr: list[XhtmlTrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "min_occurs": 1,
        },
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: None | XhtmlTfootTypeAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    valign: None | XhtmlTfootTypeValign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class XhtmlTheadType:
    class Meta:
        name = "xhtml.thead.type"

    tr: list[XhtmlTrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "min_occurs": 1,
        },
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: None | XhtmlTheadTypeAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    valign: None | XhtmlTheadTypeValign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class XhtmlTableType:
    class Meta:
        name = "xhtml.table.type"

    caption: None | XhtmlCaptionType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    col: list[XhtmlColType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    colgroup: list[XhtmlColgroupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    thead: None | XhtmlTheadType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    tfoot: None | XhtmlTfootType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    tbody: list[XhtmlTbodyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    tr: list[XhtmlTrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    summary: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    width: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    border: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    frame: None | XhtmlTableTypeFrame = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rules: None | XhtmlTableTypeRules = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cellspacing: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    cellpadding: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
