from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import ForwardRef

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class StrucDocBr:
    class Meta:
        name = "StrucDoc.Br"


class StrucDocColAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class StrucDocColValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class StrucDocColgroupAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class StrucDocColgroupValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class StrucDocContentRevised(Enum):
    INSERT = "insert"
    DELETE = "delete"


@dataclass
class StrucDocFootnoteRef:
    class Meta:
        name = "StrucDoc.FootnoteRef"

    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        },
    )
    idref: None | str = field(
        default=None,
        metadata={
            "name": "IDREF",
            "type": "Attribute",
            "required": True,
        },
    )


class StrucDocListListType(Enum):
    ORDERED = "ordered"
    UNORDERED = "unordered"


@dataclass
class StrucDocSub:
    class Meta:
        name = "StrucDoc.Sub"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class StrucDocSup:
    class Meta:
        name = "StrucDoc.Sup"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


class StrucDocTableFrame(Enum):
    VOID = "void"
    ABOVE = "above"
    BELOW = "below"
    HSIDES = "hsides"
    LHS = "lhs"
    RHS = "rhs"
    VSIDES = "vsides"
    BOX = "box"
    BORDER = "border"


class StrucDocTableRules(Enum):
    NONE = "none"
    GROUPS = "groups"
    ROWS = "rows"
    COLS = "cols"
    ALL = "all"


class StrucDocTbodyAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class StrucDocTbodyValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class StrucDocTdAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class StrucDocTdScope(Enum):
    ROW = "row"
    COL = "col"
    ROWGROUP = "rowgroup"
    COLGROUP = "colgroup"


class StrucDocTdValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class StrucDocTfootAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class StrucDocTfootValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class StrucDocThAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class StrucDocThScope(Enum):
    ROW = "row"
    COL = "col"
    ROWGROUP = "rowgroup"
    COLGROUP = "colgroup"


class StrucDocThValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class StrucDocTheadAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class StrucDocTheadValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class StrucDocTrAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class StrucDocTrValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


@dataclass
class StrucDocCaption:
    class Meta:
        name = "StrucDoc.Caption"

    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
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
                    "name": "linkHtml",
                    "type": ForwardRef("StrucDocLinkHtml"),
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sub",
                    "type": StrucDocSub,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sup",
                    "type": StrucDocSup,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnote",
                    "type": ForwardRef("StrucDocFootnote"),
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnoteRef",
                    "type": StrucDocFootnoteRef,
                    "namespace": "urn:hl7-org:v3",
                },
            ),
        },
    )


@dataclass
class StrucDocCol:
    class Meta:
        name = "StrucDoc.Col"

    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        },
    )
    span: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    width: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: None | StrucDocColAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: None | StrucDocColValign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class StrucDocTitleContent:
    class Meta:
        name = "StrucDoc.TitleContent"

    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
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
                    "name": "content",
                    "type": ForwardRef("StrucDocTitleContent"),
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sub",
                    "type": StrucDocSub,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sup",
                    "type": StrucDocSup,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "br",
                    "type": StrucDocBr,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnote",
                    "type": ForwardRef("StrucDocTitleFootnote"),
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnoteRef",
                    "type": StrucDocFootnoteRef,
                    "namespace": "urn:hl7-org:v3",
                },
            ),
        },
    )


@dataclass
class StrucDocColgroup:
    class Meta:
        name = "StrucDoc.Colgroup"

    col: list[StrucDocCol] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        },
    )
    span: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    width: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: None | StrucDocColgroupAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: None | StrucDocColgroupValign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class StrucDocRenderMultiMedia:
    class Meta:
        name = "StrucDoc.RenderMultiMedia"

    caption: None | StrucDocCaption = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    referenced_object: list[str] = field(
        default_factory=list,
        metadata={
            "name": "referencedObject",
            "type": "Attribute",
            "tokens": True,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass
class StrucDocTitleFootnote:
    class Meta:
        name = "StrucDoc.TitleFootnote"

    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
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
                    "name": "content",
                    "type": StrucDocTitleContent,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sub",
                    "type": StrucDocSub,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sup",
                    "type": StrucDocSup,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "br",
                    "type": StrucDocBr,
                    "namespace": "urn:hl7-org:v3",
                },
            ),
        },
    )


