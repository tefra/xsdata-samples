from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


class TypeShowProvidersType(Enum):
    """Enumeration of reqested type of Provider Configuration requested.

    An error may be returned if 'All' and the user security level is not
    allowed this access
    """
    ALL = "All"
    PROVISIONED = "Provisioned"
