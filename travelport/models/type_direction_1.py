from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeDirection1(Enum):
    """
    Defines the Direction for Incoming or Outgoing.
    """
    INCOMING = "Incoming"
    OUTGOING = "Outgoing"
