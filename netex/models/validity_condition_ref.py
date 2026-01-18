from __future__ import annotations

from dataclasses import dataclass

from .validity_condition_ref_structure import ValidityConditionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidityConditionRef(ValidityConditionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
