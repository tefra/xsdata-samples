from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://docs.oasis-open.org/wsrf/bf-2"


@dataclass
class BaseFaultTypeFaultCause:
    class Meta:
        global_type = False

    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
