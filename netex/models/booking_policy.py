from dataclasses import dataclass

from .booking_policy_version_structure import BookingPolicyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BookingPolicy(BookingPolicyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
