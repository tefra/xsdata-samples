from __future__ import annotations

from dataclasses import dataclass

from .check_constraint_ref_structure import CheckConstraintRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CheckConstraintRef(CheckConstraintRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
