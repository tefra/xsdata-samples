from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.crossref.org/fundref.xsd"


class AssertionName(StrEnum):
    FUNDGROUP = "fundgroup"
    FUNDER_IDENTIFIER = "funder_identifier"
    FUNDER_NAME = "funder_name"
    AWARD_NUMBER = "award_number"
