from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .control_centre import ControlCentre
from .control_centre_ref import ControlCentreRef
from .department import Department
from .department_ref import DepartmentRef
from .operating_department import OperatingDepartment
from .organisation_part_1 import OrganisationPart1
from .organisation_part_2 import OrganisationPart2
from .organisation_part_ref import OrganisationPartRef
from .organisational_unit_ref import OrganisationalUnitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OrganisationPartsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "organisationParts_RelStructure"

    control_centre_ref: List[ControlCentreRef] = field(
        default_factory=list,
        metadata={
            "name": "ControlCentreRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    organisational_unit_ref: List[OrganisationalUnitRef] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    department_ref: List[DepartmentRef] = field(
        default_factory=list,
        metadata={
            "name": "DepartmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    organisation_part_ref: List[OrganisationPartRef] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    control_centre: List[ControlCentre] = field(
        default_factory=list,
        metadata={
            "name": "ControlCentre",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operating_department: List[OperatingDepartment] = field(
        default_factory=list,
        metadata={
            "name": "OperatingDepartment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    department: List[Department] = field(
        default_factory=list,
        metadata={
            "name": "Department",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    organisation_part: List[OrganisationPart1] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_organisation_part: List[OrganisationPart2] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationPart_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
