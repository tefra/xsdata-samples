from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.warning_type import WarningType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class WarningsType:
    warning: list[WarningType] = field(
        default_factory=list,
        metadata={
            "name": "Warning",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
        },
    )
