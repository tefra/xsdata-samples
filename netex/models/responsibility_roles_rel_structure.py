from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .responsibility_role import ResponsibilityRole
from .responsibility_role_ref import ResponsibilityRoleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResponsibilityRolesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "ResponsibilityRoles_RelStructure"

    responsibility_role_ref_or_responsibility_role: Iterable[
        ResponsibilityRoleRef | ResponsibilityRole
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ResponsibilityRoleRef",
                    "type": ResponsibilityRoleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResponsibilityRole",
                    "type": ResponsibilityRole,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
