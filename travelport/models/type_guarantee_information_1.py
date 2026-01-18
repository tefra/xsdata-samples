from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_guarantee_information_agency_type_1 import (
    TypeGuaranteeInformationAgencyType1,
)
from travelport.models.type_guarantee_information_type_1 import (
    TypeGuaranteeInformationType1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass(kw_only=True)
class TypeGuaranteeInformation1:
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

    type_value: TypeGuaranteeInformationType1 = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    agency_type: TypeGuaranteeInformationAgencyType1 = field(
        metadata={
            "name": "AgencyType",
            "type": "Attribute",
            "required": True,
        }
    )
    iatanumber: str = field(
        metadata={
            "name": "IATANumber",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
