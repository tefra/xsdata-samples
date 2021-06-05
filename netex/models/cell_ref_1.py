from dataclasses import dataclass
from netex.models.cell_ref_structure import CellRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CellRef1(CellRefStructure):
    class Meta:
        name = "CellRef"
        namespace = "http://www.netex.org.uk/netex"
