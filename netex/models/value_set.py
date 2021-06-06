from dataclasses import dataclass
from .value_set_version_structure import ValueSetVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ValueSet(ValueSetVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
