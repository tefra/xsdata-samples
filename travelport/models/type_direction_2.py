from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


class TypeDirection2(StrEnum):
    """
    Defines the Direction for Incoming or Outgoing.
    """

    INCOMING = "Incoming"
    OUTGOING = "Outgoing"
