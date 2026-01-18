from __future__ import annotations

from dataclasses import dataclass

from .booking_policy_version_structure import BookingPolicyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BookingPolicy(BookingPolicyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
