from dataclasses import dataclass, field
from typing import List, Optional
from .driver_ref import DriverRef
from .operating_day_ref import OperatingDayRef
from .service_journey_version_structure import ServiceJourneyVersionStructure
from .uic_operating_period import UicOperatingPeriod

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DatedServiceJourneyVersionStructure(ServiceJourneyVersionStructure):
    class Meta:
        name = "DatedServiceJourney_VersionStructure"

    operating_day_ref_or_uic_operating_period: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OperatingDayRef",
                    "type": OperatingDayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UicOperatingPeriod",
                    "type": UicOperatingPeriod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 2,
        }
    )
    driver_ref: Optional[DriverRef] = field(
        default=None,
        metadata={
            "name": "DriverRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
