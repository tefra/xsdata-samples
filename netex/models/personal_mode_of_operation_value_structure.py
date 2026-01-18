from __future__ import annotations

from dataclasses import dataclass, field

from .mode_of_operation_value_structure import ModeOfOperationValueStructure
from .personal_operation_type_enumeration import (
    PersonalOperationTypeEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PersonalModeOfOperationValueStructure(ModeOfOperationValueStructure):
    class Meta:
        name = "PersonalModeOfOperation_ValueStructure"

    personal_operation_type: PersonalOperationTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "PersonalOperationType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
