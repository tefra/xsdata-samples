from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_float_restriction_2 import TypeFloatRestriction2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class DecimalRestriction2(TypeFloatRestriction2):
    """Restrictions on profile data for fields with a data type of float.

    Min and max values are inclusive.
    """

    class Meta:
        name = "DecimalRestriction"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"