@dataclass
class StrucDocContent:
    class Meta:
        name = "StrucDoc.Content"

    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        },
    )
    revised: None | StrucDocContentRevised = field(
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
                    "name": "content",
                    "type": ForwardRef("StrucDocContent"),
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "linkHtml",
                    "type": ForwardRef("StrucDocLinkHtml"),
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sub",
                    "type": StrucDocSub,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sup",
                    "type": StrucDocSup,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "br",
                    "type": StrucDocBr,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnote",
                    "type": ForwardRef("StrucDocFootnote"),
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnoteRef",
                    "type": StrucDocFootnoteRef,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "renderMultiMedia",
                    "type": StrucDocRenderMultiMedia,
                    "namespace": "urn:hl7-org:v3",
                },
            ),
        },
    )


@dataclass
class StrucDocTitle:
    class Meta:
        name = "StrucDoc.Title"

    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        },
    )
    media_type: str = field(
        init=False,
        default="text/x-hl7-title+xml",
        metadata={
            "name": "mediaType",
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
                    "name": "content",
                    "type": StrucDocTitleContent,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sub",
                    "type": StrucDocSub,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sup",
                    "type": StrucDocSup,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "br",
                    "type": StrucDocBr,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnote",
                    "type": StrucDocTitleFootnote,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnoteRef",
                    "type": StrucDocFootnoteRef,
                    "namespace": "urn:hl7-org:v3",
                },
            ),
        },
    )


@dataclass
class StrucDocFootnote:
    class Meta:
        name = "StrucDoc.Footnote"

    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
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
                    "name": "content",
                    "type": StrucDocContent,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "linkHtml",
                    "type": ForwardRef("StrucDocLinkHtml"),
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sub",
                    "type": StrucDocSub,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sup",
                    "type": StrucDocSup,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "br",
                    "type": StrucDocBr,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "renderMultiMedia",
                    "type": StrucDocRenderMultiMedia,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "paragraph",
                    "type": ForwardRef("StrucDocParagraph"),
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "list",
                    "type": ForwardRef("StrucDocList"),
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "table",
                    "type": ForwardRef("StrucDocTable"),
                    "namespace": "urn:hl7-org:v3",
                },
            ),
        },
    )


@dataclass
class StrucDocLinkHtml:
    class Meta:
        name = "StrucDoc.LinkHtml"

    name: None | str = field(
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
    rel: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rev: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
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
                    "name": "footnote",
                    "type": StrucDocFootnote,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnoteRef",
                    "type": StrucDocFootnoteRef,
                    "namespace": "urn:hl7-org:v3",
                },
            ),
        },
    )


@dataclass
class StrucDocParagraph:
    class Meta:
        name = "StrucDoc.Paragraph"

    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
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
                    "name": "caption",
                    "type": StrucDocCaption,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "content",
                    "type": StrucDocContent,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "linkHtml",
                    "type": StrucDocLinkHtml,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sub",
                    "type": StrucDocSub,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sup",
                    "type": StrucDocSup,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "br",
                    "type": StrucDocBr,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnote",
                    "type": StrucDocFootnote,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnoteRef",
                    "type": StrucDocFootnoteRef,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "renderMultiMedia",
                    "type": StrucDocRenderMultiMedia,
                    "namespace": "urn:hl7-org:v3",
                },
            ),
        },
    )


@dataclass
class StrucDocTh:
    class Meta:
        name = "StrucDoc.Th"

    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
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
    scope: None | StrucDocThScope = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rowspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    colspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    align: None | StrucDocThAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: None | StrucDocThValign = field(
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
                    "name": "content",
                    "type": StrucDocContent,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "linkHtml",
                    "type": StrucDocLinkHtml,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sub",
                    "type": StrucDocSub,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sup",
                    "type": StrucDocSup,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "br",
                    "type": StrucDocBr,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnote",
                    "type": StrucDocFootnote,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnoteRef",
                    "type": StrucDocFootnoteRef,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "renderMultiMedia",
                    "type": StrucDocRenderMultiMedia,
                    "namespace": "urn:hl7-org:v3",
                },
            ),
        },
    )


