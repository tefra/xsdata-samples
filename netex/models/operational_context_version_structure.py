from __future__ import annotations

from dataclasses import dataclass, field

from .all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from .control_centre_ref import ControlCentreRef
from .department_ref import DepartmentRef
from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .organisation_part_ref import OrganisationPartRef
from .organisational_unit_ref import OrganisationalUnitRef
from .private_code import PrivateCode
from .transport_submode import TransportSubmode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OperationalContextVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "OperationalContext_VersionStructure"

    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: None | PrivateCode = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    organisation_part_ref: (
        None
        | ControlCentreRef
        | OrganisationalUnitRef
        | DepartmentRef
        | OrganisationPartRef
    ) = field(
        default=None,
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
            ),
        },
    )
    vehicle_mode: None | AllVehicleModesOfTransportEnumeration = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_submode: None | TransportSubmode = field(
        default=None,
        metadata={
            "name": "TransportSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
