from dataclasses import dataclass
from netex.models.assistance_booking_service_ref_structure import AssistanceBookingServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AssistanceBookingServiceRef(AssistanceBookingServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
