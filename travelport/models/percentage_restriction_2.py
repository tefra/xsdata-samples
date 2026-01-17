from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_float_restriction_2 import TypeFloatRestriction2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class PercentageRestriction2(TypeFloatRestriction2):
    """
    Restrictions on profile data for fields with a data type of percentage.

    Min and max values are inclusive.
    """

    class Meta:
        name = "PercentageRestriction"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"
