from dataclasses import dataclass
from netex.models.interchange_ref_structure import InterchangeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InterchangeRef(InterchangeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
