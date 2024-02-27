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
class XhtmlOlType:
    class Meta:
        name = "xhtml.ol.type"

    li: List["XhtmlLiType"] = field(
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
                    "type": Type["Tt19"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["I19"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["B19"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["Big18"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["Small18"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["Sub18"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["Sup18"],
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
                    "type": Type["Ins15"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["Del15"],
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
                    "type": Type["Tt13"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["I13"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["B13"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["Big12"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["Small12"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["Sub12"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["Sup12"],
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
                    "type": Type["Ins10"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["Del10"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )


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
                    "type": Type["Tt5"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["I5"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["B5"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["Big4"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["Small4"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["Sub4"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["Sup4"],
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
                    "type": Type["Ins3"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["Del3"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )


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
                    "type": Type["Tt6"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["I6"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["B6"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["Big5"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["Small5"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["Sub5"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["Sup5"],
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
                    "type": Type["Ins4"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["Del4"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )


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
                    "type": Type["Tt7"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["I7"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["B7"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["Big6"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["Small6"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["Sub6"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["Sup6"],
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
                    "type": Type["Ins5"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["Del5"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )


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
                    "type": Type["Tt8"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["I8"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["B8"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["Big7"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["Small7"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["Sub7"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["Sup7"],
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
                    "type": Type["Ins6"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["Del6"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )


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
                    "type": Type["Tt9"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["I9"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["B9"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["Big8"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["Small8"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["Sub8"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["Sup8"],
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
                    "type": Type["Ins7"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["Del7"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )


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
                    "type": Type["Tt11"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["I11"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["B11"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["Big10"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["Small10"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["Sub10"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["Sup10"],
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
                    "type": Type["Ins9"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["Del9"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )


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
                    "type": Type["Tt3"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["I3"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["B3"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["Ins2"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["Del2"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )


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
                    "type": Type["XhtmlH1Type"],
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
                    "type": XhtmlOlType,
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
                    "type": Type["XhtmlBlockquoteType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "address",
                    "type": Type["XhtmlAddressType"],
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
                    "type": Type["Tt17"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["I17"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["B17"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["Big16"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["Small16"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["Sub16"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["Sup16"],
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
                    "type": Type["Ins13"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["Del13"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )


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
                    "type": Type["XhtmlH1Type"],
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
                    "type": XhtmlOlType,
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
                    "type": Type["XhtmlBlockquoteType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "address",
                    "type": Type["XhtmlAddressType"],
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
                    "type": Type["Tt18"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["I18"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["B18"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["Big17"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["Small17"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["Sub17"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["Sup17"],
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
                    "type": Type["Ins14"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["Del14"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )


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
    h2: List[XhtmlH2Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    h3: List[XhtmlH3Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    h4: List[XhtmlH4Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    h5: List[XhtmlH5Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    h6: List[XhtmlH6Type] = field(
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
    ol: List[XhtmlOlType] = field(
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
    p: List[XhtmlPType] = field(
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
    pre: List[XhtmlPreType] = field(
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
    address: List["XhtmlAddressType"] = field(
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
    table: List[XhtmlTableType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    del_value: List["XhtmlEditType"] = field(
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
                    "type": Type["XhtmlH1Type"],
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
                    "type": XhtmlOlType,
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
                    "type": Type["XhtmlAddressType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "hr",
                    "type": XhtmlHrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "table",
                    "type": XhtmlTableType,
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
                    "type": Type["Tt10"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["I10"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["B10"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["Big9"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["Small9"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["Sub9"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["Sup9"],
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
                    "type": Type["Ins8"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["Del8"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )


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
                    "type": Type["XhtmlH1Type"],
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
                    "type": XhtmlOlType,
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
                    "type": Type["XhtmlAddressType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "hr",
                    "type": XhtmlHrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "table",
                    "type": XhtmlTableType,
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
                    "type": Type["Tt14"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["I14"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["B14"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["Big13"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["Small13"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["Sub13"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["Sup13"],
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
                    "type": Type["Ins11"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["Del11"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )


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
                    "type": Type["XhtmlH1Type"],
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
                    "type": Type["XhtmlAddressType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "hr",
                    "type": XhtmlHrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "table",
                    "type": XhtmlTableType,
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
                    "type": Type["Tt15"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["I15"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["B15"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["Big14"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["Small14"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["Sub14"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["Sup14"],
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
                    "type": Type["Ins12"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["Del12"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
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
                    "type": Type["XhtmlAddressType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "hr",
                    "type": XhtmlHrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "table",
                    "type": XhtmlTableType,
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
                    "type": Type["Tt2"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["I2"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["B2"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["Big2"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["Small2"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["Sub2"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["Sup2"],
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
                    "type": Type["Ins1"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["Del1"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )


@dataclass
class Del1(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Del10(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Del11(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Del12(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Del13(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Del14(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Del15(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Del2(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Del3(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Del4(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Del5(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Del6(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Del7(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Del8(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Del9(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Ins1(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Ins10(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Ins11(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Ins12(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Ins13(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Ins14(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Ins15(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Ins2(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Ins3(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Ins4(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Ins5(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Ins6(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Ins7(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Ins8(XhtmlEditType):
    class Meta:
        global_type = False


@dataclass
class Ins9(XhtmlEditType):
    class Meta:
        global_type = False


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
                    "type": Type["Tt4"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["I4"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["B4"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["Big3"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["Small3"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["Sub3"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["Sup3"],
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
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


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
                    "type": Type["XhtmlAddressType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "hr",
                    "type": XhtmlHrType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "table",
                    "type": XhtmlTableType,
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
                    "type": Type["Tt16"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["I16"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["B16"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["Big15"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["Small15"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["Sub15"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["Sup15"],
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
                    "type": Type["Tt12"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["I12"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["B12"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["Big11"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["Small11"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["Sub11"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["Sup11"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": XhtmlObjectType,
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
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


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
                    "type": Type["Tt1"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["I1"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["B1"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["Big1"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["Small1"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["Sub1"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["Sup1"],
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
                    "type": Type["XhtmlInlPresType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlInlPresType.Del"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class Ins(XhtmlEditType):
        pass

    @dataclass
    class Del(XhtmlEditType):
        pass


@dataclass
class B1(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class B10(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class B11(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class B12(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class B13(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class B14(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class B15(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class B16(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class B17(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class B18(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class B19(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class B2(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class B3(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class B4(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class B5(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class B6(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class B7(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class B8(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class B9(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Big1(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Big10(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Big11(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Big12(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Big13(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Big14(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Big15(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Big16(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Big17(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Big18(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Big2(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Big3(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Big4(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Big5(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Big6(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Big7(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Big8(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Big9(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class I1(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class I10(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class I11(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class I12(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class I13(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class I14(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class I15(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class I16(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class I17(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class I18(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class I19(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class I2(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class I3(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class I4(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class I5(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class I6(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class I7(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class I8(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class I9(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Small1(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Small10(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Small11(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Small12(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Small13(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Small14(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Small15(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Small16(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Small17(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Small18(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Small2(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Small3(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Small4(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Small5(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Small6(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Small7(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Small8(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Small9(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sub1(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sub10(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sub11(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sub12(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sub13(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sub14(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sub15(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sub16(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sub17(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sub18(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sub2(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sub3(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sub4(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sub5(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sub6(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sub7(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sub8(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sub9(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sup1(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sup10(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sup11(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sup12(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sup13(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sup14(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sup15(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sup16(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sup17(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sup18(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sup2(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sup3(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sup4(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sup5(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sup6(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sup7(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sup8(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Sup9(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Tt1(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Tt10(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Tt11(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Tt12(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Tt13(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Tt14(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Tt15(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Tt16(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Tt17(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Tt18(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Tt19(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Tt2(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Tt3(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Tt4(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Tt5(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Tt6(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Tt7(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Tt8(XhtmlInlPresType):
    class Meta:
        global_type = False


@dataclass
class Tt9(XhtmlInlPresType):
    class Meta:
        global_type = False


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
                    "type": XhtmlQType,
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
                    "type": XhtmlQType,
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
                    "type": XhtmlQType,
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
                    "type": Type["XhtmlAddressType.Tt"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlAddressType.I"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlAddressType.B"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlAddressType.Big"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlAddressType.Small"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlAddressType.Sub"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlAddressType.Sup"],
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
                    "type": Type["XhtmlAddressType.Ins"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlAddressType.Del"],
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
