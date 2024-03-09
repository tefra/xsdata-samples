from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "urn:vpro:media:2009"


class RoleType(Enum):
    DIRECTOR = "DIRECTOR"
    CHIEF_EDITOR = "CHIEF_EDITOR"
    EDITOR = "EDITOR"
    PRESENTER = "PRESENTER"
    INTERVIEWER = "INTERVIEWER"
    PRODUCER = "PRODUCER"
    RESEARCH = "RESEARCH"
    GUEST = "GUEST"
    REPORTER = "REPORTER"
    ACTOR = "ACTOR"
    COMMENTATOR = "COMMENTATOR"
    SCRIPTWRITER = "SCRIPTWRITER"
    COMPOSER = "COMPOSER"
    SUBJECT = "SUBJECT"
    PARTICIPANT = "PARTICIPANT"
    SIDEKICK = "SIDEKICK"
    NEWS_PRESENTER = "NEWS_PRESENTER"
    UNDEFINED = "UNDEFINED"


RoleType.SIDEKICK.__doc__ = (
    "Introduced for MediaConnect sync. This is experimental"
)
RoleType.NEWS_PRESENTER.__doc__ = (
    "Introduced for MediaConnect sync. This is experimental"
)
