from dataclasses import dataclass, field
from typing import Optional
from .driver_ref import DriverRef
from .operating_day_ref import OperatingDayRef
from .service_journey_version_structure import ServiceJourneyVersionStructure
from .uic_operating_period import UicOperatingPeriod

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DatedServiceJourneyVersionStructure(ServiceJourneyVersionStructure):
    class Meta:
        name = "DatedServiceJourney_VersionStructure"

    operating_day_ref: Optional[OperatingDayRef] = field(
        default=None,
        metadata={
            "name": "OperatingDayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    uic_operating_period: Optional[UicOperatingPeriod] = field(
        default=None,
        metadata={
            "name": "UicOperatingPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
