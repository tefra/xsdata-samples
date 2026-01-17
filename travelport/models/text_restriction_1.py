from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_string_restriction_1 import TypeStringRestriction1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TextRestriction1(TypeStringRestriction1):
    """
    Restrictions on profile data for fields with a data type of alpha.

    Min and max lengths are inclusive.
    """

    class Meta:
        name = "TextRestriction"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"
