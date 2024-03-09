from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .control_centre import ControlCentre
from .control_centre_ref import ControlCentreRef
from .department import Department
from .department_ref import DepartmentRef
from .operating_department import OperatingDepartment
from .organisation_part_1 import OrganisationPart1
from .organisation_part_ref import OrganisationPartRef
from .organisational_unit import OrganisationalUnit
from .organisational_unit_ref import OrganisationalUnitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OrganisationPartsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "organisationParts_RelStructure"

    organisation_part_ref_or_organisation_part: List[
        Union[
            ControlCentreRef,
            OrganisationalUnitRef,
            DepartmentRef,
            OrganisationPartRef,
            ControlCentre,
            OperatingDepartment,
            OrganisationalUnit,
            Department,
            OrganisationPart1,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ControlCentreRef",
                    "type": ControlCentreRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationalUnitRef",
                    "type": OrganisationalUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DepartmentRef",
                    "type": DepartmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationPartRef",
                    "type": OrganisationPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControlCentre",
                    "type": ControlCentre,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingDepartment",
                    "type": OperatingDepartment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationalUnit",
                    "type": OrganisationalUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Department",
                    "type": Department,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationPart",
                    "type": OrganisationPart1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
