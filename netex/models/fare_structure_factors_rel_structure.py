from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .fare_demand_factor_ref import FareDemandFactorRef
from .fare_quota_factor_ref import FareQuotaFactorRef
from .fare_structure_factor import FareStructureFactor
from .geographical_structure_factor_ref import GeographicalStructureFactorRef
from .parking_charge_band_ref import ParkingChargeBandRef
from .quality_structure_factor_ref import QualityStructureFactorRef
from .time_structure_factor_ref import TimeStructureFactorRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareStructureFactorsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "fareStructureFactors_RelStructure"

    choice: Iterable[
        Union[
            ParkingChargeBandRef,
            TimeStructureFactorRef,
            FareQuotaFactorRef,
            FareDemandFactorRef,
            QualityStructureFactorRef,
            GeographicalStructureFactorRef,
            FareStructureFactor,
        ]
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
                    "name": "TimeStructureFactorRef",
                    "type": TimeStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareQuotaFactorRef",
                    "type": FareQuotaFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDemandFactorRef",
                    "type": FareDemandFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorRef",
                    "type": QualityStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalStructureFactorRef",
                    "type": GeographicalStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureFactor",
                    "type": FareStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
