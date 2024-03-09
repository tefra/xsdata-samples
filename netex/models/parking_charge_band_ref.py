from dataclasses import dataclass

from .parking_charge_band_ref_structure import ParkingChargeBandRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingChargeBandRef(ParkingChargeBandRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
