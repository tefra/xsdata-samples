from __future__ import annotations

from dataclasses import dataclass, field

from .frequency_groups_rel_structure import FrequencyGroupsRelStructure
from .service_journey_version_structure import ServiceJourneyVersionStructure
from .template_vehicle_journey_type_enumeration import (
    TemplateVehicleJourneyTypeEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TemplateServiceJourneyVersionStructure(ServiceJourneyVersionStructure):
    class Meta:
        name = "TemplateServiceJourney_VersionStructure"

    template_vehicle_journey_type: (
        None | TemplateVehicleJourneyTypeEnumeration
    ) = field(
        default=None,
        metadata={
            "name": "TemplateVehicleJourneyType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    frequency_groups: None | FrequencyGroupsRelStructure = field(
        default=None,
        metadata={
            "name": "frequencyGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
