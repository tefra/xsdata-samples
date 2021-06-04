from dataclasses import dataclass
from netex.models.purpose_of_grouping_ref_structure import PurposeOfGroupingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PurposeOfGroupingRef(PurposeOfGroupingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
