from dataclasses import dataclass

from .service_journey_interchange_derived_view_structure import (
    ServiceJourneyInterchangeDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceJourneyInterchangeView(
    ServiceJourneyInterchangeDerivedViewStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
