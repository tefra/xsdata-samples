from dataclasses import dataclass, field
from typing import Optional
from .dated_vehicle_journey_version_structure import DatedVehicleJourneyVersionStructure
from .service_alteration_enumeration import ServiceAlterationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NormalDatedVehicleJourneyVersionStructure(DatedVehicleJourneyVersionStructure):
    class Meta:
        name = "NormalDatedVehicleJourney_VersionStructure"

    service_alteration_type: Optional[ServiceAlterationEnumeration] = field(
        default=None,
        metadata={
            "name": "ServiceAlterationType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
