from dataclasses import dataclass
from .purpose_of_grouping_value_structure import PurposeOfGroupingValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PurposeOfGrouping(PurposeOfGroupingValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
