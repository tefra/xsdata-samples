from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_string_restriction_2 import TypeStringRestriction2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class TextRestriction2(TypeStringRestriction2):
    """
    Restrictions on profile data for fields with a data type of alpha.

    Min and max lengths are inclusive.
    """

    class Meta:
        name = "TextRestriction"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"
