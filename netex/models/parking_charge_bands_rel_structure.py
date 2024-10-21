from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .parking_charge_band_ref import ParkingChargeBandRef
from .priceable_object_version_structure import ParkingChargeBand

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingChargeBandsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "parkingChargeBands_RelStructure"

    parking_charge_band_ref_or_parking_charge_band: Iterable[
        Union[ParkingChargeBandRef, ParkingChargeBand]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingChargeBandRef",
                    "type": ParkingChargeBandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingChargeBand",
                    "type": ParkingChargeBand,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
