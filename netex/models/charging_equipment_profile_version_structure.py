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

    coupling_type: CouplingTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "CouplingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    plug_type: PlugTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "PlugType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_plug_ref: TypeOfPlugRef | None = field(
        default=None,
        metadata={
            "name": "TypeOfPlugRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    current_type: CurrentTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "CurrentType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    charging_voltage: Decimal | None = field(
        default=None,
        metadata={
            "name": "ChargingVoltage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_charging_power: Decimal | None = field(
        default=None,
        metadata={
            "name": "MaximumChargingPower",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    preparation_duration: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "PreparationDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    finalisation_duration: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "FinalisationDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
