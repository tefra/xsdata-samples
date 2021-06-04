from dataclasses import dataclass
from netex.models.series_constraint_ref_structure_2 import SeriesConstraintRefStructure2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SeriesConstraintRef(SeriesConstraintRefStructure2):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
