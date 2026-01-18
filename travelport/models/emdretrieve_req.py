from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.provider_reservation_detail_1 import (
    ProviderReservationDetail1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class EmdretrieveReq(BaseReq1):
    """
    Electronic Miscellaneous Document retrieve request.Supported providers
    are 1G/1V/1P.

    Parameters
    ----------
    list_retrieve
        Provider: 1G/1V/1P-Information required for retrieval of list of
        EMDs
    detail_retrieve
        Provider: 1G/1V/1P-Information required for a detailed EMD retrieve
    """

    class Meta:
        name = "EMDRetrieveReq"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    list_retrieve: None | EmdretrieveReq.ListRetrieve = field(
        default=None,
        metadata={
            "name": "ListRetrieve",
            "type": "Element",
        },
    )
    detail_retrieve: None | EmdretrieveReq.DetailRetrieve = field(
        default=None,
        metadata={
            "name": "DetailRetrieve",
            "type": "Element",
        },
    )

    @dataclass(kw_only=True)
    class ListRetrieve:
        """
        Parameters
        ----------
        provider_reservation_detail
            Provider reservation details to be provided to fetch list of
            EMDs associated with it.
        """

        provider_reservation_detail: ProviderReservationDetail1 = field(
            metadata={
                "name": "ProviderReservationDetail",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class DetailRetrieve:
        """
        Parameters
        ----------
        provider_reservation_detail
            Provider reservation locator to be specified for display
            operation, if mentioned along woth the EMD number then
            synchronization of that EMD is performed considering the same to
            be associated with the mentioned PNR.
        emdnumber
            EMD number to be specified for display operation. If mentioned
            along with provider reservation detail then synchronization of
            that EMD is performed considering the same to be associated with
            the mentioned PNR.
        """

        provider_reservation_detail: None | ProviderReservationDetail1 = field(
            default=None,
            metadata={
                "name": "ProviderReservationDetail",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
            },
        )
        emdnumber: str = field(
            metadata={
                "name": "EMDNumber",
                "type": "Element",
                "required": True,
                "length": 13,
            }
        )
