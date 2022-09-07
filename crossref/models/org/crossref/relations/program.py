from dataclasses import dataclass, field
from typing import List
from crossref.models.org.crossref.relations.related_item import RelatedItem

__NAMESPACE__ = "http://www.crossref.org/relations.xsd"


@dataclass
class Program:
    """
    Wrapper element for relationship metadata.
    """
    class Meta:
        name = "program"
        namespace = "http://www.crossref.org/relations.xsd"

    related_item: List[RelatedItem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    name: str = field(
        init=False,
        default="relations",
        metadata={
            "type": "Attribute",
        }
    )
