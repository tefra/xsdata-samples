from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_guarantee_information_history_agency_type_2 import TypeGuaranteeInformationHistoryAgencyType2
from travelport.models.type_guarantee_information_history_type_2 import TypeGuaranteeInformationHistoryType2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeGuaranteeInformationHistory2:
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
        name = "typeGuaranteeInformationHistory"

    type_value: None | TypeGuaranteeInformationHistoryType2 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    agency_type: None | TypeGuaranteeInformationHistoryAgencyType2 = field(
        default=None,
        metadata={
            "name": "AgencyType",
            "type": "Attribute",
        }
    )
    iatanumber: None | str = field(
        default=None,
        metadata={
            "name": "IATANumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
