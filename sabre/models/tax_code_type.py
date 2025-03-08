from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class TaxCodeType:
    """
    Defines the data fields available for tax code.

    Attributes:
        tax_code: Identifies the code for the tax.
    """

    tax_code: None | str = field(
        default=None,
        metadata={
            "name": "TaxCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Z0-9]{2}[A-Z0-9]{0,1}",
        },
    )
