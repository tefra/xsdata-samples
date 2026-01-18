from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class TypeSearchAccountingReference1:
    """
    The Searchable fields on AccountingReference.

    Parameters
    ----------
    type_value
        A code for categorizing a reference for a Traveler's bookings.  This
        is often used by the Traveler's employer for budgeting, internal
        billing or other cost accounting purposes.  Examples include Budget
        Codes, Department Codes, Project Codes, etc.
    value
        The number or alphanumeric code for an employer reference.
    """

    class Meta:
        name = "typeSearchAccountingReference"

    type_value: str = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    value: str = field(
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        }
    )
