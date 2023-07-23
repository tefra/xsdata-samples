from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_float_restriction_1 import TypeFloatRestriction1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class PercentageRestriction1(TypeFloatRestriction1):
    """Restrictions on profile data for fields with a data type of percentage.

    Min and max values are inclusive.
    """
    class Meta:
        name = "PercentageRestriction"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"
