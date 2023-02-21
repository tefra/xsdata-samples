from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ProbabilityOfOccurrenceEnum(Enum):
    """
    Levels of confidence that the sender has in the information, ordered {certain,
    probable, risk of}.

    :cvar CERTAIN: The source is completely certain of the occurrence of
        the situation record version content.
    :cvar PROBABLE: The source has a reasonably high level of confidence
        of the occurrence of the situation record version content.
    :cvar RISK_OF: The source has a moderate level of confidence of the
        occurrence of the situation record version content.
    """
    CERTAIN = "certain"
    PROBABLE = "probable"
    RISK_OF = "riskOf"
