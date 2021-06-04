from dataclasses import dataclass
from netex.models.series_constraint_ref_structure_1 import SeriesConstraintRefStructure1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SeriesConstraintRefStructure2(SeriesConstraintRefStructure1):
    class Meta:
        name = "SeriesConstraintRefStructure"