@dataclass
class StrucDocItem:
    class Meta:
        name = "StrucDoc.Item"

    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
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
                    "name": "caption",
                    "type": StrucDocCaption,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "content",
                    "type": StrucDocContent,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "linkHtml",
                    "type": StrucDocLinkHtml,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sub",
                    "type": StrucDocSub,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sup",
                    "type": StrucDocSup,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "br",
                    "type": StrucDocBr,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnote",
                    "type": StrucDocFootnote,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnoteRef",
                    "type": StrucDocFootnoteRef,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "renderMultiMedia",
                    "type": StrucDocRenderMultiMedia,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "paragraph",
                    "type": StrucDocParagraph,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "list",
                    "type": ForwardRef("StrucDocList"),
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "table",
                    "type": ForwardRef("StrucDocTable"),
                    "namespace": "urn:hl7-org:v3",
                },
            ),
        },
    )


@dataclass
class StrucDocList:
    class Meta:
        name = "StrucDoc.List"

    caption: None | StrucDocCaption = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    item: list[StrucDocItem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        },
    )
    list_type: StrucDocListListType = field(
        default=StrucDocListListType.UNORDERED,
        metadata={
            "name": "listType",
            "type": "Attribute",
        },
    )


@dataclass
class StrucDocTd:
    class Meta:
        name = "StrucDoc.Td"

    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
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
    scope: None | StrucDocTdScope = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rowspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    colspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    align: None | StrucDocTdAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: None | StrucDocTdValign = field(
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
                    "name": "content",
                    "type": StrucDocContent,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "linkHtml",
                    "type": StrucDocLinkHtml,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sub",
                    "type": StrucDocSub,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sup",
                    "type": StrucDocSup,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "br",
                    "type": StrucDocBr,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnote",
                    "type": StrucDocFootnote,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnoteRef",
                    "type": StrucDocFootnoteRef,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "renderMultiMedia",
                    "type": StrucDocRenderMultiMedia,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "paragraph",
                    "type": StrucDocParagraph,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "list",
                    "type": StrucDocList,
                    "namespace": "urn:hl7-org:v3",
                },
            ),
        },
    )


@dataclass
class StrucDocTr:
    class Meta:
        name = "StrucDoc.Tr"

    th: list[StrucDocTh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    td: list[StrucDocTd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        },
    )
    align: None | StrucDocTrAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: None | StrucDocTrValign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class StrucDocTbody:
    class Meta:
        name = "StrucDoc.Tbody"

    tr: list[StrucDocTr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        },
    )
    align: None | StrucDocTbodyAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: None | StrucDocTbodyValign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class StrucDocTfoot:
    class Meta:
        name = "StrucDoc.Tfoot"

    tr: list[StrucDocTr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        },
    )
    align: None | StrucDocTfootAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: None | StrucDocTfootValign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class StrucDocThead:
    class Meta:
        name = "StrucDoc.Thead"

    tr: list[StrucDocTr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        },
    )
    align: None | StrucDocTheadAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: None | StrucDocTheadValign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class StrucDocTable:
    class Meta:
        name = "StrucDoc.Table"

    caption: None | StrucDocCaption = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    col: list[StrucDocCol] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    colgroup: list[StrucDocColgroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    thead: None | StrucDocThead = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    tfoot: None | StrucDocTfoot = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    tbody: list[StrucDocTbody] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
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
        },
    )
    border: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    frame: None | StrucDocTableFrame = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rules: None | StrucDocTableRules = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cellspacing: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cellpadding: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class StrucDocText:
    class Meta:
        name = "StrucDoc.Text"

    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        },
    )
    media_type: str = field(
        init=False,
        default="text/x-hl7-text+xml",
        metadata={
            "name": "mediaType",
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
                    "name": "content",
                    "type": StrucDocContent,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "linkHtml",
                    "type": StrucDocLinkHtml,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sub",
                    "type": StrucDocSub,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sup",
                    "type": StrucDocSup,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "br",
                    "type": StrucDocBr,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnote",
                    "type": StrucDocFootnote,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnoteRef",
                    "type": StrucDocFootnoteRef,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "renderMultiMedia",
                    "type": StrucDocRenderMultiMedia,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "paragraph",
                    "type": StrucDocParagraph,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "list",
                    "type": StrucDocList,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "table",
                    "type": StrucDocTable,
                    "namespace": "urn:hl7-org:v3",
                },
            ),
        },
    )
