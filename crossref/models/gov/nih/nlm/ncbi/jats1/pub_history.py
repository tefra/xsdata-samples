from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.event import Event

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass(kw_only=True)
class PubHistory:
    """
    <div> <h3>Publication History</h3> </div>.
    """

    class Meta:
        name = "pub-history"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    event: list[Event] = field(
        default_factory=list,
        metadata={
            "type": "Element",
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
