from enum import Enum

__NAMESPACE__ = "urn:vpro:media:2009"


class IntentionEnum(Enum):
    INFORM = "INFORM"
    INFORM_NEWS_AND_FACTS = "INFORM_NEWS_AND_FACTS"
    INFORM_INDEPTH = "INFORM_INDEPTH"
    INFORM_GENERAL = "INFORM_GENERAL"
    ENTERTAINMENT = "ENTERTAINMENT"
    ENTERTAINMENT_LEASURE = "ENTERTAINMENT_LEASURE"
    ENTERTAINMENT_INFORMATIVE = "ENTERTAINMENT_INFORMATIVE"
    ACTIVATING = "ACTIVATING"