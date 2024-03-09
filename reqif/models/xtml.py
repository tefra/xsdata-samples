from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Type, Union
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


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
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
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d*\*",
        },
    )
    align: Optional[XhtmlColTypeAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        },
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    valign: Optional[XhtmlColTypeValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class XhtmlParamType:
    class Meta:
        name = "xhtml.param.type"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[str] = field(
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
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlSpanType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": Type["XhtmlEmType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": Type["XhtmlStrongType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": Type["XhtmlDfnType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": Type["XhtmlCodeType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": Type["XhtmlSampType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": Type["XhtmlKbdType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": Type["XhtmlVarType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": Type["XhtmlCiteType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": Type["XhtmlAbbrType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": Type["XhtmlAcronymType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlSpanType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": Type["XhtmlEmType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": Type["XhtmlStrongType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": Type["XhtmlDfnType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": Type["XhtmlCodeType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": Type["XhtmlSampType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": Type["XhtmlKbdType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": Type["XhtmlVarType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": Type["XhtmlCiteType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": Type["XhtmlAbbrType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": Type["XhtmlAcronymType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )


@dataclass
class XhtmlColgroupType:
    class Meta:
        name = "xhtml.colgroup.type"

    col: List[XhtmlColType] = field(
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
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
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d*\*",
        },
    )
    align: Optional[XhtmlColgroupTypeAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        },
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    valign: Optional[XhtmlColgroupTypeValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class B(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Big(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class I(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Small(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sub(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sup(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Tt(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    datetime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "h1",
                    "type": Type["XhtmlH1Type"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h2",
                    "type": Type["XhtmlH2Type"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h3",
                    "type": Type["XhtmlH3Type"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h4",
                    "type": Type["XhtmlH4Type"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h5",
                    "type": Type["XhtmlH5Type"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "h6",
                    "type": Type["XhtmlH6Type"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ul",
                    "type": Type["XhtmlUlType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ol",
                    "type": Type["XhtmlOlType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dl",
                    "type": Type["XhtmlDlType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "p",
                    "type": Type["XhtmlPType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "div",
                    "type": Type["XhtmlDivType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "pre",
                    "type": Type["XhtmlPreType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "blockquote",
                    "type": Type["XhtmlBlockquoteType"],
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
                    "type": Type["XhtmlTableType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": Type["XhtmlSpanType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": Type["XhtmlEmType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": Type["XhtmlStrongType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": Type["XhtmlDfnType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": Type["XhtmlCodeType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": Type["XhtmlSampType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": Type["XhtmlKbdType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": Type["XhtmlVarType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": Type["XhtmlCiteType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": Type["XhtmlAbbrType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": Type["XhtmlAcronymType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["XhtmlEditType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlEditType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlEditType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlEditType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlEditType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlEditType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlEditType.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass


@dataclass
class Del(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Ins(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlSpanType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": Type["XhtmlEmType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": Type["XhtmlStrongType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": Type["XhtmlDfnType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": Type["XhtmlCodeType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": Type["XhtmlSampType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": Type["XhtmlKbdType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": Type["XhtmlVarType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": Type["XhtmlCiteType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": Type["XhtmlAbbrType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": Type["XhtmlAcronymType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["XhtmlAbbrType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlAbbrType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlAbbrType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlAbbrType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlAbbrType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlAbbrType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlAbbrType.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlAbbrType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlAbbrType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
class XhtmlBlockquoteType:
    class Meta:
        name = "xhtml.blockquote.type"

    h1: List["XhtmlH1Type"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    h2: List["XhtmlH2Type"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    h3: List["XhtmlH3Type"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    h4: List["XhtmlH4Type"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    h5: List["XhtmlH5Type"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    h6: List["XhtmlH6Type"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    ul: List["XhtmlUlType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    ol: List["XhtmlOlType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    dl: List["XhtmlDlType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    p: List["XhtmlPType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    div: List["XhtmlDivType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    pre: List["XhtmlPreType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    blockquote: List["XhtmlBlockquoteType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    address: List[XhtmlAddressType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    hr: List[XhtmlHrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    table: List["XhtmlTableType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    ins: List[XhtmlEditType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    del_value: List[XhtmlEditType] = field(
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlSpanType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": Type["XhtmlEmType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": Type["XhtmlStrongType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": Type["XhtmlDfnType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": Type["XhtmlCodeType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": Type["XhtmlSampType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": Type["XhtmlKbdType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": Type["XhtmlVarType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": Type["XhtmlCiteType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": Type["XhtmlAbbrType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": Type["XhtmlAcronymType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["XhtmlH1Type.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlH1Type.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlH1Type.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlH1Type.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlH1Type.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlH1Type.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlH1Type.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlH1Type.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlH1Type.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlSpanType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": Type["XhtmlEmType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": Type["XhtmlStrongType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": Type["XhtmlDfnType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": Type["XhtmlCodeType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": Type["XhtmlSampType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": Type["XhtmlKbdType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": Type["XhtmlVarType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": Type["XhtmlCiteType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": Type["XhtmlAbbrType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": Type["XhtmlAcronymType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["XhtmlH2Type.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlH2Type.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlH2Type.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlH2Type.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlH2Type.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlH2Type.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlH2Type.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlH2Type.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlH2Type.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlSpanType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": Type["XhtmlEmType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": Type["XhtmlStrongType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": Type["XhtmlDfnType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": Type["XhtmlCodeType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": Type["XhtmlSampType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": Type["XhtmlKbdType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": Type["XhtmlVarType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": Type["XhtmlCiteType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": Type["XhtmlAbbrType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": Type["XhtmlAcronymType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["XhtmlH3Type.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlH3Type.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlH3Type.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlH3Type.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlH3Type.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlH3Type.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlH3Type.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlH3Type.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlH3Type.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlSpanType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": Type["XhtmlEmType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": Type["XhtmlStrongType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": Type["XhtmlDfnType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": Type["XhtmlCodeType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": Type["XhtmlSampType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": Type["XhtmlKbdType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": Type["XhtmlVarType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": Type["XhtmlCiteType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": Type["XhtmlAbbrType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": Type["XhtmlAcronymType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["XhtmlH4Type.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlH4Type.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlH4Type.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlH4Type.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlH4Type.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlH4Type.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlH4Type.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlH4Type.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlH4Type.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlSpanType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": Type["XhtmlEmType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": Type["XhtmlStrongType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": Type["XhtmlDfnType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": Type["XhtmlCodeType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": Type["XhtmlSampType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": Type["XhtmlKbdType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": Type["XhtmlVarType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": Type["XhtmlCiteType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": Type["XhtmlAbbrType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": Type["XhtmlAcronymType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["XhtmlH5Type.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlH5Type.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlH5Type.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlH5Type.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlH5Type.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlH5Type.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlH5Type.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlH5Type.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlH5Type.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlSpanType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": Type["XhtmlEmType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": Type["XhtmlStrongType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": Type["XhtmlDfnType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": Type["XhtmlCodeType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": Type["XhtmlSampType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": Type["XhtmlKbdType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": Type["XhtmlVarType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": Type["XhtmlCiteType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": Type["XhtmlAbbrType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": Type["XhtmlAcronymType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["XhtmlH6Type.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlH6Type.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlH6Type.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlH6Type.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlH6Type.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlH6Type.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlH6Type.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlH6Type.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlH6Type.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlSpanType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": Type["XhtmlEmType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": Type["XhtmlStrongType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": Type["XhtmlDfnType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": Type["XhtmlCodeType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": Type["XhtmlSampType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": Type["XhtmlKbdType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": Type["XhtmlVarType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": Type["XhtmlCiteType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": Type["XhtmlAbbrType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": Type["XhtmlAcronymType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["XhtmlPType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlPType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlPType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlPType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlPType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlPType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlPType.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlPType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlPType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlSpanType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": Type["XhtmlEmType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": Type["XhtmlStrongType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": Type["XhtmlDfnType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": Type["XhtmlCodeType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": Type["XhtmlSampType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": Type["XhtmlKbdType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": Type["XhtmlVarType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": Type["XhtmlCiteType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": Type["XhtmlAbbrType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": Type["XhtmlAcronymType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["XhtmlPreType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlPreType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlPreType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlPreType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlPreType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlSpanType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": Type["XhtmlEmType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": Type["XhtmlStrongType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": Type["XhtmlDfnType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": Type["XhtmlCodeType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": Type["XhtmlSampType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": Type["XhtmlKbdType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": Type["XhtmlVarType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": Type["XhtmlCiteType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": XhtmlAbbrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": Type["XhtmlAcronymType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["XhtmlAcronymType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlAcronymType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlAcronymType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlAcronymType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlAcronymType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlAcronymType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlAcronymType.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlAcronymType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlAcronymType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlUlType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ol",
                    "type": Type["XhtmlOlType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dl",
                    "type": Type["XhtmlDlType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "p",
                    "type": Type["XhtmlPType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "div",
                    "type": Type["XhtmlDivType"],
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
                    "type": Type["XhtmlTableType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "br",
                    "type": XhtmlBrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "span",
                    "type": Type["XhtmlSpanType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": Type["XhtmlEmType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": Type["XhtmlStrongType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": Type["XhtmlDfnType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": Type["XhtmlCodeType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": Type["XhtmlSampType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": Type["XhtmlKbdType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": Type["XhtmlVarType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": Type["XhtmlCiteType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "abbr",
                    "type": Type["XhtmlAbbrType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "acronym",
                    "type": Type["XhtmlAcronymType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "q",
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["XhtmlDivType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlDivType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlDivType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlDivType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlDivType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlDivType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlDivType.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlDivType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlDivType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlSpanType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": Type["XhtmlEmType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": Type["XhtmlStrongType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": Type["XhtmlDfnType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": Type["XhtmlCodeType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": Type["XhtmlSampType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": Type["XhtmlKbdType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": Type["XhtmlVarType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "cite",
                    "type": Type["XhtmlCiteType"],
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
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["XhtmlCiteType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlCiteType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlCiteType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlCiteType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlCiteType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlCiteType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlCiteType.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlCiteType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlCiteType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlSpanType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": Type["XhtmlEmType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": Type["XhtmlStrongType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": Type["XhtmlDfnType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": Type["XhtmlCodeType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": Type["XhtmlSampType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": Type["XhtmlKbdType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": Type["XhtmlVarType"],
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
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["XhtmlCodeType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlCodeType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlCodeType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlCodeType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlCodeType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlCodeType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlCodeType.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlCodeType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlCodeType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlSpanType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": Type["XhtmlEmType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": Type["XhtmlStrongType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dfn",
                    "type": Type["XhtmlDfnType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": XhtmlCodeType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "samp",
                    "type": Type["XhtmlSampType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": Type["XhtmlKbdType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": Type["XhtmlVarType"],
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
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["XhtmlDfnType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlDfnType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlDfnType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlDfnType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlDfnType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlDfnType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlDfnType.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlDfnType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlDfnType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlSpanType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": Type["XhtmlEmType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": Type["XhtmlStrongType"],
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
                    "type": Type["XhtmlSampType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": Type["XhtmlKbdType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": Type["XhtmlVarType"],
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
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["XhtmlEmType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlEmType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlEmType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlEmType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlEmType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlEmType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlEmType.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlEmType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlEmType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlSpanType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": XhtmlEmType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": Type["XhtmlStrongType"],
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
                    "type": Type["XhtmlSampType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": Type["XhtmlKbdType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": Type["XhtmlVarType"],
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
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["XhtmlKbdType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlKbdType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlKbdType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlKbdType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlKbdType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlKbdType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlKbdType.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlKbdType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlKbdType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlSpanType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": XhtmlEmType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": Type["XhtmlStrongType"],
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
                    "type": Type["XhtmlSampType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "kbd",
                    "type": XhtmlKbdType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "var",
                    "type": Type["XhtmlVarType"],
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
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["XhtmlSampType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlSampType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlSampType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlSampType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlSampType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlSampType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlSampType.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlSampType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlSampType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlSpanType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": XhtmlEmType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "strong",
                    "type": Type["XhtmlStrongType"],
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
                    "type": Type["XhtmlVarType"],
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
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["XhtmlStrongType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlStrongType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlStrongType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlStrongType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlStrongType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlStrongType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlStrongType.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlStrongType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlStrongType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlSpanType"],
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
                    "type": Type["XhtmlVarType"],
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
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["XhtmlVarType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlVarType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlVarType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlVarType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlVarType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlVarType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlVarType.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlVarType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlVarType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlSpanType"],
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
                    "type": Type["XhtmlQType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "tt",
                    "type": Type["XhtmlQType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlQType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlQType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlQType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlQType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlQType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlQType.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlQType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlQType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlSpanType"],
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
                    "type": Type["XhtmlSpanType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlSpanType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlSpanType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlSpanType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlSpanType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlSpanType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlSpanType.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlSpanType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlSpanType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charset: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rel: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    rev: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    accesskey: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        },
    )
    tabindex: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlAType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlAType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlAType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlAType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlAType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlAType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlAType.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlAType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlAType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlUlType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ol",
                    "type": Type["XhtmlOlType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "dl",
                    "type": Type["XhtmlDlType"],
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
                    "type": Type["XhtmlTableType"],
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
                    "type": Type["XhtmlDdType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlDdType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlDdType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlDdType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlDdType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlDdType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlDdType.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": XhtmlAType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlDdType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlDdType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlDtType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlDtType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlDtType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlDtType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlDtType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlDtType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlDtType.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": XhtmlAType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlDtType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlDtType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
class XhtmlDlType:
    class Meta:
        name = "xhtml.dl.type"

    dt: List[XhtmlDtType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    dd: List[XhtmlDdType] = field(
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlUlType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ol",
                    "type": Type["XhtmlOlType"],
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
                    "type": Type["XhtmlTableType"],
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
                    "type": Type["XhtmlLiType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlLiType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlLiType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlLiType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlLiType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlLiType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlLiType.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": XhtmlAType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlLiType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlLiType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass


@dataclass
class XhtmlOlType:
    class Meta:
        name = "xhtml.ol.type"

    li: List[XhtmlLiType] = field(
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class XhtmlUlType:
    class Meta:
        name = "xhtml.ul.type"

    li: List[XhtmlLiType] = field(
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    declare: Optional[XhtmlObjectTypeDeclare] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    classid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    codebase: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    data: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    codetype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    archive: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    standby: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    tabindex: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlTableType"],
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
                    "type": Type["XhtmlObjectType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlObjectType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlObjectType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlObjectType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlObjectType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlObjectType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlObjectType.Sup"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": XhtmlAType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": Type["XhtmlObjectType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlObjectType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlObjectType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlCaptionType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlCaptionType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlCaptionType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlCaptionType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlCaptionType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlCaptionType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlCaptionType.Sup"],
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
                    "type": Type["XhtmlCaptionType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlCaptionType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlHeadingType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlHeadingType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlHeadingType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlHeadingType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlHeadingType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlHeadingType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlHeadingType.Sup"],
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
                    "type": Type["XhtmlHeadingType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlHeadingType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    abbr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    axis: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    headers: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    scope: Optional[XhtmlTdTypeScope] = field(
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
    align: Optional[XhtmlTdTypeAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        },
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    valign: Optional[XhtmlTdTypeValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlTableType"],
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
                    "type": Type["XhtmlTdType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlTdType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlTdType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlTdType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlTdType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlTdType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlTdType.Sup"],
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
                    "type": Type["XhtmlTdType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlTdType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass


@dataclass
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    abbr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    axis: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    headers: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    scope: Optional[XhtmlThTypeScope] = field(
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
    align: Optional[XhtmlThTypeAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        },
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    valign: Optional[XhtmlThTypeValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
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
                    "type": Type["XhtmlTableType"],
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
                    "type": Type["XhtmlThType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlThType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlThType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlThType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlThType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlThType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlThType.Sup"],
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
                    "type": Type["XhtmlThType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlThType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Big(XhtmlInlPresType):
        pass

    @dataclass
    class Small(XhtmlInlPresType):
        pass

    @dataclass
    class Sub(XhtmlInlPresType):
        pass

    @dataclass
    class Sup(XhtmlInlPresType):
        pass

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass

    @dataclass
    class Tt(XhtmlInlPresType):
        pass

    @dataclass
    class I(XhtmlInlPresType):
        pass

    @dataclass
    class B(XhtmlInlPresType):
        pass


@dataclass
class XhtmlTrType:
    class Meta:
        name = "xhtml.tr.type"

    th: List[XhtmlThType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    td: List[XhtmlTdType] = field(
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: Optional[XhtmlTrTypeAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        },
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    valign: Optional[XhtmlTrTypeValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class XhtmlTbodyType:
    class Meta:
        name = "xhtml.tbody.type"

    tr: List[XhtmlTrType] = field(
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: Optional[XhtmlTbodyTypeAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        },
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    valign: Optional[XhtmlTbodyTypeValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class XhtmlTfootType:
    class Meta:
        name = "xhtml.tfoot.type"

    tr: List[XhtmlTrType] = field(
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: Optional[XhtmlTfootTypeAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        },
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    valign: Optional[XhtmlTfootTypeValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class XhtmlTheadType:
    class Meta:
        name = "xhtml.thead.type"

    tr: List[XhtmlTrType] = field(
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: Optional[XhtmlTheadTypeAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        },
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    valign: Optional[XhtmlTheadTypeValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class XhtmlTableType:
    class Meta:
        name = "xhtml.table.type"

    caption: Optional[XhtmlCaptionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    col: List[XhtmlColType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    colgroup: List[XhtmlColgroupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    thead: Optional[XhtmlTheadType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    tfoot: Optional[XhtmlTfootType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    tbody: List[XhtmlTbodyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    tr: List[XhtmlTrType] = field(
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    summary: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    border: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    frame: Optional[XhtmlTableTypeFrame] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rules: Optional[XhtmlTableTypeRules] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cellspacing: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
    cellpadding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        },
    )
