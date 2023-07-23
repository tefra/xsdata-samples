from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1
from travelport.models.loyalty_card_1 import LoyaltyCard1
from travelport.models.person_name_search import PersonNameSearch

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirPrePayReq(BaseReq1):
    """
    Flight Pass Request.

    Parameters
    ----------
    list_search
        Provider: ACH.
    pre_pay_retrieve
        Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    list_search: None | AirPrePayReq.ListSearch = field(
        default=None,
        metadata={
            "name": "ListSearch",
            "type": "Element",
        }
    )
    pre_pay_retrieve: None | AirPrePayReq.PrePayRetrieve = field(
        default=None,
        metadata={
            "name": "PrePayRetrieve",
            "type": "Element",
        }
    )

    @dataclass
    class ListSearch:
        """
        Parameters
        ----------
        person_name_search
            Customer name detail for searching flight pass content.
        loyalty_card
            Customer loyalty card for searching flight pass content.
        start_from_result
            Start index of the section of flight pass numbers that is being
            requested.
        max_results
            Max Number of Flight Passes being requested for.
        """
        person_name_search: None | PersonNameSearch = field(
            default=None,
            metadata={
                "name": "PersonNameSearch",
                "type": "Element",
            }
        )
        loyalty_card: list[LoyaltyCard1] = field(
            default_factory=list,
            metadata={
                "name": "LoyaltyCard",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "max_occurs": 999,
            }
        )
        start_from_result: None | int = field(
            default=None,
            metadata={
                "name": "StartFromResult",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 1,
            }
        )
        max_results: None | int = field(
            default=None,
            metadata={
                "name": "MaxResults",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 1,
                "max_inclusive": 200,
            }
        )

    @dataclass
    class PrePayRetrieve:
        """
        Parameters
        ----------
        id
            Pre pay id to retrieved,example flight pass  number
        type_value
            Pre pay id type,example 'FlightPass'
        """
        id: None | str = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Attribute",
                "required": True,
                "min_length": 1,
                "max_length": 36,
            }
        )
        type_value: None | str = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
