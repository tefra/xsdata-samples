from dataclasses import dataclass, field
from typing import List
from netex.models.parking_charge_band_ref import ParkingChargeBandRef
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from netex.models.time_structure_factor import TimeStructureFactor
from netex.models.time_structure_factor_ref import TimeStructureFactorRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeStructureFactorsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "timeStructureFactors_RelStructure"

    parking_charge_band_ref: List[ParkingChargeBandRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingChargeBandRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_structure_factor_ref: List[TimeStructureFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "TimeStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_structure_factor: List[TimeStructureFactor] = field(
        default_factory=list,
        metadata={
            "name": "TimeStructureFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
