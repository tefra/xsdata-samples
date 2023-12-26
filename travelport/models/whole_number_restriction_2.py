from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_integer_restriction_2 import (
    TypeIntegerRestriction2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class WholeNumberRestriction2(TypeIntegerRestriction2):
    """Restrictions on profile data for fields with a data type of string.

    Min and max lengths are inclusive.
    """

    class Meta:
        name = "WholeNumberRestriction"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"
