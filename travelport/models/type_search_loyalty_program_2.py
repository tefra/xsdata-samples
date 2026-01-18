from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class TypeSearchLoyaltyProgram2:
    """
    The Searchable fields on LoyaltyProgram.

    Parameters
    ----------
    number
    supplier_code
        The code of the supplier that provides the loyalty program (e.g. UA,
        HZ, etc.)
    """

    class Meta:
        name = "typeSearchLoyaltyProgram"

    number: str = field(
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        }
    )
    supplier_code: str = field(
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "max_length": 6,
        }
    )
