from dataclasses import dataclass
from netex.models.type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PurposeOfJourneyPartitionValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "PurposeOfJourneyPartition_ValueStructure"
