from __future__ import annotations

from dataclasses import dataclass

from .alternative_mode_of_operation_value_structure import (
    AlternativeModeOfOperationValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AlternativeModeOfOperation(AlternativeModeOfOperationValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
