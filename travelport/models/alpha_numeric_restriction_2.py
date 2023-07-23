from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_string_restriction_2 import TypeStringRestriction2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class AlphaNumericRestriction2(TypeStringRestriction2):
    """Restrictions on profile data for fields with a data type of alphanumeric.

    Min and max lengths are inclusive.
    """
    class Meta:
        name = "AlphaNumericRestriction"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"
