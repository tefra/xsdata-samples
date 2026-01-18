from __future__ import annotations

from dataclasses import dataclass, field

from .driver_ref import DriverRef
from .operating_day_ref import OperatingDayRef
from .service_journey_version_structure import ServiceJourneyVersionStructure
from .uic_operating_period import UicOperatingPeriod

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DatedServiceJourneyVersionStructure(ServiceJourneyVersionStructure):
    class Meta:
        name = "DatedServiceJourney_VersionStructure"

    operating_day_ref_or_uic_operating_period: (
        None | OperatingDayRef | UicOperatingPeriod
    ) = field(
        default=None,
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
        },
    )
    driver_ref: None | DriverRef = field(
        default=None,
        metadata={
            "name": "DriverRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
