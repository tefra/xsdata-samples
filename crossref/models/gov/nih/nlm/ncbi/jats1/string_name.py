from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.degrees import Degrees
from crossref.models.gov.nih.nlm.ncbi.jats1.given_names import GivenNames
from crossref.models.gov.nih.nlm.ncbi.jats1.prefix import Prefix
from crossref.models.gov.nih.nlm.ncbi.jats1.string_name_name_style import (
    StringNameNameStyle,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.suffix import Suffix
from crossref.models.gov.nih.nlm.ncbi.jats1.surname import Surname
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class StringName:
    """
    <div> <h3>Name of Person (Unstructured)</h3> </div>.
    """

    class Meta:
        name = "string-name"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

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
    name_style: StringNameNameStyle = field(
        default=StringNameNameStyle.WESTERN,
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
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "degrees",
                    "type": Degrees,
                },
                {
                    "name": "given-names",
                    "type": GivenNames,
                },
                {
                    "name": "prefix",
                    "type": Prefix,
                },
                {
                    "name": "surname",
                    "type": Surname,
                },
                {
                    "name": "suffix",
                    "type": Suffix,
                },
            ),
        },
    )
