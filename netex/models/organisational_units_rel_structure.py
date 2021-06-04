from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.organisational_unit import OrganisationalUnit
from netex.models.organisational_unit_ref import OrganisationalUnitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OrganisationalUnitsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "organisationalUnits_RelStructure"

    organisational_unit_ref: List[OrganisationalUnitRef] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    organisational_unit: List[OrganisationalUnit] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationalUnit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
