from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ChangedFlagEnum(Enum):
    """
    List of flags to indicate what has changed in an exchage.

    :cvar CATALOGUE: Catalogue has changed indicator.
    :cvar FILTER: Filter has changed indicator.
    """

    CATALOGUE = "catalogue"
    FILTER = "filter"
