from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.contrib_id_authenticated import (
    ContribIdAuthenticated,
)
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass(kw_only=True)
class ContribId:
    """
    <div> <h3>Contributor Identifier</h3> </div>.
    """

    class Meta:
        name = "contrib-id"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    assigning_authority: None | str = field(
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
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    contrib_id_type: None | str = field(
        default=None,
        metadata={
            "name": "contrib-id-type",
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
        },
    )
