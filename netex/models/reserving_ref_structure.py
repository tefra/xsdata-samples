from __future__ import annotations

from dataclasses import dataclass

from .booking_policy_ref_structure import BookingPolicyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReservingRefStructure(BookingPolicyRefStructure):
    pass
