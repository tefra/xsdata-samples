from dataclasses import dataclass, field
from typing import Optional
from netex.models.department_ref import DepartmentRef
from netex.models.multilingual_string import MultilingualString
from netex.models.organisation_part_version_structure import OrganisationPartVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ControlCentreVersionStructure(OrganisationPartVersionStructure):
    class Meta:
        name = "ControlCentre_VersionStructure"

    number: Optional[int] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    control_centre_code: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ControlCentreCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    department_ref: Optional[DepartmentRef] = field(
        default=None,
        metadata={
            "name": "DepartmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
