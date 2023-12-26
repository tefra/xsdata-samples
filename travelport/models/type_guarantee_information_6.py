from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_guarantee_information_agency_type_6 import (
    TypeGuaranteeInformationAgencyType6,
)
from travelport.models.type_guarantee_information_type_6 import (
    TypeGuaranteeInformationType6,
)

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class TypeGuaranteeInformation6:
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

    type_value: None | TypeGuaranteeInformationType6 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    agency_type: None | TypeGuaranteeInformationAgencyType6 = field(
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
