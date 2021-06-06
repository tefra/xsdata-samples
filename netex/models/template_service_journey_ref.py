from dataclasses import dataclass
from .template_service_journey_ref_structure import TemplateServiceJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TemplateServiceJourneyRef(TemplateServiceJourneyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
