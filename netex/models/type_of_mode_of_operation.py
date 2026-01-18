from __future__ import annotations

from dataclasses import dataclass

from .type_of_mode_of_operation_value_structure import (
    TypeOfModeOfOperationValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfModeOfOperation(TypeOfModeOfOperationValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
