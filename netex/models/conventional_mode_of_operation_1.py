from __future__ import annotations

from dataclasses import dataclass

from .conventional_mode_of_operation_value_structure import (
    ConventionalModeOfOperationValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ConventionalModeOfOperation1(ConventionalModeOfOperationValueStructure):
    class Meta:
        name = "ConventionalModeOfOperation"
        namespace = "http://www.netex.org.uk/netex"
