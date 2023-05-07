from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class Issn:
    """
    <div> <h3>Issn</h3> </div>
    """
    class Meta:
        name = "issn"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    assigning_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
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
    pub_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "pub-type",
            "type": "Attribute",
        }
    )
    publication_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "publication-format",
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
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
