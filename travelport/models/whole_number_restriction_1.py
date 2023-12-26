from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_integer_restriction_1 import (
    TypeIntegerRestriction1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class WholeNumberRestriction1(TypeIntegerRestriction1):
    """Restrictions on profile data for fields with a data type of string.

    Min and max lengths are inclusive.
    """

    class Meta:
        name = "WholeNumberRestriction"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"
