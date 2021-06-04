from dataclasses import dataclass
from netex.models.type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingAlgorithmTypeValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "TimingAlgorithmType_ValueStructure"
