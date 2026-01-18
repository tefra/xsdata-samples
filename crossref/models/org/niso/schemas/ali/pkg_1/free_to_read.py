from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.niso.org/schemas/ali/1.0/"


@dataclass
class FreeToRead:
    """
    <div> <h3>Free to Read (Niso Ali)</h3> </div>.
    """

    class Meta:
        name = "free_to_read"
        namespace = "http://www.niso.org/schemas/ali/1.0/"

    content_type: str | None = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    end_date: str | None = field(
        default=None,
        metadata={
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
    start_date: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
