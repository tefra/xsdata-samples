from __future__ import annotations

from dataclasses import dataclass

from .template_service_journey_version_structure import (
    TemplateServiceJourneyVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TemplateServiceJourney(TemplateServiceJourneyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
