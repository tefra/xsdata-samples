from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Othtype:
    """
    Parameters
    ----------
    cat0
        Category 0 rules. True if category applies.  False if rules do not
        apply.
    cat1
        Category 1 rules. True if category applies.  False if rules do not
        apply.
    cat2
        Category 2 rules. True if category applies.  False if rules do not
        apply.
    cat3
        Category 3 rules. True if category applies.  False if rules do not
        apply.
    cat4
        Category 4 rules. True if category applies.  False if rules do not
        apply.
    cat5
        Category 5 rules. True if category applies.  False if rules do not
        apply.
    cat6
        Category 6 rules. True if category applies.  False if rules do not
        apply.
    cat7
        Category 7 rules. True if category applies.  False if rules do not
        apply.
    cat8
        Category 8 rules. True if category applies.  False if rules do not
        apply.
    cat9
        Category 9 rules. True if category applies.  False if rules do not
        apply.
    cat10
        Category 10 rules. True if category applies.  False if rules do not
        apply.
    cat11
        Category 11 rules. True if category applies.  False if rules do not
        apply.
    cat12
        Category 12 rules. True if category applies.  False if rules do not
        apply.
    cat13
        Category 13 rules. True if category applies.  False if rules do not
        apply.
    cat14
        Category 14 rules. True if category applies.  False if rules do not
        apply.
    cat15
        Category 15 rules. True if category applies.  False if rules do not
        apply.
    cat16
        Category 16 rules. True if category applies.  False if rules do not
        apply.
    cat17
        Category 17 rules. True if category applies.  False if rules do not
        apply.
    cat18
        Category 18 rules. True if category applies.  False if rules do not
        apply.
    cat19
        Category 19 rules. True if category applies.  False if rules do not
        apply.
    cat20
        Category 20 rules. True if category applies.  False if rules do not
        apply.
    cat21
        Category 21 rules. True if category applies.  False if rules do not
        apply.
    cat22
        Category 22 rules. True if category applies.  False if rules do not
        apply.
    cat23
        Category 23 rules. True if category applies.  False if rules do not
        apply.
    cat24
        Category 24 rules. True if category applies.  False if rules do not
        apply.
    cat25
        Category 25 rules. True if category applies.  False if rules do not
        apply.
    cat26
        Category 26 rules. True if category applies.  False if rules do not
        apply.
    cat27
        Category 27 rules. True if category applies.  False if rules do not
        apply.
    cat28
        Category 28 rules. True if category applies.  False if rules do not
        apply.
    cat29
        Category 29 rules. True if category applies.  False if rules do not
        apply.
    cat30
        Category 30 rules. True if category applies.  False if rules do not
        apply.
    cat31
        Category 31 rules. True if category applies.  False if rules do not
        apply.
    restrictive_dt
        Most restrictive ticketing date.
    surcharge_amt
        Surcharge amount
    not_usacity
        Not USA city.  True if Origin or final destination not a continental
        U.S. City. False if Origin or final destination a continental U.S.
        City.
    missing_rules
        Missing rules.  True if rules are missing.  False if rules are not
        missing.
    """
    class Meta:
        name = "OTHType"

    cat0: None | bool = field(
        default=None,
        metadata={
            "name": "Cat0",
            "type": "Attribute",
        }
    )
    cat1: None | bool = field(
        default=None,
        metadata={
            "name": "Cat1",
            "type": "Attribute",
        }
    )
    cat2: None | bool = field(
        default=None,
        metadata={
            "name": "Cat2",
            "type": "Attribute",
        }
    )
    cat3: None | bool = field(
        default=None,
        metadata={
            "name": "Cat3",
            "type": "Attribute",
        }
    )
    cat4: None | bool = field(
        default=None,
        metadata={
            "name": "Cat4",
            "type": "Attribute",
        }
    )
    cat5: None | bool = field(
        default=None,
        metadata={
            "name": "Cat5",
            "type": "Attribute",
        }
    )
    cat6: None | bool = field(
        default=None,
        metadata={
            "name": "Cat6",
            "type": "Attribute",
        }
    )
    cat7: None | bool = field(
        default=None,
        metadata={
            "name": "Cat7",
            "type": "Attribute",
        }
    )
    cat8: None | bool = field(
        default=None,
        metadata={
            "name": "Cat8",
            "type": "Attribute",
        }
    )
    cat9: None | bool = field(
        default=None,
        metadata={
            "name": "Cat9",
            "type": "Attribute",
        }
    )
    cat10: None | bool = field(
        default=None,
        metadata={
            "name": "Cat10",
            "type": "Attribute",
        }
    )
    cat11: None | bool = field(
        default=None,
        metadata={
            "name": "Cat11",
            "type": "Attribute",
        }
    )
    cat12: None | bool = field(
        default=None,
        metadata={
            "name": "Cat12",
            "type": "Attribute",
        }
    )
    cat13: None | bool = field(
        default=None,
        metadata={
            "name": "Cat13",
            "type": "Attribute",
        }
    )
    cat14: None | bool = field(
        default=None,
        metadata={
            "name": "Cat14",
            "type": "Attribute",
        }
    )
    cat15: None | bool = field(
        default=None,
        metadata={
            "name": "Cat15",
            "type": "Attribute",
        }
    )
    cat16: None | bool = field(
        default=None,
        metadata={
            "name": "Cat16",
            "type": "Attribute",
        }
    )
    cat17: None | bool = field(
        default=None,
        metadata={
            "name": "Cat17",
            "type": "Attribute",
        }
    )
    cat18: None | bool = field(
        default=None,
        metadata={
            "name": "Cat18",
            "type": "Attribute",
        }
    )
    cat19: None | bool = field(
        default=None,
        metadata={
            "name": "Cat19",
            "type": "Attribute",
        }
    )
    cat20: None | bool = field(
        default=None,
        metadata={
            "name": "Cat20",
            "type": "Attribute",
        }
    )
    cat21: None | bool = field(
        default=None,
        metadata={
            "name": "Cat21",
            "type": "Attribute",
        }
    )
    cat22: None | bool = field(
        default=None,
        metadata={
            "name": "Cat22",
            "type": "Attribute",
        }
    )
    cat23: None | bool = field(
        default=None,
        metadata={
            "name": "Cat23",
            "type": "Attribute",
        }
    )
    cat24: None | bool = field(
        default=None,
        metadata={
            "name": "Cat24",
            "type": "Attribute",
        }
    )
    cat25: None | bool = field(
        default=None,
        metadata={
            "name": "Cat25",
            "type": "Attribute",
        }
    )
    cat26: None | bool = field(
        default=None,
        metadata={
            "name": "Cat26",
            "type": "Attribute",
        }
    )
    cat27: None | bool = field(
        default=None,
        metadata={
            "name": "Cat27",
            "type": "Attribute",
        }
    )
    cat28: None | bool = field(
        default=None,
        metadata={
            "name": "Cat28",
            "type": "Attribute",
        }
    )
    cat29: None | bool = field(
        default=None,
        metadata={
            "name": "Cat29",
            "type": "Attribute",
        }
    )
    cat30: None | bool = field(
        default=None,
        metadata={
            "name": "Cat30",
            "type": "Attribute",
        }
    )
    cat31: None | bool = field(
        default=None,
        metadata={
            "name": "Cat31",
            "type": "Attribute",
        }
    )
    restrictive_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "RestrictiveDt",
            "type": "Attribute",
        }
    )
    surcharge_amt: None | Decimal = field(
        default=None,
        metadata={
            "name": "SurchargeAmt",
            "type": "Attribute",
        }
    )
    not_usacity: None | bool = field(
        default=None,
        metadata={
            "name": "NotUSACity",
            "type": "Attribute",
        }
    )
    missing_rules: None | bool = field(
        default=None,
        metadata={
            "name": "MissingRules",
            "type": "Attribute",
        }
    )
