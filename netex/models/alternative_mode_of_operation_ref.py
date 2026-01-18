from __future__ import annotations

from dataclasses import dataclass

from .alternative_mode_of_operation_ref_structure import (
    AlternativeModeOfOperationRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AlternativeModeOfOperationRef(AlternativeModeOfOperationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
