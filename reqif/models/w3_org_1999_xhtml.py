from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from reqif.models.w3_org_xml_1998_namespace import (
    XhtmlInlPresTypeValue,
    XhtmlATypeValue,
    XhtmlAbbrTypeValue,
    XhtmlAcronymTypeValue,
    XhtmlAddressTypeValue,
    XhtmlBlockquoteTypeValue,
    XhtmlBrTypeValue,
    XhtmlCaptionTypeValue,
    XhtmlCiteTypeValue,
    XhtmlCodeTypeValue,
    XhtmlColTypeValue,
    XhtmlColgroupTypeValue,
    XhtmlDdTypeValue,
    XhtmlDfnTypeValue,
    XhtmlDivTypeValue,
    XhtmlDlTypeValue,
    XhtmlDtTypeValue,
    XhtmlEditTypeValue,
    XhtmlEmTypeValue,
    XhtmlH1TypeValue,
    XhtmlH2TypeValue,
    XhtmlH3TypeValue,
    XhtmlH4TypeValue,
    XhtmlH5TypeValue,
    XhtmlH6TypeValue,
    XhtmlHeadingTypeValue,
    XhtmlHrTypeValue,
    XhtmlKbdTypeValue,
    XhtmlLiTypeValue,
    XhtmlObjectTypeValue,
    XhtmlOlTypeValue,
    XhtmlPTypeValue,
    XhtmlPreTypeValue,
    XhtmlQTypeValue,
    XhtmlSampTypeValue,
    XhtmlSpanTypeValue,
    XhtmlStrongTypeValue,
    XhtmlTableTypeValue,
    XhtmlTbodyTypeValue,
    XhtmlTdTypeValue,
    XhtmlTfootTypeValue,
    XhtmlThTypeValue,
    XhtmlTheadTypeValue,
    XhtmlTrTypeValue,
    XhtmlUlTypeValue,
    XhtmlVarTypeValue,
)

__NAMESPACE__ = "http://www.w3.org/1999/xhtml"


class XhtmlParamTypeValuetype(Enum):
    DATA = "data"
    REF = "ref"
    OBJECT = "object"


