from dataclasses import dataclass, field
from typing import Optional
from netex.models.step_limit_unit_enumeration import StepLimitUnitEnumeration
from netex.models.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StepLimitVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "StepLimit_VersionStructure"

    restricted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Restricted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    adjustment_units: Optional[StepLimitUnitEnumeration] = field(
        default=None,
        metadata={
            "name": "AdjustmentUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_number_of_steps: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumNumberOfSteps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_number_of_steps: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfSteps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_number_of_trips: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfTrips",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
