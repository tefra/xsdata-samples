from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class RedirectEntry:
    class Meta:
        name = "redirectEntry"
        namespace = "urn:vpro:api:2013"

    from_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Attribute",
        }
    )
    to: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    ultimate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    circular: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
