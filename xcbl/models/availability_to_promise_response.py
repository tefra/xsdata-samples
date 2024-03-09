from dataclasses import dataclass, field
from typing import List, Optional

from xcbl.models.shipping_schedule_response import (
    TotalNumberOfLineItems,
    TransportRouting,
)
from xcbl.models.sourcing_result import (
    BaseItemDetail,
    DeliveryDetail,
    InitiatingParty,
    ListOfAttachment,
    ListOfReferenceCoded,
    Transport,
)
from xcbl.models.sourcing_result_response import GeneralNote
from xcbl.models.time_series_response import Party
from xcbl.models.trading_partner_response import Reference


@dataclass(kw_only=True)
class AtpcheckTypeCoded:
    class Meta:
        name = "ATPCheckTypeCoded"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AtpcheckTypeCodedOther:
    class Meta:
        name = "ATPCheckTypeCodedOther"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AvailabilityDeliveryOptionCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AvailabilityDeliveryOptionCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AvailabilityResponseIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AvailabilityToPromisePurposeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AvailabilityToPromisePurposeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseResponseCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseResponseCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AtpcheckType:
    class Meta:
        name = "ATPCheckType"

    atpcheck_type_coded: AtpcheckTypeCoded = field(
        metadata={
            "name": "ATPCheckTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    atpcheck_type_coded_other: Optional[AtpcheckTypeCodedOther] = field(
        default=None,
        metadata={
            "name": "ATPCheckTypeCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Atpresponse:
    class Meta:
        name = "ATPResponse"

    availability_to_promise_response_coded: AvailabilityToPromiseResponseCoded = field(
        metadata={
            "name": "AvailabilityToPromiseResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    availability_to_promise_response_coded_other: Optional[
        AvailabilityToPromiseResponseCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseResponseCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AvailabilityDeliveryOption:
    availability_delivery_option_coded: AvailabilityDeliveryOptionCoded = (
        field(
            metadata={
                "name": "AvailabilityDeliveryOptionCoded",
                "type": "Element",
                "required": True,
            }
        )
    )
    availability_delivery_option_coded_other: Optional[
        AvailabilityDeliveryOptionCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "AvailabilityDeliveryOptionCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AvailabilityResponseHeaderTransport:
    transport_routing: TransportRouting = field(
        metadata={
            "name": "TransportRouting",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityResponseId:
    class Meta:
        name = "AvailabilityResponseID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityResponseListOfAttachment:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityShipToParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseId:
    class Meta:
        name = "AvailabilityToPromiseID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromisePurpose:
    availability_to_promise_purpose_coded: AvailabilityToPromisePurposeCoded = field(
        metadata={
            "name": "AvailabilityToPromisePurposeCoded",
            "type": "Element",
            "required": True,
        }
    )
    availability_to_promise_purpose_coded_other: Optional[
        AvailabilityToPromisePurposeCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromisePurposeCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseResponseBaseItemDetail:
    base_item_detail: BaseItemDetail = field(
        metadata={
            "name": "BaseItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseResponseDeliveryDetail:
    delivery_detail: DeliveryDetail = field(
        metadata={
            "name": "DeliveryDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseResponseItemListOfAttachment:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseResponseSummary:
    total_number_of_line_items: Optional[TotalNumberOfLineItems] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItems",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseResponseTransportDetail:
    transport: Transport = field(
        metadata={
            "name": "Transport",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RespondingParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityResponseDeliveryOption:
    availability_delivery_option: AvailabilityDeliveryOption = field(
        metadata={
            "name": "AvailabilityDeliveryOption",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseItemResponse:
    availability_to_promise_purpose: AvailabilityToPromisePurpose = field(
        metadata={
            "name": "AvailabilityToPromisePurpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseResponseHeader:
    availability_response_id: AvailabilityResponseId = field(
        metadata={
            "name": "AvailabilityResponseID",
            "type": "Element",
            "required": True,
        }
    )
    availability_response_issue_date: AvailabilityResponseIssueDate = field(
        metadata={
            "name": "AvailabilityResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    availability_to_promise_id: AvailabilityToPromiseId = field(
        metadata={
            "name": "AvailabilityToPromiseID",
            "type": "Element",
            "required": True,
        }
    )
    atpresponse: Atpresponse = field(
        metadata={
            "name": "ATPResponse",
            "type": "Element",
            "required": True,
        }
    )
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        },
    )
    availability_response_delivery_option: AvailabilityResponseDeliveryOption = field(
        metadata={
            "name": "AvailabilityResponseDeliveryOption",
            "type": "Element",
            "required": True,
        }
    )
    atpcheck_type: Optional[AtpcheckType] = field(
        default=None,
        metadata={
            "name": "ATPCheckType",
            "type": "Element",
        },
    )
    initiating_party: InitiatingParty = field(
        metadata={
            "name": "InitiatingParty",
            "type": "Element",
            "required": True,
        }
    )
    responding_party: Optional[RespondingParty] = field(
        default=None,
        metadata={
            "name": "RespondingParty",
            "type": "Element",
        },
    )
    availability_ship_to_party: Optional[AvailabilityShipToParty] = field(
        default=None,
        metadata={
            "name": "AvailabilityShipToParty",
            "type": "Element",
        },
    )
    availability_response_header_transport: Optional[
        AvailabilityResponseHeaderTransport
    ] = field(
        default=None,
        metadata={
            "name": "AvailabilityResponseHeaderTransport",
            "type": "Element",
        },
    )
    general_note: Optional[GeneralNote] = field(
        default=None,
        metadata={
            "name": "GeneralNote",
            "type": "Element",
        },
    )
    availability_response_list_of_attachment: Optional[
        AvailabilityResponseListOfAttachment
    ] = field(
        default=None,
        metadata={
            "name": "AvailabilityResponseListOfAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseResponseItemDetail:
    availability_to_promise_item_response: Optional[
        AvailabilityToPromiseItemResponse
    ] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseItemResponse",
            "type": "Element",
        },
    )
    availability_to_promise_response_base_item_detail: AvailabilityToPromiseResponseBaseItemDetail = field(
        metadata={
            "name": "AvailabilityToPromiseResponseBaseItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    availability_to_promise_response_delivery_detail: Optional[
        AvailabilityToPromiseResponseDeliveryDetail
    ] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseResponseDeliveryDetail",
            "type": "Element",
        },
    )
    availability_to_promise_response_transport_detail: Optional[
        AvailabilityToPromiseResponseTransportDetail
    ] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseResponseTransportDetail",
            "type": "Element",
        },
    )
    availability_to_promise_response_item_list_of_attachment: Optional[
        AvailabilityToPromiseResponseItemListOfAttachment
    ] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseResponseItemListOfAttachment",
            "type": "Element",
        },
    )
    general_note: Optional[GeneralNote] = field(
        default=None,
        metadata={
            "name": "GeneralNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfAvailabilityToPromiseResponseItemDetail:
    availability_to_promise_response_item_detail: List[
        AvailabilityToPromiseResponseItemDetail
    ] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityToPromiseResponseItemDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseResponseDetail:
    list_of_availability_to_promise_response_item_detail: Optional[
        ListOfAvailabilityToPromiseResponseItemDetail
    ] = field(
        default=None,
        metadata={
            "name": "ListOfAvailabilityToPromiseResponseItemDetail",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseResponse:
    availability_to_promise_response_header: AvailabilityToPromiseResponseHeader = field(
        metadata={
            "name": "AvailabilityToPromiseResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
    availability_to_promise_response_detail: Optional[
        AvailabilityToPromiseResponseDetail
    ] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseResponseDetail",
            "type": "Element",
        },
    )
    availability_to_promise_response_summary: Optional[
        AvailabilityToPromiseResponseSummary
    ] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseResponseSummary",
            "type": "Element",
        },
    )
