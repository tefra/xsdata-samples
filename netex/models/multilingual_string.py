from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MultilingualString:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    text_id_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "textIdType",
            "type": "Attribute",
        },
    )
