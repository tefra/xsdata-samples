from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_text_block_1 import TypeTextBlock1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass(kw_only=True)
class CommandResponse(TypeTextBlock1):
    """
    The response from the host.

    Usually pre-formatted.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"
