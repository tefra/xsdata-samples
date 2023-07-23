from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypeMasked1(Enum):
    """Defines whether the field data should be masked in messaging, and the
    masking pattern.

    All masking is simple character substitution (replace each masked
    character with an asterisk).
    """
    NOT_MASKED = "Not Masked"
    MASK_ALL = "Mask All"
    MASK_FIRST_AND_LAST = "Mask First and Last"
    MASK_LAST_TWO = "Mask Last Two"
    SHOW_FIRST_AND_LAST = "Show First and Last"
    SHOW_FIRST_FOUR = "Show First Four"
    SHOW_LAST_FOUR = "Show Last Four"
    SHOW_FIRST_THREE = "Show First Three"
    SHOW_LAST_THREE = "Show Last Three"
