from dataclasses import dataclass

from .series_constraint_ref_structure_2 import SeriesConstraintRefStructure2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SeriesConstraintRefStructure1(SeriesConstraintRefStructure2):
    class Meta:
        name = "SeriesConstraintRefStructure"
