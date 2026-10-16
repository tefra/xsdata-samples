from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeContactPurpose2(StrEnum):
    """
    A code for categorizing a contact mechanism based on purpose or use.

    Examples include business, persona., etc.
    """

    ALL = "All"
    BUSINESS = "Business"
    PERSONAL = "Personal"
