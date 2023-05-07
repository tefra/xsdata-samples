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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    span: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d*\*",
        }
    )
    align: Optional[XhtmlColTypeAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        }
    )
    valign: Optional[XhtmlColTypeValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
        }
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class XhtmlParamType:
    class Meta:
        name = "xhtml.param.type"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valuetype: XhtmlParamTypeValuetype = field(
        default=XhtmlParamTypeValuetype.DATA,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlInlPresType"],
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
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
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
        }
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    span: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d*\*",
        }
    )
    align: Optional[XhtmlColgroupTypeAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        }
    )
    valign: Optional[XhtmlColgroupTypeValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlInlPresType"],
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
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlInlPresType"],
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
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlInlPresType"],
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
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlInlPresType"],
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
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlInlPresType"],
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
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlInlPresType"],
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
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlInlPresType"],
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
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": Type["XhtmlAType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    abbr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    axis: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    headers: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: Optional[XhtmlTdTypeScope] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rowspan: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        }
    )
    colspan: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[XhtmlTdTypeAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        }
    )
    valign: Optional[XhtmlTdTypeValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlInlPresType"],
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
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    abbr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    axis: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    headers: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: Optional[XhtmlThTypeScope] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rowspan: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        }
    )
    colspan: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[XhtmlThTypeAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        }
    )
    valign: Optional[XhtmlThTypeValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlInlPresType"],
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
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
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
        }
    )
    td: List[XhtmlTdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[XhtmlTrTypeAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        }
    )
    valign: Optional[XhtmlTrTypeValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
        }
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[XhtmlTbodyTypeAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        }
    )
    valign: Optional[XhtmlTbodyTypeValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
        }
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[XhtmlTfootTypeAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        }
    )
    valign: Optional[XhtmlTfootTypeValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
        }
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[XhtmlTheadTypeAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        }
    )
    valign: Optional[XhtmlTheadTypeValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
        }
    )
    col: List[XhtmlColType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    colgroup: List[XhtmlColgroupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    thead: Optional[XhtmlTheadType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tfoot: Optional[XhtmlTfootType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tbody: List[XhtmlTbodyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tr: List[XhtmlTrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    summary: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        }
    )
    border: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    frame: Optional[XhtmlTableTypeFrame] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rules: Optional[XhtmlTableTypeRules] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    cellspacing: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        }
    )
    cellpadding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        }
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
        }
    )
    h2: List[XhtmlH2Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    h3: List[XhtmlH3Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    h4: List[XhtmlH4Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    h5: List[XhtmlH5Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    h6: List[XhtmlH6Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    ul: List["XhtmlUlType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    ol: List[XhtmlOlType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dl: List["XhtmlDlType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    p: List[XhtmlPType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    div: List["XhtmlDivType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    pre: List[XhtmlPreType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    blockquote: List["XhtmlBlockquoteType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    address: List["XhtmlAddressType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    hr: List[XhtmlHrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    table: List[XhtmlTableType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata={
            "name": "del",
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    cite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlInlPresType"],
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
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlInlPresType"],
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
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
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
        }
    )
    dd: List[XhtmlDdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlInlPresType"],
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
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
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
        }
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    cite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datetime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlInlPresType"],
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
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": Type["XhtmlEditType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlInlPresType"],
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
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    declare: Optional[XhtmlObjectTypeDeclare] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    classid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    codebase: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    data: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    codetype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    archive: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    standby: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+[%]|\d*\.\d+[%]",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    tabindex: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlInlPresType"],
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
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
    )


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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charset: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rel: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    rev: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    accesskey: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
        }
    )
    tabindex: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "object",
                    "type": XhtmlObjectType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ins",
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Type["XhtmlInlPresType"],
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": Type["XhtmlInlPresType"],
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
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
    )


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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    cite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": XhtmlInlPresType,
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
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
    )


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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": XhtmlInlPresType,
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
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
    )


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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": XhtmlInlPresType,
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
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
    )


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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": XhtmlInlPresType,
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
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
    )


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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": XhtmlInlPresType,
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
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
    )


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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": XhtmlInlPresType,
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
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
    )


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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": XhtmlInlPresType,
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
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
    )


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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": XhtmlInlPresType,
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
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
    )


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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": XhtmlInlPresType,
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
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
    )


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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": XhtmlInlPresType,
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
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
    )


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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": XhtmlInlPresType,
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
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
    )


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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": XhtmlInlPresType,
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
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": XhtmlInlPresType,
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
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
    )


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
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "big",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "small",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": XhtmlInlPresType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sup",
                    "type": XhtmlInlPresType,
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
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "del",
                    "type": XhtmlEditType,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        }
    )
