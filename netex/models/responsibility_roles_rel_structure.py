from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .responsibility_role_ref import ResponsibilityRoleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResponsibilityRolesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "ResponsibilityRoles_RelStructure"

    responsibility_role_ref: List[ResponsibilityRoleRef] = field(
        default_factory=list,
        metadata={
            "name": "ResponsibilityRoleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
