from dataclasses import dataclass, field
from typing import List, Optional, Union
from crossref.models.gov.nih.nlm.ncbi.jats1.annotation import (
    AddrLine,
    Bold,
    ExtLink,
    FixedCase,
    Institution,
    InstitutionWrap,
    Italic,
    Label,
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
from crossref.models.gov.nih.nlm.ncbi.jats1.city import City
from crossref.models.gov.nih.nlm.ncbi.jats1.country import Country
from crossref.models.gov.nih.nlm.ncbi.jats1.email import Email
from crossref.models.gov.nih.nlm.ncbi.jats1.fax import Fax
from crossref.models.gov.nih.nlm.ncbi.jats1.phone import Phone
from crossref.models.gov.nih.nlm.ncbi.jats1.postal_code import PostalCode
from crossref.models.gov.nih.nlm.ncbi.jats1.state import State
from crossref.models.gov.nih.nlm.ncbi.jats1.uri import Uri
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class Corresp:
    """<div>

    <h3>Correspondence Information</h3> </div>
    """
    class Meta:
        name = "corresp"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
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
                    "name": "addr-line",
                    "type": AddrLine,
                },
                {
                    "name": "city",
                    "type": City,
                },
                {
                    "name": "country",
                    "type": Country,
                },
                {
                    "name": "fax",
                    "type": Fax,
                },
                {
                    "name": "institution",
                    "type": Institution,
                },
                {
                    "name": "institution-wrap",
                    "type": InstitutionWrap,
                },
                {
                    "name": "phone",
                    "type": Phone,
                },
                {
                    "name": "postal-code",
                    "type": PostalCode,
                },
                {
                    "name": "state",
                    "type": State,
                },
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
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
                    "name": "label",
                    "type": Label,
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
        }
    )
