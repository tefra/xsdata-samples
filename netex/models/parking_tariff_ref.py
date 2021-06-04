from dataclasses import dataclass
from netex.models.parking_tariff_ref_structure import ParkingTariffRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingTariffRef(ParkingTariffRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
