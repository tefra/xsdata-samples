from dataclasses import dataclass, field
from typing import Optional, Union

from crossref.models.gov.nih.nlm.ncbi.jats1.given_names import GivenNames
from crossref.models.gov.nih.nlm.ncbi.jats1.name_name_style import (
    NameNameStyle,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.prefix import Prefix
from crossref.models.gov.nih.nlm.ncbi.jats1.suffix import Suffix
from crossref.models.gov.nih.nlm.ncbi.jats1.surname import Surname
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class Name:
    """
    <div> <h3>Name of Person (Structured)</h3> </div>.
    """

    class Meta:
        name = "name"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    surname: Surname | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    given_names: list[GivenNames] = field(
        default_factory=list,
        metadata={
            "name": "given-names",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    prefix: Prefix | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    suffix: Suffix | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    content_type: str | None = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    name_style: NameNameStyle = field(
        default=NameNameStyle.WESTERN,
        metadata={
            "name": "name-style",
            "type": "Attribute",
        },
    )
    specific_use: str | None = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: str | LangValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
