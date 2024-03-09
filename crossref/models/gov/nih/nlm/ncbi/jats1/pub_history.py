from dataclasses import dataclass, field
from typing import List, Optional

from crossref.models.gov.nih.nlm.ncbi.jats1.event import Event

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class PubHistory:
    """
    <div> <h3>Publication History</h3> </div>
    """

    class Meta:
        name = "pub-history"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    event: List[Event] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
