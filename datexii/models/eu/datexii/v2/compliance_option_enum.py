from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ComplianceOptionEnum(StrEnum):
    """
    Types of compliance.

    :cvar ADVISORY: Advisory compliance.
    :cvar MANDATORY: Mandatory compliance.
    """

    ADVISORY = "advisory"
    MANDATORY = "mandatory"
