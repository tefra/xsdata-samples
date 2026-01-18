from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


class ProcessingMetaBaseTagset(Enum):
    ARCHIVING = "archiving"
    AUTHORING = "authoring"
    PUBLISHING = "publishing"
