from __future__ import annotations

from dataclasses import dataclass, field

from .conventional_mode_of_operation_value_structure import (
    ConventionalModeOfOperationValueStructure,
)
from .scheduled_operation_type_enumeration import (
    ScheduledOperationTypeEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ScheduledModeOfOperationValueStructure(
    ConventionalModeOfOperationValueStructure
):
    class Meta:
        name = "ScheduledModeOfOperation_ValueStructure"

    scheduled_operation_type: ScheduledOperationTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "ScheduledOperationType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
