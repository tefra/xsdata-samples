from dataclasses import dataclass
from .object_filter_by_value_structure import ObjectFilterByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ObjectFilterByValue(ObjectFilterByValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
