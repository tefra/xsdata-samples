from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class UrgencyEnum(Enum):
    """
    Degrees of urgency that a receiving client should associate with the
    disseminate of the information contained in the publication.

    :cvar EXTREMELY_URGENT: Dissemination of the information is
        extremely urgent.
    :cvar URGENT: Dissemination of the information is urgent.
    :cvar NORMAL_URGENCY: Dissemination of the information is of normal
        urgency.
    """
    EXTREMELY_URGENT = "extremelyUrgent"
    URGENT = "urgent"
    NORMAL_URGENCY = "normalUrgency"
