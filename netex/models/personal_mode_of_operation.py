from __future__ import annotations

from dataclasses import dataclass

from .personal_mode_of_operation_value_structure import (
    PersonalModeOfOperationValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PersonalModeOfOperation(PersonalModeOfOperationValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
