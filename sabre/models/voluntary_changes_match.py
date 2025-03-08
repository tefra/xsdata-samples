from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class VoluntaryChangesMatch(Enum):
    """
    Attributes:
        ALL: Conditions are joined by logical conjunction - fare needs
            to fulfill all the conditions to be returned in response.
        ANY: Conditions are joined by logical disjunction - fare needs
            to fulfill at least one of the conditions to be returned in
            response.
        INFO: Return penalty information
    """

    ALL = "All"
    ANY = "Any"
    INFO = "Info"
