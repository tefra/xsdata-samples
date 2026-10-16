from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypeContactPurpose1(StrEnum):
    """
    A code for categorizing a contact mechanism based on purpose or use.

    Examples include business, persona., etc.
    """

    ALL = "All"
    BUSINESS = "Business"
    PERSONAL = "Personal"
