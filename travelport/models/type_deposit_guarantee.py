from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDate

from travelport.models.type_deposit_guarantee_option_type import (
    TypeDepositGuaranteeOptionType,
)
from travelport.models.type_deposit_guarantee_type import (
    TypeDepositGuaranteeType,
)
from travelport.models.type_reserve_requirement import TypeReserveRequirement

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass(kw_only=True)
class TypeDepositGuarantee:
    """
    The deposit and guarantee information for a vehicle rental.

    Parameters
    ----------
    purpose
        Specifies if this is guarantee, deposit and Prepayment information.
        Values: “Guarantee”, “Deposit”, “PrePayment” “Other”.
    type_value
        Specifies if deposit or guarantee rule is for a specified amount,
        the amount for a specific number of days or a percentage of the
        rental.
    amount
        The amount of money required for a guarantee or deposit.
    percent
        The percentage of the rental amount for the guarantee or deposit.
    due_date
        The date a deposit is due.
    number_of_days
        Specifies the number of days from booking or prior to pickup by
        which the deposit should be made.
    option_type
        Specifies if the number of days is after booking or prior to pickup.
    required
        If “true” a Guarantee, Deposit or Prepayment is required. 1P, 1G, 1V
        only.
    requirement_passed
        If true, the rental information passes the guarantee or deposit
        requirements.
    """

    class Meta:
        name = "typeDepositGuarantee"

    purpose: TypeReserveRequirement = field(
        metadata={
            "name": "Purpose",
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: None | TypeDepositGuaranteeType = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        },
    )
    percent: None | Decimal = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Attribute",
        },
    )
    due_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DueDate",
            "type": "Attribute",
        },
    )
    number_of_days: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfDays",
            "type": "Attribute",
        },
    )
    option_type: None | TypeDepositGuaranteeOptionType = field(
        default=None,
        metadata={
            "name": "OptionType",
            "type": "Attribute",
        },
    )
    required: None | bool = field(
        default=None,
        metadata={
            "name": "Required",
            "type": "Attribute",
        },
    )
    requirement_passed: None | bool = field(
        default=None,
        metadata={
            "name": "RequirementPassed",
            "type": "Attribute",
        },
    )
