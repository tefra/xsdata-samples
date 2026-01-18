from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.contrib_id_authenticated import (
    ContribIdAuthenticated,
)
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class ContribId:
    """
    <div> <h3>Contributor Identifier</h3> </div>.
    """

    class Meta:
        name = "contrib-id"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    assigning_authority: str | None = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        },
    )
    authenticated: ContribIdAuthenticated = field(
        default=ContribIdAuthenticated.FALSE,
        metadata={
            "type": "Attribute",
        },
    )
    content_type: str | None = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    contrib_id_type: str | None = field(
        default=None,
        metadata={
            "name": "contrib-id-type",
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
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
