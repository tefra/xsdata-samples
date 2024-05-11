from dataclasses import dataclass

from .passenger_beacon_equipment_ref_structure import (
    PassengerBeaconEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerBeaconEquipmentRef(PassengerBeaconEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
