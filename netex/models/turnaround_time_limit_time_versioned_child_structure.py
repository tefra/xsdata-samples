from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from .journey_timing_versioned_child_structure import JourneyTimingVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TurnaroundTimeLimitTimeVersionedChildStructure(JourneyTimingVersionedChildStructure):
    class Meta:
        name = "TurnaroundTimeLimitTime_VersionedChildStructure"

    minimum_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
