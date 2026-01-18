from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import (
    Label,
    P,
    Sec,
    Title,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.object_id import ObjectId
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class TransAbstract:
    """
    <div> <h3>Translated Abstract</h3> </div>.
    """

    class Meta:
        name = "trans-abstract"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    label: Label | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: Title | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sec: list[Sec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    abstract_type: str | None = field(
        default=None,
        metadata={
            "name": "abstract-type",
            "type": "Attribute",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
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
