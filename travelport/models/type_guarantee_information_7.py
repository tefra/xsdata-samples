from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_guarantee_information_agency_type_7 import (
    TypeGuaranteeInformationAgencyType7,
)
from travelport.models.type_guarantee_information_type_7 import (
    TypeGuaranteeInformationType7,
)

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class TypeGuaranteeInformation7:
    """
    Information pertaining to the payment of type Guarantee.

    Parameters
    ----------
    type_value
        Guarantee only or Deposit
    agency_type
        Guarantee to Agency IATA or Guarantee to Another Agency IATA
    iatanumber
        Payment IATA number. (ie. IATA of Agency or Other Agency)
    """

    class Meta:
        name = "typeGuaranteeInformation"

    type_value: None | TypeGuaranteeInformationType7 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    agency_type: None | TypeGuaranteeInformationAgencyType7 = field(
        default=None,
        metadata={
            "name": "AgencyType",
            "type": "Attribute",
            "required": True,
        },
    )
    iatanumber: None | str = field(
        default=None,
        metadata={
            "name": "IATANumber",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        },
    )
