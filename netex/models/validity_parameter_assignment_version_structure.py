from dataclasses import dataclass, field
from typing import List, Optional
from .access_right_parameter_assignment_version_structure import AccessRightParameterAssignmentVersionStructure
from .fare_demand_factor_ref import FareDemandFactorRef
from .fare_quota_factor_ref import FareQuotaFactorRef
from .geographical_interval_ref import GeographicalIntervalRef
from .geographical_structure_factor_ref import GeographicalStructureFactorRef
from .parking_charge_band_ref import ParkingChargeBandRef
from .quality_structure_factor_ref import QualityStructureFactorRef
from .time_interval_ref import TimeIntervalRef
from .time_structure_factor_ref import TimeStructureFactorRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ValidityParameterAssignmentVersionStructure(AccessRightParameterAssignmentVersionStructure):
    class Meta:
        name = "ValidityParameterAssignment_VersionStructure"

    time_interval_ref: Optional[TimeIntervalRef] = field(
        default=None,
        metadata={
            "name": "TimeIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_charge_band_ref: List[ParkingChargeBandRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingChargeBandRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
        }
    )
    time_structure_factor_ref: Optional[TimeStructureFactorRef] = field(
        default=None,
        metadata={
            "name": "TimeStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_interval_ref: Optional[GeographicalIntervalRef] = field(
        default=None,
        metadata={
            "name": "GeographicalIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_structure_factor_ref: Optional[GeographicalStructureFactorRef] = field(
        default=None,
        metadata={
            "name": "GeographicalStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_quota_factor_ref: List[FareQuotaFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "FareQuotaFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    fare_demand_factor_ref: List[FareDemandFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "FareDemandFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    quality_structure_factor_ref: Optional[QualityStructureFactorRef] = field(
        default=None,
        metadata={
            "name": "QualityStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )