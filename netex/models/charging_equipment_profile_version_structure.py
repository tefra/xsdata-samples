from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from xsdata.models.datatype import XmlDuration
from .coupling_type_enumeration import CouplingTypeEnumeration
from .current_type_enumeration import CurrentTypeEnumeration
from .plug_type_enumeration import PlugTypeEnumeration
from .type_of_plug_ref import TypeOfPlugRef
from .vehicle_equipment_profile_version_structure import (
    VehicleEquipmentProfileVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ChargingEquipmentProfileVersionStructure(
    VehicleEquipmentProfileVersionStructure
):
    class Meta:
        name = "ChargingEquipmentProfile_VersionStructure"

    coupling_type: Optional[CouplingTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "CouplingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    plug_type: Optional[PlugTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "PlugType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_plug_ref: Optional[TypeOfPlugRef] = field(
        default=None,
        metadata={
            "name": "TypeOfPlugRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    current_type: Optional[CurrentTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "CurrentType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    charging_voltage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ChargingVoltage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_charging_power: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumChargingPower",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    preparation_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "PreparationDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    finalisation_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "FinalisationDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
