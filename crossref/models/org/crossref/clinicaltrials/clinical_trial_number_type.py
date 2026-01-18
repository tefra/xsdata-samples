from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/clinicaltrials.xsd"


class ClinicalTrialNumberType(Enum):
    PRE_RESULTS = "preResults"
    RESULTS = "results"
    POST_RESULTS = "postResults"
