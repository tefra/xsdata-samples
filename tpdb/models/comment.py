from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDate


@dataclass
class Comment:
    class Meta:
        name = "comment"

    author: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )