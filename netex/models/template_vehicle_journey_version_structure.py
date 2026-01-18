from __future__ import annotations

from dataclasses import dataclass, field

from .frequency_groups_rel_structure import FrequencyGroupsRelStructure
from .journey_version_structure import JourneyVersionStructure
from .template_vehicle_journey_type_enumeration import (
    TemplateVehicleJourneyTypeEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TemplateVehicleJourneyVersionStructure(JourneyVersionStructure):
    class Meta:
        name = "TemplateVehicleJourney_VersionStructure"

    template_vehicle_journey_type: (
        TemplateVehicleJourneyTypeEnumeration | None
    ) = field(
        default=None,
        metadata={
            "name": "TemplateVehicleJourneyType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    frequency_groups: FrequencyGroupsRelStructure | None = field(
        default=None,
        metadata={
            "name": "frequencyGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
