from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.period_extended import PeriodExtended

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class PeriodExtensionType:
    class Meta:
        name = "_PeriodExtensionType"

    period_extended: None | PeriodExtended = field(
        default=None,
        metadata={
            "name": "periodExtended",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
