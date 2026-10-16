from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.crossref.org/clinicaltrials.xsd"


class ClinicalTrialNumberType(StrEnum):
    PRE_RESULTS = "preResults"
    RESULTS = "results"
    POST_RESULTS = "postResults"
