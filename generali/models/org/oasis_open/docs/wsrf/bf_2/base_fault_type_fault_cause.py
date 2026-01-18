from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://docs.oasis-open.org/wsrf/bf-2"


@dataclass
class BaseFaultTypeFaultCause:
    class Meta:
        global_type = False

    other_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
