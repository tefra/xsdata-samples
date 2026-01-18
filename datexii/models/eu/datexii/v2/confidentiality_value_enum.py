from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ConfidentialityValueEnum(Enum):
    """
    Values of confidentiality.

    :cvar INTERNAL_USE: For internal use only of the recipient
        organisation.
    :cvar NO_RESTRICTION: No restriction on usage.
    :cvar RESTRICTED_TO_AUTHORITIES: Restricted for use only by
        authorities.
    :cvar RESTRICTED_TO_AUTHORITIES_AND_TRAFFIC_OPERATORS: Restricted
        for use only by authorities and traffic operators.
    :cvar RESTRICTED_TO_AUTHORITIES_TRAFFIC_OPERATORS_AND_PUBLISHERS:
        Restricted for use only by authorities, traffic operators and
        publishers (service providers).
    :cvar RESTRICTED_TO_AUTHORITIES_TRAFFIC_OPERATORS_AND_VMS:
        Restricted for use only by authorities, traffic operators,
        publishers (service providers) and variable message signs.
    """

    INTERNAL_USE = "internalUse"
    NO_RESTRICTION = "noRestriction"
    RESTRICTED_TO_AUTHORITIES = "restrictedToAuthorities"
    RESTRICTED_TO_AUTHORITIES_AND_TRAFFIC_OPERATORS = (
        "restrictedToAuthoritiesAndTrafficOperators"
    )
    RESTRICTED_TO_AUTHORITIES_TRAFFIC_OPERATORS_AND_PUBLISHERS = (
        "restrictedToAuthoritiesTrafficOperatorsAndPublishers"
    )
    RESTRICTED_TO_AUTHORITIES_TRAFFIC_OPERATORS_AND_VMS = (
        "restrictedToAuthoritiesTrafficOperatorsAndVms"
    )
