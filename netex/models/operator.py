from dataclasses import dataclass
from .operator_version_structure import OperatorVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Operator(OperatorVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
