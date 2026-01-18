from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import (
    Abbrev,
    Alternatives,
    Bold,
    ChemStruct,
    FixedCase,
    IndexTerm,
    InlineFormula,
    InlineMedia,
    Italic,
    Monospace,
    NamedContent,
    Overline,
    Roman,
    Ruby,
    SansSerif,
    Sc,
    Strike,
    StyledContent,
    Sub,
    Sup,
    Underline,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.index_term_range_end import (
    IndexTermRangeEnd,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.inline_graphic import InlineGraphic
from crossref.models.gov.nih.nlm.ncbi.jats1.milestone_end import MilestoneEnd
from crossref.models.gov.nih.nlm.ncbi.jats1.milestone_start import (
    MilestoneStart,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.private_char import PrivateChar
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass(kw_only=True)
class ConfTheme:
    """
    <div> <h3>Conference Theme</h3> </div>.
    """

    class Meta:
        name = "conf-theme"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
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
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        },
    )
