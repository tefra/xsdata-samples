from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional
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


class XhtmlParamAttlistValuetype(Enum):
    """
    :cvar DATA:
    :cvar REF:
    :cvar OBJECT:
    """
    DATA = "data"
    REF = "ref"
    OBJECT = "object"


class XhtmlParamTypeValuetype(Enum):
    """
    :cvar DATA:
    :cvar REF:
    :cvar OBJECT:
    """
    DATA = "data"
    REF = "ref"
    OBJECT = "object"


@dataclass
class XhtmlBrType:
    """
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    """
    class Meta:
        name = "xhtml.br.type"

    space: XhtmlBrTypeValue = field(
        init=False,
        default=XhtmlBrTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlColType:
    """
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    :ivar span:
    :ivar width:
    :ivar align:
    :ivar char:
    :ivar charoff:
    :ivar valign:
    """
    class Meta:
        name = "xhtml.col.type"

    space: XhtmlColTypeValue = field(
        init=False,
        default=XhtmlColTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    span: int = field(
        default=1,
        metadata=dict(
            type="Attribute"
        )
    )
    width: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            pattern=r"\d*\*"
        )
    )
    align: Optional["XhtmlColType.Align"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    char: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            length=1
        )
    )
    charoff: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            pattern=r"\d+[%]|\d*\.\d+[%]"
        )
    )
    valign: Optional["XhtmlColType.Valign"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Align(Enum):
        """
        :cvar LEFT:
        :cvar CENTER:
        :cvar RIGHT:
        :cvar JUSTIFY:
        :cvar CHAR:
        """
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        """
        :cvar TOP:
        :cvar MIDDLE:
        :cvar BOTTOM:
        :cvar BASELINE:
        """
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


@dataclass
class XhtmlHrType:
    """
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.hr.type"

    space: XhtmlHrTypeValue = field(
        init=False,
        default=XhtmlHrTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlOlType:
    """
    :ivar li:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.ol.type"

    li: List["XhtmlLiType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlOlTypeValue = field(
        init=False,
        default=XhtmlOlTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlParamType:
    """
    :ivar id:
    :ivar name:
    :ivar value:
    :ivar valuetype:
    :ivar type:
    """
    class Meta:
        name = "xhtml.param.type"

    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    valuetype: XhtmlParamTypeValuetype = field(
        default=XhtmlParamTypeValuetype.DATA,
        metadata=dict(
            type="Attribute"
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlColgroupType:
    """
    :ivar col:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    :ivar span:
    :ivar width:
    :ivar align:
    :ivar char:
    :ivar charoff:
    :ivar valign:
    """
    class Meta:
        name = "xhtml.colgroup.type"

    col: List[XhtmlColType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlColgroupTypeValue = field(
        init=False,
        default=XhtmlColgroupTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    span: int = field(
        default=1,
        metadata=dict(
            type="Attribute"
        )
    )
    width: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            pattern=r"\d*\*"
        )
    )
    align: Optional["XhtmlColgroupType.Align"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    char: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            length=1
        )
    )
    charoff: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            pattern=r"\d+[%]|\d*\.\d+[%]"
        )
    )
    valign: Optional["XhtmlColgroupType.Valign"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Align(Enum):
        """
        :cvar LEFT:
        :cvar CENTER:
        :cvar RIGHT:
        :cvar JUSTIFY:
        :cvar CHAR:
        """
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        """
        :cvar TOP:
        :cvar MIDDLE:
        :cvar BOTTOM:
        :cvar BASELINE:
        """
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


@dataclass
class XhtmlQType:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    :ivar cite_attribute:
    """
    class Meta:
        name = "xhtml.q.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List["XhtmlStrongType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List["XhtmlDfnType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List["XhtmlCodeType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List["XhtmlSampType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List["XhtmlKbdType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List["XhtmlVarType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List["XhtmlCiteType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List["XhtmlAbbrType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List["XhtmlAcronymType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List["XhtmlQType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlQTypeValue = field(
        init=False,
        default=XhtmlQTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    cite_attribute: Optional[str] = field(
        default=None,
        metadata=dict(
            name="cite",
            type="Attribute"
        )
    )


@dataclass
class XhtmlAcronymType:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.acronym.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List["XhtmlStrongType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List["XhtmlDfnType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List["XhtmlCodeType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List["XhtmlSampType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List["XhtmlKbdType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List["XhtmlVarType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List["XhtmlCiteType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List["XhtmlAbbrType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List["XhtmlAcronymType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlAcronymTypeValue = field(
        init=False,
        default=XhtmlAcronymTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlAbbrType:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.abbr.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List["XhtmlStrongType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List["XhtmlDfnType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List["XhtmlCodeType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List["XhtmlSampType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List["XhtmlKbdType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List["XhtmlVarType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List["XhtmlCiteType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List["XhtmlAbbrType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlAbbrTypeValue = field(
        init=False,
        default=XhtmlAbbrTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlCiteType:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.cite.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List["XhtmlStrongType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List["XhtmlDfnType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List["XhtmlCodeType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List["XhtmlSampType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List["XhtmlKbdType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List["XhtmlVarType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List["XhtmlCiteType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlCiteTypeValue = field(
        init=False,
        default=XhtmlCiteTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlVarType:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.var.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List["XhtmlStrongType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List["XhtmlDfnType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List["XhtmlCodeType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List["XhtmlSampType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List["XhtmlKbdType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List["XhtmlVarType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlVarTypeValue = field(
        init=False,
        default=XhtmlVarTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlKbdType:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.kbd.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List["XhtmlStrongType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List["XhtmlDfnType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List["XhtmlCodeType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List["XhtmlSampType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List["XhtmlKbdType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlKbdTypeValue = field(
        init=False,
        default=XhtmlKbdTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlSampType:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.samp.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List["XhtmlStrongType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List["XhtmlDfnType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List["XhtmlCodeType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List["XhtmlSampType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlSampTypeValue = field(
        init=False,
        default=XhtmlSampTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlCodeType:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.code.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List["XhtmlStrongType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List["XhtmlDfnType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List["XhtmlCodeType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlCodeTypeValue = field(
        init=False,
        default=XhtmlCodeTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlDfnType:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.dfn.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List["XhtmlStrongType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List["XhtmlDfnType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlDfnTypeValue = field(
        init=False,
        default=XhtmlDfnTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlStrongType:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.strong.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List["XhtmlStrongType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlStrongTypeValue = field(
        init=False,
        default=XhtmlStrongTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlCaptionType:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.caption.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlCaptionTypeValue = field(
        init=False,
        default=XhtmlCaptionTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlDtType:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.dt.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlDtTypeValue = field(
        init=False,
        default=XhtmlDtTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlH2Type:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.h2.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlH2TypeValue = field(
        init=False,
        default=XhtmlH2TypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlH3Type:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.h3.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlH3TypeValue = field(
        init=False,
        default=XhtmlH3TypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlH4Type:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.h4.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlH4TypeValue = field(
        init=False,
        default=XhtmlH4TypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlH5Type:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.h5.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlH5TypeValue = field(
        init=False,
        default=XhtmlH5TypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlH6Type:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.h6.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlH6TypeValue = field(
        init=False,
        default=XhtmlH6TypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlPType:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.p.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlPTypeValue = field(
        init=False,
        default=XhtmlPTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlPreType:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar a:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.pre.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlPreTypeValue = field(
        init=False,
        default=XhtmlPreTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlDdType:
    """
    :ivar content:
    :ivar h1:
    :ivar h2:
    :ivar h3:
    :ivar h4:
    :ivar h5:
    :ivar h6:
    :ivar ul:
    :ivar ol:
    :ivar dl:
    :ivar p:
    :ivar div:
    :ivar pre:
    :ivar blockquote:
    :ivar address:
    :ivar hr:
    :ivar table:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.dd.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h1: List["XhtmlH1Type"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h2: List[XhtmlH2Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h3: List[XhtmlH3Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h4: List[XhtmlH4Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h5: List[XhtmlH5Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h6: List[XhtmlH6Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ul: List["XhtmlUlType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ol: List[XhtmlOlType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dl: List["XhtmlDlType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    p: List[XhtmlPType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    div: List["XhtmlDivType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    pre: List[XhtmlPreType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    blockquote: List["XhtmlBlockquoteType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    address: List["XhtmlAddressType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    hr: List[XhtmlHrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    table: List["XhtmlTableType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlDdTypeValue = field(
        init=False,
        default=XhtmlDdTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlDlType:
    """
    :ivar dt:
    :ivar dd:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.dl.type"

    dt: List[XhtmlDtType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dd: List[XhtmlDdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlDlTypeValue = field(
        init=False,
        default=XhtmlDlTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlTdType:
    """
    :ivar content:
    :ivar h1:
    :ivar h2:
    :ivar h3:
    :ivar h4:
    :ivar h5:
    :ivar h6:
    :ivar ul:
    :ivar ol:
    :ivar dl:
    :ivar p:
    :ivar div:
    :ivar pre:
    :ivar blockquote:
    :ivar address:
    :ivar hr:
    :ivar table:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    :ivar abbr_attribute:
    :ivar axis:
    :ivar headers:
    :ivar scope:
    :ivar rowspan:
    :ivar colspan:
    :ivar align:
    :ivar char:
    :ivar charoff:
    :ivar valign:
    """
    class Meta:
        name = "xhtml.td.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h1: List["XhtmlH1Type"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h2: List[XhtmlH2Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h3: List[XhtmlH3Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h4: List[XhtmlH4Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h5: List[XhtmlH5Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h6: List[XhtmlH6Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ul: List["XhtmlUlType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ol: List[XhtmlOlType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dl: List[XhtmlDlType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    p: List[XhtmlPType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    div: List["XhtmlDivType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    pre: List[XhtmlPreType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    blockquote: List["XhtmlBlockquoteType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    address: List["XhtmlAddressType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    hr: List[XhtmlHrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    table: List["XhtmlTableType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlTdTypeValue = field(
        init=False,
        default=XhtmlTdTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    abbr_attribute: Optional[str] = field(
        default=None,
        metadata=dict(
            name="abbr",
            type="Attribute"
        )
    )
    axis: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    headers: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    scope: Optional["XhtmlTdType.Scope"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    rowspan: int = field(
        default=1,
        metadata=dict(
            type="Attribute"
        )
    )
    colspan: int = field(
        default=1,
        metadata=dict(
            type="Attribute"
        )
    )
    align: Optional["XhtmlTdType.Align"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    char: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            length=1
        )
    )
    charoff: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            pattern=r"\d+[%]|\d*\.\d+[%]"
        )
    )
    valign: Optional["XhtmlTdType.Valign"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Scope(Enum):
        """
        :cvar ROW:
        :cvar COL:
        :cvar ROWGROUP:
        :cvar COLGROUP:
        """
        ROW = "row"
        COL = "col"
        ROWGROUP = "rowgroup"
        COLGROUP = "colgroup"

    class Align(Enum):
        """
        :cvar LEFT:
        :cvar CENTER:
        :cvar RIGHT:
        :cvar JUSTIFY:
        :cvar CHAR:
        """
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        """
        :cvar TOP:
        :cvar MIDDLE:
        :cvar BOTTOM:
        :cvar BASELINE:
        """
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


@dataclass
class XhtmlThType:
    """
    :ivar content:
    :ivar h1:
    :ivar h2:
    :ivar h3:
    :ivar h4:
    :ivar h5:
    :ivar h6:
    :ivar ul:
    :ivar ol:
    :ivar dl:
    :ivar p:
    :ivar div:
    :ivar pre:
    :ivar blockquote:
    :ivar address:
    :ivar hr:
    :ivar table:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    :ivar abbr_attribute:
    :ivar axis:
    :ivar headers:
    :ivar scope:
    :ivar rowspan:
    :ivar colspan:
    :ivar align:
    :ivar char:
    :ivar charoff:
    :ivar valign:
    """
    class Meta:
        name = "xhtml.th.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h1: List["XhtmlH1Type"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h2: List[XhtmlH2Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h3: List[XhtmlH3Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h4: List[XhtmlH4Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h5: List[XhtmlH5Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h6: List[XhtmlH6Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ul: List["XhtmlUlType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ol: List[XhtmlOlType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dl: List[XhtmlDlType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    p: List[XhtmlPType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    div: List["XhtmlDivType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    pre: List[XhtmlPreType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    blockquote: List["XhtmlBlockquoteType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    address: List["XhtmlAddressType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    hr: List[XhtmlHrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    table: List["XhtmlTableType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlThTypeValue = field(
        init=False,
        default=XhtmlThTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    abbr_attribute: Optional[str] = field(
        default=None,
        metadata=dict(
            name="abbr",
            type="Attribute"
        )
    )
    axis: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    headers: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    scope: Optional["XhtmlThType.Scope"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    rowspan: int = field(
        default=1,
        metadata=dict(
            type="Attribute"
        )
    )
    colspan: int = field(
        default=1,
        metadata=dict(
            type="Attribute"
        )
    )
    align: Optional["XhtmlThType.Align"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    char: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            length=1
        )
    )
    charoff: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            pattern=r"\d+[%]|\d*\.\d+[%]"
        )
    )
    valign: Optional["XhtmlThType.Valign"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Scope(Enum):
        """
        :cvar ROW:
        :cvar COL:
        :cvar ROWGROUP:
        :cvar COLGROUP:
        """
        ROW = "row"
        COL = "col"
        ROWGROUP = "rowgroup"
        COLGROUP = "colgroup"

    class Align(Enum):
        """
        :cvar LEFT:
        :cvar CENTER:
        :cvar RIGHT:
        :cvar JUSTIFY:
        :cvar CHAR:
        """
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        """
        :cvar TOP:
        :cvar MIDDLE:
        :cvar BOTTOM:
        :cvar BASELINE:
        """
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


@dataclass
class XhtmlTrType:
    """
    :ivar th:
    :ivar td:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    :ivar align:
    :ivar char:
    :ivar charoff:
    :ivar valign:
    """
    class Meta:
        name = "xhtml.tr.type"

    th: List[XhtmlThType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    td: List[XhtmlTdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlTrTypeValue = field(
        init=False,
        default=XhtmlTrTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    align: Optional["XhtmlTrType.Align"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    char: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            length=1
        )
    )
    charoff: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            pattern=r"\d+[%]|\d*\.\d+[%]"
        )
    )
    valign: Optional["XhtmlTrType.Valign"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Align(Enum):
        """
        :cvar LEFT:
        :cvar CENTER:
        :cvar RIGHT:
        :cvar JUSTIFY:
        :cvar CHAR:
        """
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        """
        :cvar TOP:
        :cvar MIDDLE:
        :cvar BOTTOM:
        :cvar BASELINE:
        """
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


@dataclass
class XhtmlTbodyType:
    """
    :ivar tr:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    :ivar align:
    :ivar char:
    :ivar charoff:
    :ivar valign:
    """
    class Meta:
        name = "xhtml.tbody.type"

    tr: List[XhtmlTrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlTbodyTypeValue = field(
        init=False,
        default=XhtmlTbodyTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    align: Optional["XhtmlTbodyType.Align"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    char: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            length=1
        )
    )
    charoff: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            pattern=r"\d+[%]|\d*\.\d+[%]"
        )
    )
    valign: Optional["XhtmlTbodyType.Valign"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Align(Enum):
        """
        :cvar LEFT:
        :cvar CENTER:
        :cvar RIGHT:
        :cvar JUSTIFY:
        :cvar CHAR:
        """
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        """
        :cvar TOP:
        :cvar MIDDLE:
        :cvar BOTTOM:
        :cvar BASELINE:
        """
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


@dataclass
class XhtmlTfootType:
    """
    :ivar tr:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    :ivar align:
    :ivar char:
    :ivar charoff:
    :ivar valign:
    """
    class Meta:
        name = "xhtml.tfoot.type"

    tr: List[XhtmlTrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlTfootTypeValue = field(
        init=False,
        default=XhtmlTfootTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    align: Optional["XhtmlTfootType.Align"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    char: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            length=1
        )
    )
    charoff: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            pattern=r"\d+[%]|\d*\.\d+[%]"
        )
    )
    valign: Optional["XhtmlTfootType.Valign"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Align(Enum):
        """
        :cvar LEFT:
        :cvar CENTER:
        :cvar RIGHT:
        :cvar JUSTIFY:
        :cvar CHAR:
        """
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        """
        :cvar TOP:
        :cvar MIDDLE:
        :cvar BOTTOM:
        :cvar BASELINE:
        """
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


@dataclass
class XhtmlTheadType:
    """
    :ivar tr:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    :ivar align:
    :ivar char:
    :ivar charoff:
    :ivar valign:
    """
    class Meta:
        name = "xhtml.thead.type"

    tr: List[XhtmlTrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlTheadTypeValue = field(
        init=False,
        default=XhtmlTheadTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    align: Optional["XhtmlTheadType.Align"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    char: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            length=1
        )
    )
    charoff: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            pattern=r"\d+[%]|\d*\.\d+[%]"
        )
    )
    valign: Optional["XhtmlTheadType.Valign"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Align(Enum):
        """
        :cvar LEFT:
        :cvar CENTER:
        :cvar RIGHT:
        :cvar JUSTIFY:
        :cvar CHAR:
        """
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        """
        :cvar TOP:
        :cvar MIDDLE:
        :cvar BOTTOM:
        :cvar BASELINE:
        """
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


@dataclass
class XhtmlTableType:
    """
    :ivar caption:
    :ivar col:
    :ivar colgroup:
    :ivar thead:
    :ivar tfoot:
    :ivar tbody:
    :ivar tr:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    :ivar summary:
    :ivar width:
    :ivar border:
    :ivar frame:
    :ivar rules:
    :ivar cellspacing:
    :ivar cellpadding:
    """
    class Meta:
        name = "xhtml.table.type"

    caption: Optional[XhtmlCaptionType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    col: List[XhtmlColType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    colgroup: List[XhtmlColgroupType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    thead: Optional[XhtmlTheadType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    tfoot: Optional[XhtmlTfootType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    tbody: List[XhtmlTbodyType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    tr: List[XhtmlTrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlTableTypeValue = field(
        init=False,
        default=XhtmlTableTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    summary: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    width: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            pattern=r"\d+[%]|\d*\.\d+[%]"
        )
    )
    border: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    frame: Optional["XhtmlTableType.Frame"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    rules: Optional["XhtmlTableType.Rules"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    cellspacing: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            pattern=r"\d+[%]|\d*\.\d+[%]"
        )
    )
    cellpadding: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            pattern=r"\d+[%]|\d*\.\d+[%]"
        )
    )

    class Frame(Enum):
        """
        :cvar VOID:
        :cvar ABOVE:
        :cvar BELOW:
        :cvar HSIDES:
        :cvar LHS:
        :cvar RHS:
        :cvar VSIDES:
        :cvar BOX:
        :cvar BORDER:
        """
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
        """
        :cvar NONE_VALUE:
        :cvar GROUPS:
        :cvar ROWS:
        :cvar COLS:
        :cvar ALL:
        """
        NONE_VALUE = "none"
        GROUPS = "groups"
        ROWS = "rows"
        COLS = "cols"
        ALL = "all"


@dataclass
class XhtmlBlockquoteType:
    """
    :ivar h1:
    :ivar h2:
    :ivar h3:
    :ivar h4:
    :ivar h5:
    :ivar h6:
    :ivar ul:
    :ivar ol:
    :ivar dl:
    :ivar p:
    :ivar div:
    :ivar pre:
    :ivar blockquote:
    :ivar address:
    :ivar hr:
    :ivar table:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    :ivar cite:
    """
    class Meta:
        name = "xhtml.blockquote.type"

    h1: List["XhtmlH1Type"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h2: List[XhtmlH2Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h3: List[XhtmlH3Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h4: List[XhtmlH4Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h5: List[XhtmlH5Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h6: List[XhtmlH6Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ul: List["XhtmlUlType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ol: List[XhtmlOlType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dl: List[XhtmlDlType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    p: List[XhtmlPType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    div: List["XhtmlDivType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    pre: List[XhtmlPreType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    blockquote: List["XhtmlBlockquoteType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    address: List["XhtmlAddressType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    hr: List[XhtmlHrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    table: List[XhtmlTableType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlBlockquoteTypeValue = field(
        init=False,
        default=XhtmlBlockquoteTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    cite: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlDivType:
    """
    :ivar content:
    :ivar h1:
    :ivar h2:
    :ivar h3:
    :ivar h4:
    :ivar h5:
    :ivar h6:
    :ivar ul:
    :ivar ol:
    :ivar dl:
    :ivar p:
    :ivar div:
    :ivar pre:
    :ivar blockquote:
    :ivar address:
    :ivar hr:
    :ivar table:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.div.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h1: List["XhtmlH1Type"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h2: List[XhtmlH2Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h3: List[XhtmlH3Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h4: List[XhtmlH4Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h5: List[XhtmlH5Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h6: List[XhtmlH6Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ul: List["XhtmlUlType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ol: List[XhtmlOlType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dl: List[XhtmlDlType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    p: List[XhtmlPType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    div: List["XhtmlDivType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    pre: List[XhtmlPreType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    blockquote: List[XhtmlBlockquoteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    address: List["XhtmlAddressType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    hr: List[XhtmlHrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    table: List[XhtmlTableType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlDivTypeValue = field(
        init=False,
        default=XhtmlDivTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlLiType:
    """
    :ivar content:
    :ivar h1:
    :ivar h2:
    :ivar h3:
    :ivar h4:
    :ivar h5:
    :ivar h6:
    :ivar ul:
    :ivar ol:
    :ivar dl:
    :ivar p:
    :ivar div:
    :ivar pre:
    :ivar blockquote:
    :ivar address:
    :ivar hr:
    :ivar table:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.li.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h1: List["XhtmlH1Type"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h2: List[XhtmlH2Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h3: List[XhtmlH3Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h4: List[XhtmlH4Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h5: List[XhtmlH5Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h6: List[XhtmlH6Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ul: List["XhtmlUlType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ol: List[XhtmlOlType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dl: List[XhtmlDlType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    p: List[XhtmlPType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    div: List[XhtmlDivType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    pre: List[XhtmlPreType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    blockquote: List[XhtmlBlockquoteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    address: List["XhtmlAddressType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    hr: List[XhtmlHrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    table: List[XhtmlTableType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List["XhtmlAType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List["XhtmlObjectType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlLiTypeValue = field(
        init=False,
        default=XhtmlLiTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlUlType:
    """
    :ivar li:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.ul.type"

    li: List[XhtmlLiType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlUlTypeValue = field(
        init=False,
        default=XhtmlUlTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlObjectType:
    """
    :ivar content:
    :ivar param:
    :ivar h1:
    :ivar h2:
    :ivar h3:
    :ivar h4:
    :ivar h5:
    :ivar h6:
    :ivar ul:
    :ivar ol:
    :ivar dl:
    :ivar p:
    :ivar div:
    :ivar pre:
    :ivar blockquote:
    :ivar address:
    :ivar hr:
    :ivar table:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    :ivar declare:
    :ivar classid:
    :ivar codebase:
    :ivar data:
    :ivar type:
    :ivar codetype:
    :ivar archive:
    :ivar standby:
    :ivar height:
    :ivar width:
    :ivar name:
    :ivar tabindex:
    """
    class Meta:
        name = "xhtml.object.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    param: List[XhtmlParamType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h1: Optional["XhtmlH1Type"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    h2: Optional[XhtmlH2Type] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    h3: Optional[XhtmlH3Type] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    h4: Optional[XhtmlH4Type] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    h5: Optional[XhtmlH5Type] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    h6: Optional[XhtmlH6Type] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    ul: Optional[XhtmlUlType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    ol: Optional[XhtmlOlType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    dl: Optional[XhtmlDlType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    p: Optional[XhtmlPType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    div: Optional[XhtmlDivType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    pre: Optional[XhtmlPreType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    blockquote: Optional[XhtmlBlockquoteType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    address: Optional["XhtmlAddressType"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    hr: Optional[XhtmlHrType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            required=True
        )
    )
    table: Optional[XhtmlTableType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    br: Optional[XhtmlBrType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    span: Optional["XhtmlSpanType"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    em: Optional["XhtmlEmType"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    strong: Optional[XhtmlStrongType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    dfn: Optional[XhtmlDfnType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    code: Optional[XhtmlCodeType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    samp: Optional[XhtmlSampType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    kbd: Optional[XhtmlKbdType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    var: Optional[XhtmlVarType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    cite: Optional[XhtmlCiteType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    abbr: Optional[XhtmlAbbrType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    acronym: Optional[XhtmlAcronymType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    q: Optional[XhtmlQType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    tt: Optional["XhtmlInlPresType"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    i: Optional["XhtmlInlPresType"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    b: Optional["XhtmlInlPresType"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    big: Optional["XhtmlInlPresType"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    small: Optional["XhtmlInlPresType"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    sub: Optional["XhtmlInlPresType"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    sup: Optional["XhtmlInlPresType"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    a: Optional["XhtmlAType"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            required=True
        )
    )
    object: Optional["XhtmlObjectType"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    ins: Optional["XhtmlEditType"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    del_value: Optional["XhtmlEditType"] = field(
        default=None,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    space: XhtmlObjectTypeValue = field(
        init=False,
        default=XhtmlObjectTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    declare: Optional["XhtmlObjectType.Declare"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    classid: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    codebase: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    data: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    codetype: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    archive: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Attribute",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    standby: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    height: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            pattern=r"\d+[%]|\d*\.\d+[%]"
        )
    )
    width: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            pattern=r"\d+[%]|\d*\.\d+[%]"
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    tabindex: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Declare(Enum):
        """
        :cvar DECLARE:
        """
        DECLARE = "declare"


@dataclass
class XhtmlAType:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    :ivar href:
    :ivar charset:
    :ivar type:
    :ivar hreflang:
    :ivar rel:
    :ivar rev:
    :ivar accesskey:
    :ivar tabindex:
    """
    class Meta:
        name = "xhtml.a.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List[XhtmlObjectType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlATypeValue = field(
        init=False,
        default=XhtmlATypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    href: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    charset: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    rel: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Attribute",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    rev: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Attribute",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    accesskey: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            length=1
        )
    )
    tabindex: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlInlPresType:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.InlPres.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List["XhtmlInlPresType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List[XhtmlAType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List[XhtmlObjectType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlInlPresTypeValue = field(
        init=False,
        default=XhtmlInlPresTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlEmType:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.em.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List["XhtmlEmType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List[XhtmlAType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List[XhtmlObjectType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlEmTypeValue = field(
        init=False,
        default=XhtmlEmTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlH1Type:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.h1.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List[XhtmlEmType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List[XhtmlAType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List[XhtmlObjectType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlH1TypeValue = field(
        init=False,
        default=XhtmlH1TypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlEditType:
    """
    :ivar content:
    :ivar h1:
    :ivar h2:
    :ivar h3:
    :ivar h4:
    :ivar h5:
    :ivar h6:
    :ivar ul:
    :ivar ol:
    :ivar dl:
    :ivar p:
    :ivar div:
    :ivar pre:
    :ivar blockquote:
    :ivar address:
    :ivar hr:
    :ivar table:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    :ivar cite_attribute:
    :ivar datetime:
    """
    class Meta:
        name = "xhtml.edit.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h1: List[XhtmlH1Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h2: List[XhtmlH2Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h3: List[XhtmlH3Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h4: List[XhtmlH4Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h5: List[XhtmlH5Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    h6: List[XhtmlH6Type] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ul: List[XhtmlUlType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ol: List[XhtmlOlType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dl: List[XhtmlDlType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    p: List[XhtmlPType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    div: List[XhtmlDivType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    pre: List[XhtmlPreType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    blockquote: List[XhtmlBlockquoteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    address: List["XhtmlAddressType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    hr: List[XhtmlHrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    table: List[XhtmlTableType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List[XhtmlEmType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List[XhtmlAType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List[XhtmlObjectType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List["XhtmlEditType"] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlEditTypeValue = field(
        init=False,
        default=XhtmlEditTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    cite_attribute: Optional[str] = field(
        default=None,
        metadata=dict(
            name="cite",
            type="Attribute"
        )
    )
    datetime: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlSpanType:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.span.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List["XhtmlSpanType"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List[XhtmlEmType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List[XhtmlAType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List[XhtmlObjectType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List[XhtmlEditType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List[XhtmlEditType] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlSpanTypeValue = field(
        init=False,
        default=XhtmlSpanTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlAddressType:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.address.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List[XhtmlSpanType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List[XhtmlEmType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List[XhtmlAType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List[XhtmlObjectType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List[XhtmlEditType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List[XhtmlEditType] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlAddressTypeValue = field(
        init=False,
        default=XhtmlAddressTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class XhtmlHeadingType:
    """
    :ivar content:
    :ivar br:
    :ivar span:
    :ivar em:
    :ivar strong:
    :ivar dfn:
    :ivar code:
    :ivar samp:
    :ivar kbd:
    :ivar var:
    :ivar cite:
    :ivar abbr:
    :ivar acronym:
    :ivar q:
    :ivar tt:
    :ivar i:
    :ivar b:
    :ivar big:
    :ivar small:
    :ivar sub:
    :ivar sup:
    :ivar a:
    :ivar object:
    :ivar ins:
    :ivar del_value:
    :ivar space:
    :ivar id:
    :ivar class_value:
    :ivar title:
    :ivar lang:
    :ivar style:
    """
    class Meta:
        name = "xhtml.heading.type"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[XhtmlBrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    span: List[XhtmlSpanType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    em: List[XhtmlEmType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strong: List[XhtmlStrongType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dfn: List[XhtmlDfnType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: List[XhtmlCodeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    samp: List[XhtmlSampType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kbd: List[XhtmlKbdType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    var: List[XhtmlVarType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cite: List[XhtmlCiteType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    abbr: List[XhtmlAbbrType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    acronym: List[XhtmlAcronymType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    q: List[XhtmlQType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    tt: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    i: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    big: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List[XhtmlInlPresType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List[XhtmlAType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    object: List[XhtmlObjectType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ins: List[XhtmlEditType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    del_value: List[XhtmlEditType] = field(
        default_factory=list,
        metadata=dict(
            name="del",
            type="Element",
            namespace="http://www.w3.org/1999/xhtml",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    space: XhtmlHeadingTypeValue = field(
        init=False,
        default=XhtmlHeadingTypeValue.PRESERVE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    class_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="class",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
