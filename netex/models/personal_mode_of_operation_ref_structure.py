from __future__ import annotations

from dataclasses import dataclass

from .mode_of_operation_ref_structure import ModeOfOperationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PersonalModeOfOperationRefStructure(ModeOfOperationRefStructure):
    pass
