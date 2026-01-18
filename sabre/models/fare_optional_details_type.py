from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class FareOptionalDetailsType:
    """
    You don't need to specify all of these attributes for a given flight.

    For some of them it is sufficient to be specified in the last flight of
    a given fare component. For details, see notes below --- the attributes
    are annotated with ,,last Flight in Fare Component''.

    Attributes:
        component_no: Fare component number
        basis_code: Fare basis code
        amount: Fare amount (note: last Flight in Fare Component)
        vendor: Vendor (note: last Flight in Fare Component)
        source_vendor: Fare Source Vendor (note: last Flight in Fare
            Component)
        tariff: Tariff (note: last Flight in Fare Component)
        rule_number: Rule Number (note: last Flight in Fare Component)
        brand_id: Used to indicate brand code
        program_id:
    """

    component_no: None | int = field(
        default=None,
        metadata={
            "name": "ComponentNo",
            "type": "Attribute",
        },
    )
    basis_code: None | str = field(
        default=None,
        metadata={
            "name": "BasisCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 15,
            "pattern": r"[A-Z0-9]+(/[A-Z0-9]+)?",
        },
    )
    amount: None | Decimal = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "fraction_digits": 3,
        },
    )
    vendor: None | str = field(
        default=None,
        metadata={
            "name": "Vendor",
            "type": "Attribute",
        },
    )
    source_vendor: None | str = field(
        default=None,
        metadata={
            "name": "SourceVendor",
            "type": "Attribute",
            "pattern": r"[0-9A-Z]{2,3}",
        },
    )
    tariff: None | str = field(
        default=None,
        metadata={
            "name": "Tariff",
            "type": "Attribute",
        },
    )
    rule_number: None | str = field(
        default=None,
        metadata={
            "name": "RuleNumber",
            "type": "Attribute",
        },
    )
    brand_id: None | str = field(
        default=None,
        metadata={
            "name": "BrandID",
            "type": "Attribute",
            "min_length": 1,
        },
    )
    program_id: None | int = field(
        default=None,
        metadata={
            "name": "ProgramID",
            "type": "Attribute",
        },
    )
