from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/fundref.xsd"


class AssertionName(Enum):
    FUNDGROUP = "fundgroup"
    FUNDER_IDENTIFIER = "funder_identifier"
    FUNDER_NAME = "funder_name"
    AWARD_NUMBER = "award_number"
