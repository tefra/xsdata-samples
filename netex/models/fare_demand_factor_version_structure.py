from dataclasses import dataclass, field
from typing import Optional
from netex.models.fare_demand_type_enumeration import FareDemandTypeEnumeration
from netex.models.quality_structure_factor_version_structure import QualityStructureFactorVersionStructure
from netex.models.start_time_at_stop_points_rel_structure import StartTimeAtStopPointsRelStructure
from netex.models.stop_use_constraint_enumeration import StopUseConstraintEnumeration
from netex.models.time_demand_type_ref import TimeDemandTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareDemandFactorVersionStructure(QualityStructureFactorVersionStructure):
    class Meta:
        name = "FareDemandFactor_VersionStructure"

    fare_demand_type: Optional[FareDemandTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "FareDemandType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_demand_type_ref: Optional[TimeDemandTypeRef] = field(
        default=None,
        metadata={
            "name": "TimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_use_constraint: Optional[StopUseConstraintEnumeration] = field(
        default=None,
        metadata={
            "name": "StopUseConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_times_at_stop_points: Optional[StartTimeAtStopPointsRelStructure] = field(
        default=None,
        metadata={
            "name": "startTimesAtStopPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
