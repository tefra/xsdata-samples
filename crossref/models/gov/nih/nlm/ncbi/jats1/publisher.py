from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import (
    PublisherLoc,
    PublisherName,
)

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass(kw_only=True)
class Publisher:
    """
    <div> <h3>Publisher</h3> </div>.
    """

    class Meta:
        name = "publisher"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    publisher_name: list[PublisherName] = field(
        default_factory=list,
        metadata={
            "name": "publisher-name",
            "type": "Element",
            "sequence": 1,
        },
    )
    publisher_loc: list[PublisherLoc] = field(
        default_factory=list,
        metadata={
            "name": "publisher-loc",
            "type": "Element",
            "sequence": 1,
        },
    )
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
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