@dataclass
class XhtmlBrType:
    class Meta:
        name = "xhtml.br.type"

    space: XhtmlBrTypeValue = field(
        init=False,
        default=XhtmlBrTypeValue.PRESERVE,
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

    space: XhtmlColTypeValue = field(
        init=False,
        default=XhtmlColTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
    align: Optional["XhtmlColType.Align"] = field(
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
    valign: Optional["XhtmlColType.Valign"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    class Align(Enum):
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


@dataclass
class XhtmlHrType:
    class Meta:
        name = "xhtml.hr.type"

    space: XhtmlHrTypeValue = field(
        init=False,
        default=XhtmlHrTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
    space: XhtmlOlTypeValue = field(
        init=False,
        default=XhtmlOlTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
    space: XhtmlColgroupTypeValue = field(
        init=False,
        default=XhtmlColgroupTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
    align: Optional["XhtmlColgroupType.Align"] = field(
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
    valign: Optional["XhtmlColgroupType.Valign"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    class Align(Enum):
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


@dataclass
class XhtmlQType:
    class Meta:
        name = "xhtml.q.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List["XhtmlStrongType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List["XhtmlDfnType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List["XhtmlCodeType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List["XhtmlSampType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List["XhtmlKbdType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List["XhtmlVarType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List["XhtmlCiteType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List["XhtmlAbbrType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List["XhtmlAcronymType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List["XhtmlQType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlQTypeValue = field(
        init=False,
        default=XhtmlQTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
    cite_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "cite",
            "type": "Attribute",
        }
    )


@dataclass
class XhtmlAcronymType:
    class Meta:
        name = "xhtml.acronym.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List["XhtmlStrongType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List["XhtmlDfnType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List["XhtmlCodeType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List["XhtmlSampType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List["XhtmlKbdType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List["XhtmlVarType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List["XhtmlCiteType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List["XhtmlAbbrType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List["XhtmlAcronymType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlAcronymTypeValue = field(
        init=False,
        default=XhtmlAcronymTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlAbbrType:
    class Meta:
        name = "xhtml.abbr.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List["XhtmlStrongType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List["XhtmlDfnType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List["XhtmlCodeType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List["XhtmlSampType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List["XhtmlKbdType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List["XhtmlVarType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List["XhtmlCiteType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List["XhtmlAbbrType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlAbbrTypeValue = field(
        init=False,
        default=XhtmlAbbrTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlCiteType:
    class Meta:
        name = "xhtml.cite.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List["XhtmlStrongType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List["XhtmlDfnType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List["XhtmlCodeType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List["XhtmlSampType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List["XhtmlKbdType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List["XhtmlVarType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List["XhtmlCiteType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlCiteTypeValue = field(
        init=False,
        default=XhtmlCiteTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlVarType:
    class Meta:
        name = "xhtml.var.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List["XhtmlStrongType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List["XhtmlDfnType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List["XhtmlCodeType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List["XhtmlSampType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List["XhtmlKbdType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List["XhtmlVarType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlVarTypeValue = field(
        init=False,
        default=XhtmlVarTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlKbdType:
    class Meta:
        name = "xhtml.kbd.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List["XhtmlStrongType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List["XhtmlDfnType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List["XhtmlCodeType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List["XhtmlSampType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List["XhtmlKbdType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlKbdTypeValue = field(
        init=False,
        default=XhtmlKbdTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlSampType:
    class Meta:
        name = "xhtml.samp.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List["XhtmlStrongType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List["XhtmlDfnType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List["XhtmlCodeType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List["XhtmlSampType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlSampTypeValue = field(
        init=False,
        default=XhtmlSampTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlCodeType:
    class Meta:
        name = "xhtml.code.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List["XhtmlStrongType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List["XhtmlDfnType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List["XhtmlCodeType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlCodeTypeValue = field(
        init=False,
        default=XhtmlCodeTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlDfnType:
    class Meta:
        name = "xhtml.dfn.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List["XhtmlStrongType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List["XhtmlDfnType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlDfnTypeValue = field(
        init=False,
        default=XhtmlDfnTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlStrongType:
    class Meta:
        name = "xhtml.strong.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List["XhtmlStrongType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlStrongTypeValue = field(
        init=False,
        default=XhtmlStrongTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlCaptionType:
    class Meta:
        name = "xhtml.caption.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlCaptionTypeValue = field(
        init=False,
        default=XhtmlCaptionTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlDtType:
    class Meta:
        name = "xhtml.dt.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlDtTypeValue = field(
        init=False,
        default=XhtmlDtTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlH2Type:
    class Meta:
        name = "xhtml.h2.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlH2TypeValue = field(
        init=False,
        default=XhtmlH2TypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlH3Type:
    class Meta:
        name = "xhtml.h3.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlH3TypeValue = field(
        init=False,
        default=XhtmlH3TypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlH4Type:
    class Meta:
        name = "xhtml.h4.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlH4TypeValue = field(
        init=False,
        default=XhtmlH4TypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlH5Type:
    class Meta:
        name = "xhtml.h5.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlH5TypeValue = field(
        init=False,
        default=XhtmlH5TypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlH6Type:
    class Meta:
        name = "xhtml.h6.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlH6TypeValue = field(
        init=False,
        default=XhtmlH6TypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlPType:
    class Meta:
        name = "xhtml.p.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlPTypeValue = field(
        init=False,
        default=XhtmlPTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlPreType:
    class Meta:
        name = "xhtml.pre.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
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
    space: XhtmlPreTypeValue = field(
        init=False,
        default=XhtmlPreTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlDdType:
    class Meta:
        name = "xhtml.dd.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
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
    table: List["XhtmlTableType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlDdTypeValue = field(
        init=False,
        default=XhtmlDdTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlDlType:
    class Meta:
        name = "xhtml.dl.type"

    dt: List[XhtmlDtType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    dd: List[XhtmlDdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    space: XhtmlDlTypeValue = field(
        init=False,
        default=XhtmlDlTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlTdType:
    class Meta:
        name = "xhtml.td.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
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
    dl: List[XhtmlDlType] = field(
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
    table: List["XhtmlTableType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlTdTypeValue = field(
        init=False,
        default=XhtmlTdTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
    abbr_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "abbr",
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
    scope: Optional["XhtmlTdType.Scope"] = field(
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
    align: Optional["XhtmlTdType.Align"] = field(
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
    valign: Optional["XhtmlTdType.Valign"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    class Scope(Enum):
        ROW = "row"
        COL = "col"
        ROWGROUP = "rowgroup"
        COLGROUP = "colgroup"

    class Align(Enum):
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


@dataclass
class XhtmlThType:
    class Meta:
        name = "xhtml.th.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
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
    dl: List[XhtmlDlType] = field(
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
    table: List["XhtmlTableType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlThTypeValue = field(
        init=False,
        default=XhtmlThTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
    abbr_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "abbr",
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
    scope: Optional["XhtmlThType.Scope"] = field(
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
    align: Optional["XhtmlThType.Align"] = field(
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
    valign: Optional["XhtmlThType.Valign"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    class Scope(Enum):
        ROW = "row"
        COL = "col"
        ROWGROUP = "rowgroup"
        COLGROUP = "colgroup"

    class Align(Enum):
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


@dataclass
class XhtmlTrType:
    class Meta:
        name = "xhtml.tr.type"

    th: List[XhtmlThType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    td: List[XhtmlTdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    space: XhtmlTrTypeValue = field(
        init=False,
        default=XhtmlTrTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
    align: Optional["XhtmlTrType.Align"] = field(
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
    valign: Optional["XhtmlTrType.Valign"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    class Align(Enum):
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


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
    space: XhtmlTbodyTypeValue = field(
        init=False,
        default=XhtmlTbodyTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
    align: Optional["XhtmlTbodyType.Align"] = field(
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
    valign: Optional["XhtmlTbodyType.Valign"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    class Align(Enum):
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


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
    space: XhtmlTfootTypeValue = field(
        init=False,
        default=XhtmlTfootTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
    align: Optional["XhtmlTfootType.Align"] = field(
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
    valign: Optional["XhtmlTfootType.Valign"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    class Align(Enum):
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


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
    space: XhtmlTheadTypeValue = field(
        init=False,
        default=XhtmlTheadTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
    align: Optional["XhtmlTheadType.Align"] = field(
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
    valign: Optional["XhtmlTheadType.Valign"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    class Align(Enum):
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


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
    space: XhtmlTableTypeValue = field(
        init=False,
        default=XhtmlTableTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
    frame: Optional["XhtmlTableType.Frame"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rules: Optional["XhtmlTableType.Rules"] = field(
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

    class Frame(Enum):
        VOID = "void"
        ABOVE = "above"
        BELOW = "below"
        HSIDES = "hsides"
        LHS = "lhs"
        RHS = "rhs"
        VSIDES = "vsides"
        BOX = "box"
        BORDER = "border"

    class Rules(Enum):
        NONE_VALUE = "none"
        GROUPS = "groups"
        ROWS = "rows"
        COLS = "cols"
        ALL = "all"


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
    dl: List[XhtmlDlType] = field(
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
    space: XhtmlBlockquoteTypeValue = field(
        init=False,
        default=XhtmlBlockquoteTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
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
    dl: List[XhtmlDlType] = field(
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
    blockquote: List[XhtmlBlockquoteType] = field(
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
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlDivTypeValue = field(
        init=False,
        default=XhtmlDivTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
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
    dl: List[XhtmlDlType] = field(
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
    div: List[XhtmlDivType] = field(
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
    blockquote: List[XhtmlBlockquoteType] = field(
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
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List["XhtmlObjectType"] = field(
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
    space: XhtmlLiTypeValue = field(
        init=False,
        default=XhtmlLiTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
    space: XhtmlUlTypeValue = field(
        init=False,
        default=XhtmlUlTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlObjectType:
    class Meta:
        name = "xhtml.object.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    param: List[XhtmlParamType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    h1: List["XhtmlH1Type"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    h2: List[XhtmlH2Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    h3: List[XhtmlH3Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    h4: List[XhtmlH4Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    h5: List[XhtmlH5Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    h6: List[XhtmlH6Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    ul: List[XhtmlUlType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    ol: List[XhtmlOlType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    dl: List[XhtmlDlType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    p: List[XhtmlPType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    div: List[XhtmlDivType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    pre: List[XhtmlPreType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    blockquote: List[XhtmlBlockquoteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    address: List["XhtmlAddressType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    hr: List[XhtmlHrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    table: List[XhtmlTableType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata={
            "name": "del",
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
            "sequential": True,
        }
    )
    space: XhtmlObjectTypeValue = field(
        init=False,
        default=XhtmlObjectTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
    declare: Optional["XhtmlObjectType.Declare"] = field(
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

    class Declare(Enum):
        DECLARE = "declare"


@dataclass
class XhtmlAType:
    class Meta:
        name = "xhtml.a.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List[XhtmlObjectType] = field(
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
    space: XhtmlATypeValue = field(
        init=False,
        default=XhtmlATypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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


@dataclass
class XhtmlInlPresType:
    class Meta:
        name = "xhtml.InlPres.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List[XhtmlAType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List[XhtmlObjectType] = field(
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
    space: XhtmlInlPresTypeValue = field(
        init=False,
        default=XhtmlInlPresTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlEmType:
    class Meta:
        name = "xhtml.em.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List[XhtmlAType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List[XhtmlObjectType] = field(
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
    space: XhtmlEmTypeValue = field(
        init=False,
        default=XhtmlEmTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlH1Type:
    class Meta:
        name = "xhtml.h1.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List[XhtmlEmType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List[XhtmlAType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List[XhtmlObjectType] = field(
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
    space: XhtmlH1TypeValue = field(
        init=False,
        default=XhtmlH1TypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    h1: List[XhtmlH1Type] = field(
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
    ul: List[XhtmlUlType] = field(
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
    dl: List[XhtmlDlType] = field(
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
    div: List[XhtmlDivType] = field(
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
    blockquote: List[XhtmlBlockquoteType] = field(
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
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List[XhtmlEmType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List[XhtmlAType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List[XhtmlObjectType] = field(
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
    space: XhtmlEditTypeValue = field(
        init=False,
        default=XhtmlEditTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
    cite_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "cite",
            "type": "Attribute",
        }
    )
    datetime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class XhtmlSpanType:
    class Meta:
        name = "xhtml.span.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List[XhtmlEmType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List[XhtmlAType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List[XhtmlObjectType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    ins: List[XhtmlEditType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    del_value: List[XhtmlEditType] = field(
        default_factory=list,
        metadata={
            "name": "del",
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    space: XhtmlSpanTypeValue = field(
        init=False,
        default=XhtmlSpanTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlAddressType:
    class Meta:
        name = "xhtml.address.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List[XhtmlSpanType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List[XhtmlEmType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List[XhtmlAType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List[XhtmlObjectType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    ins: List[XhtmlEditType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    del_value: List[XhtmlEditType] = field(
        default_factory=list,
        metadata={
            "name": "del",
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    space: XhtmlAddressTypeValue = field(
        init=False,
        default=XhtmlAddressTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
class XhtmlHeadingType:
    class Meta:
        name = "xhtml.heading.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    span: List[XhtmlSpanType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    em: List[XhtmlEmType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    tt: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    i: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    b: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    big: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    small: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sub: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    sup: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    a: List[XhtmlAType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    object: List[XhtmlObjectType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    ins: List[XhtmlEditType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    del_value: List[XhtmlEditType] = field(
        default_factory=list,
        metadata={
            "name": "del",
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    space: XhtmlHeadingTypeValue = field(
        init=False,
        default=XhtmlHeadingTypeValue.PRESERVE,
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
    lang: Optional[str] = field(
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
