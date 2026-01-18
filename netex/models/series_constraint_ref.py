from __future__ import annotations

from dataclasses import dataclass

from .series_constraint_ref_structure_1 import SeriesConstraintRefStructure1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SeriesConstraintRef(SeriesConstraintRefStructure1):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
