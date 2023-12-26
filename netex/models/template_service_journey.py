from dataclasses import dataclass
from .template_service_journey_version_structure import (
    TemplateServiceJourneyVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TemplateServiceJourney(TemplateServiceJourneyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
