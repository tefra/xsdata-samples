from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.gov.nih.nlm.ncbi.jats1.annotation import (
    PublisherLoc,
    PublisherName,
)

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class Publisher:
    """
    <div> <h3>Publisher</h3> </div>
    """
    class Meta:
        name = "publisher"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    publisher_name: List[PublisherName] = field(
        default_factory=list,
        metadata={
            "name": "publisher-name",
            "type": "Element",
            "sequence": 1,
        }
    )
    publisher_loc: List[PublisherLoc] = field(
        default_factory=list,
        metadata={
            "name": "publisher-loc",
            "type": "Element",
            "sequence": 1,
        }
    )
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
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
