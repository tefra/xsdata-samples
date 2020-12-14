from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class StrucDocBr:
    class Meta:
        name = "StrucDoc.Br"


@dataclass
class StrucDocCol:
    class Meta:
        name = "StrucDoc.Col"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        }
    )
    span: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional["StrucDocCol.Align"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional["StrucDocCol.Valign"] = field(
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
class StrucDocFootnoteRef:
    class Meta:
        name = "StrucDoc.FootnoteRef"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        }
    )
    idref: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDREF",
            "type": "Attribute",
            "required": True,
        }
    )


class StrucDocListListType(Enum):
    ORDERED = "ordered"
    UNORDERED = "unordered"


@dataclass
class StrucDocSub:
    class Meta:
        name = "StrucDoc.Sub"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class StrucDocSup:
    class Meta:
        name = "StrucDoc.Sup"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class StrucDocCaption:
    class Meta:
        name = "StrucDoc.Caption"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    link_html: List["StrucDocLinkHtml"] = field(
        default_factory=list,
        metadata={
            "name": "linkHtml",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    sub: List[StrucDocSub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    sup: List[StrucDocSup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    footnote: List["StrucDocFootnote"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    footnote_ref: List[StrucDocFootnoteRef] = field(
        default_factory=list,
        metadata={
            "name": "footnoteRef",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class StrucDocColgroup:
    class Meta:
        name = "StrucDoc.Colgroup"

    col: List[StrucDocCol] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        }
    )
    span: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional["StrucDocColgroup.Align"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional["StrucDocColgroup.Valign"] = field(
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
class StrucDocTitleFootnote:
    class Meta:
        name = "StrucDoc.TitleFootnote"

    content_any: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    content: List["StrucDocTitleContent"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    sub: List[StrucDocSub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    sup: List[StrucDocSup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    br: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class StrucDocRenderMultiMedia:
    class Meta:
        name = "StrucDoc.RenderMultiMedia"

    caption: Optional[StrucDocCaption] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    referenced_object: List[str] = field(
        default_factory=list,
        metadata={
            "name": "referencedObject",
            "type": "Attribute",
            "required": True,
            "tokens": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class StrucDocTitleContent:
    class Meta:
        name = "StrucDoc.TitleContent"

    content_any: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    content: List["StrucDocTitleContent"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    sub: List[StrucDocSub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    sup: List[StrucDocSup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    br: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    footnote: List[StrucDocTitleFootnote] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    footnote_ref: List[StrucDocFootnoteRef] = field(
        default_factory=list,
        metadata={
            "name": "footnoteRef",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class StrucDocParagraph:
    class Meta:
        name = "StrucDoc.Paragraph"

    content_any: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    caption: Optional[StrucDocCaption] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    content: List["StrucDocContent"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    link_html: List["StrucDocLinkHtml"] = field(
        default_factory=list,
        metadata={
            "name": "linkHtml",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    sub: List[StrucDocSub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    sup: List[StrucDocSup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    br: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    footnote: List["StrucDocFootnote"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    footnote_ref: List[StrucDocFootnoteRef] = field(
        default_factory=list,
        metadata={
            "name": "footnoteRef",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    render_multi_media: List[StrucDocRenderMultiMedia] = field(
        default_factory=list,
        metadata={
            "name": "renderMultiMedia",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class StrucDocTh:
    class Meta:
        name = "StrucDoc.Th"

    content_any: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    content: List["StrucDocContent"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    link_html: List["StrucDocLinkHtml"] = field(
        default_factory=list,
        metadata={
            "name": "linkHtml",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    sub: List[StrucDocSub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    sup: List[StrucDocSup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    br: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    footnote: List["StrucDocFootnote"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    footnote_ref: List[StrucDocFootnoteRef] = field(
        default_factory=list,
        metadata={
            "name": "footnoteRef",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    render_multi_media: List[StrucDocRenderMultiMedia] = field(
        default_factory=list,
        metadata={
            "name": "renderMultiMedia",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
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
    scope: Optional["StrucDocTh.Scope"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rowspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        }
    )
    colspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional["StrucDocTh.Align"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional["StrucDocTh.Valign"] = field(
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
class StrucDocTitle:
    class Meta:
        name = "StrucDoc.Title"

    content_any: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    content: List[StrucDocTitleContent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    sub: List[StrucDocSub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    sup: List[StrucDocSup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    br: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    footnote: List[StrucDocTitleFootnote] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    footnote_ref: List[StrucDocFootnoteRef] = field(
        default_factory=list,
        metadata={
            "name": "footnoteRef",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        }
    )
    media_type: str = field(
        init=False,
        default="text/x-hl7-title+xml",
        metadata={
            "name": "mediaType",
            "type": "Attribute",
        }
    )


@dataclass
class StrucDocTd:
    class Meta:
        name = "StrucDoc.Td"

    content_any: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    content: List["StrucDocContent"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    link_html: List["StrucDocLinkHtml"] = field(
        default_factory=list,
        metadata={
            "name": "linkHtml",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    sub: List[StrucDocSub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    sup: List[StrucDocSup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    br: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    footnote: List["StrucDocFootnote"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    footnote_ref: List[StrucDocFootnoteRef] = field(
        default_factory=list,
        metadata={
            "name": "footnoteRef",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    render_multi_media: List[StrucDocRenderMultiMedia] = field(
        default_factory=list,
        metadata={
            "name": "renderMultiMedia",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    paragraph: List[StrucDocParagraph] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    list_value: List["StrucDocList"] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
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
    scope: Optional["StrucDocTd.Scope"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rowspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        }
    )
    colspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional["StrucDocTd.Align"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional["StrucDocTd.Valign"] = field(
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
class StrucDocTr:
    class Meta:
        name = "StrucDoc.Tr"

    th: List[StrucDocTh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    td: List[StrucDocTd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        }
    )
    align: Optional["StrucDocTr.Align"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional["StrucDocTr.Valign"] = field(
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
class StrucDocTbody:
    class Meta:
        name = "StrucDoc.Tbody"

    tr: List[StrucDocTr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        }
    )
    align: Optional["StrucDocTbody.Align"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional["StrucDocTbody.Valign"] = field(
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
class StrucDocTfoot:
    class Meta:
        name = "StrucDoc.Tfoot"

    tr: List[StrucDocTr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        }
    )
    align: Optional["StrucDocTfoot.Align"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional["StrucDocTfoot.Valign"] = field(
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
class StrucDocThead:
    class Meta:
        name = "StrucDoc.Thead"

    tr: List[StrucDocTr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        }
    )
    align: Optional["StrucDocThead.Align"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional["StrucDocThead.Valign"] = field(
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
class StrucDocTable:
    class Meta:
        name = "StrucDoc.Table"

    caption: Optional[StrucDocCaption] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    col: List[StrucDocCol] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    colgroup: List[StrucDocColgroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    thead: Optional[StrucDocThead] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    tfoot: Optional[StrucDocTfoot] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    tbody: List[StrucDocTbody] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
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
        }
    )
    border: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    frame: Optional["StrucDocTable.Frame"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rules: Optional["StrucDocTable.Rules"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    cellspacing: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    cellpadding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
class StrucDocItem:
    class Meta:
        name = "StrucDoc.Item"

    content_any: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    caption: Optional[StrucDocCaption] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    content: List["StrucDocContent"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    link_html: List["StrucDocLinkHtml"] = field(
        default_factory=list,
        metadata={
            "name": "linkHtml",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    sub: List[StrucDocSub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    sup: List[StrucDocSup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    br: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    footnote: List["StrucDocFootnote"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    footnote_ref: List[StrucDocFootnoteRef] = field(
        default_factory=list,
        metadata={
            "name": "footnoteRef",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    render_multi_media: List[StrucDocRenderMultiMedia] = field(
        default_factory=list,
        metadata={
            "name": "renderMultiMedia",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    paragraph: List[StrucDocParagraph] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    list_value: List["StrucDocList"] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    table: List[StrucDocTable] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class StrucDocList:
    class Meta:
        name = "StrucDoc.List"

    caption: Optional[StrucDocCaption] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    item: List[StrucDocItem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        }
    )
    list_type: StrucDocListListType = field(
        default=StrucDocListListType.UNORDERED,
        metadata={
            "name": "listType",
            "type": "Attribute",
        }
    )


@dataclass
class StrucDocFootnote:
    class Meta:
        name = "StrucDoc.Footnote"

    content_any: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    content: List["StrucDocContent"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    link_html: List["StrucDocLinkHtml"] = field(
        default_factory=list,
        metadata={
            "name": "linkHtml",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    sub: List[StrucDocSub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    sup: List[StrucDocSup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    br: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    render_multi_media: List[StrucDocRenderMultiMedia] = field(
        default_factory=list,
        metadata={
            "name": "renderMultiMedia",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    paragraph: List[StrucDocParagraph] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    list_value: List[StrucDocList] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    table: List[StrucDocTable] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class StrucDocLinkHtml:
    class Meta:
        name = "StrucDoc.LinkHtml"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    footnote: List[StrucDocFootnote] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    footnote_ref: List[StrucDocFootnoteRef] = field(
        default_factory=list,
        metadata={
            "name": "footnoteRef",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    name: Optional[str] = field(
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
    rel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rev: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class StrucDocContent:
    class Meta:
        name = "StrucDoc.Content"

    content_any: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    content: List["StrucDocContent"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    link_html: List[StrucDocLinkHtml] = field(
        default_factory=list,
        metadata={
            "name": "linkHtml",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    sub: List[StrucDocSub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    sup: List[StrucDocSup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    br: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    footnote: List[StrucDocFootnote] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    footnote_ref: List[StrucDocFootnoteRef] = field(
        default_factory=list,
        metadata={
            "name": "footnoteRef",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    render_multi_media: List[StrucDocRenderMultiMedia] = field(
        default_factory=list,
        metadata={
            "name": "renderMultiMedia",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        }
    )
    revised: Optional["StrucDocContent.Revised"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    class Revised(Enum):
        INSERT = "insert"
        DELETE = "delete"


@dataclass
class StrucDocText:
    class Meta:
        name = "StrucDoc.Text"

    content_any: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    content: List[StrucDocContent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    link_html: List[StrucDocLinkHtml] = field(
        default_factory=list,
        metadata={
            "name": "linkHtml",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    sub: List[StrucDocSub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    sup: List[StrucDocSup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    br: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    footnote: List[StrucDocFootnote] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    footnote_ref: List[StrucDocFootnoteRef] = field(
        default_factory=list,
        metadata={
            "name": "footnoteRef",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    render_multi_media: List[StrucDocRenderMultiMedia] = field(
        default_factory=list,
        metadata={
            "name": "renderMultiMedia",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    paragraph: List[StrucDocParagraph] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    list_value: List[StrucDocList] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    table: List[StrucDocTable] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        }
    )
    media_type: str = field(
        init=False,
        default="text/x-hl7-text+xml",
        metadata={
            "name": "mediaType",
            "type": "Attribute",
        }
    )
