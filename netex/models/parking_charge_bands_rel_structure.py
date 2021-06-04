from dataclasses import dataclass, field
from typing import List
from netex.models.cell_versioned_child_structure import ParkingChargeBand
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.parking_charge_band_ref import ParkingChargeBandRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingChargeBandsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "parkingChargeBands_RelStructure"

    parking_charge_band_ref: List[ParkingChargeBandRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingChargeBandRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_charge_band: List[ParkingChargeBand] = field(
        default_factory=list,
        metadata={
            "name": "ParkingChargeBand",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
