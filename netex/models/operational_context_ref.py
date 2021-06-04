from dataclasses import dataclass
from netex.models.operational_context_ref_structure import OperationalContextRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OperationalContextRef(OperationalContextRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
