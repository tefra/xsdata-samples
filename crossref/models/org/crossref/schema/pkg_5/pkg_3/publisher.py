from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Publisher:
    """
    A container for information about the publisher of the item being
    registered.
    """
    class Meta:
        name = "publisher"
        namespace = "http://www.crossref.org/schema/5.3.1"

    publisher_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        }
    )
    publisher_place: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 2,
            "max_length": 255,
        }
    )
