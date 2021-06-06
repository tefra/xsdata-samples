from dataclasses import dataclass, field
from typing import List, Optional
from .all_modes_enumeration import AllModesEnumeration
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .control_centre_ref import ControlCentreRef
from .department_ref import DepartmentRef
from .multilingual_string import MultilingualString
from .organisation_part_ref import OrganisationPartRef
from .organisational_unit_ref import OrganisationalUnitRef
from .private_code import PrivateCode
from .transport_submode import TransportSubmode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OperationalContextVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "OperationalContext_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    control_centre_ref: List[ControlCentreRef] = field(
        default_factory=list,
        metadata={
            "name": "ControlCentreRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    organisational_unit_ref: List[OrganisationalUnitRef] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    department_ref: List[DepartmentRef] = field(
        default_factory=list,
        metadata={
            "name": "DepartmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    organisation_part_ref: Optional[OrganisationPartRef] = field(
        default=None,
        metadata={
            "name": "OrganisationPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_mode: Optional[AllModesEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_submode: Optional[TransportSubmode] = field(
        default=None,
        metadata={
            "name": "TransportSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
