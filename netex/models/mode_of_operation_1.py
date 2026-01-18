from __future__ import annotations

from dataclasses import dataclass

from .mode_of_operation_value_structure import ModeOfOperationValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ModeOfOperation1(ModeOfOperationValueStructure):
    class Meta:
        name = "ModeOfOperation"
        namespace = "http://www.netex.org.uk/netex"
