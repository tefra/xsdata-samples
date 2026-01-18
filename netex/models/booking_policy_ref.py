from __future__ import annotations

from dataclasses import dataclass

from .booking_policy_ref_structure import BookingPolicyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BookingPolicyRef(BookingPolicyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
