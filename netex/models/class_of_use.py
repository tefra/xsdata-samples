from dataclasses import dataclass
from netex.models.class_of_use_value_structure import ClassOfUseValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ClassOfUse(ClassOfUseValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
