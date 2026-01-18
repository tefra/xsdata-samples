from dataclasses import dataclass, field

from .department_ref import DepartmentRef
from .multilingual_string import MultilingualString
from .organisation_part_version_structure import (
    OrganisationPartVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ControlCentreVersionStructure(OrganisationPartVersionStructure):
    class Meta:
        name = "ControlCentre_VersionStructure"

    number: int | None = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    control_centre_code: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "ControlCentreCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    department_ref: DepartmentRef | None = field(
        default=None,
        metadata={
            "name": "DepartmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
