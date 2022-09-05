from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    DeliveryDetail,
    InitiatingParty,
    ListOfAttachment,
    ListOfReferenceCoded,
    Party,
    Reference,
    Transport,
)
from xcbl.models.availability_check_result import AvailabilityShipToParty
from xcbl.models.goods_receipt import TransportRouting
from xcbl.models.order_request import BaseItemDetail


@dataclass(kw_only=True)
class AtpcheckType:
    class Meta:
        name = "ATPCheckType"

    atpcheck_type_coded: str = field(
        metadata={
            "name": "ATPCheckTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    atpcheck_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATPCheckTypeCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Atpresponse:
    class Meta:
        name = "ATPResponse"

    availability_to_promise_response_coded: str = field(
        metadata={
            "name": "AvailabilityToPromiseResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    availability_to_promise_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseResponseCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AvailabilityDeliveryOption:
    availability_delivery_option_coded: str = field(
        metadata={
            "name": "AvailabilityDeliveryOptionCoded",
            "type": "Element",
            "required": True,
        }
    )
    availability_delivery_option_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvailabilityDeliveryOptionCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromisePurpose:
    availability_to_promise_purpose_coded: str = field(
        metadata={
            "name": "AvailabilityToPromisePurposeCoded",
            "type": "Element",
            "required": True,
        }
    )
    availability_to_promise_purpose_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromisePurposeCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseSummary:
    total_number_of_line_items: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItems",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AvailabilityId:
    class Meta:
        name = "AvailabilityID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseBaseItemDetail:
    base_item_detail: BaseItemDetail = field(
        metadata={
            "name": "BaseItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseDeliveryDetail:
    delivery_detail: DeliveryDetail = field(
        metadata={
            "name": "DeliveryDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseHeaderTransport:
    transport_routing: TransportRouting = field(
        metadata={
            "name": "TransportRouting",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseItemListOfAttachment:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseListOfAttachment:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseTransportDetail:
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
class AvailabilityToPromiseHeader:
    availability_id: AvailabilityId = field(
        metadata={
            "name": "AvailabilityID",
            "type": "Element",
            "required": True,
        }
    )
    availability_issue_date: str = field(
        metadata={
            "name": "AvailabilityIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        }
    )
    availability_to_promise_purpose: AvailabilityToPromisePurpose = field(
        metadata={
            "name": "AvailabilityToPromisePurpose",
            "type": "Element",
            "required": True,
        }
    )
    availability_delivery_option: AvailabilityDeliveryOption = field(
        metadata={
            "name": "AvailabilityDeliveryOption",
            "type": "Element",
            "required": True,
        }
    )
    atpcheck_type: Optional[AtpcheckType] = field(
        default=None,
        metadata={
            "name": "ATPCheckType",
            "type": "Element",
        }
    )
    atpresponse: Optional[Atpresponse] = field(
        default=None,
        metadata={
            "name": "ATPResponse",
            "type": "Element",
        }
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
        }
    )
    availability_ship_to_party: Optional[AvailabilityShipToParty] = field(
        default=None,
        metadata={
            "name": "AvailabilityShipToParty",
            "type": "Element",
        }
    )
    availability_to_promise_header_transport: Optional[AvailabilityToPromiseHeaderTransport] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseHeaderTransport",
            "type": "Element",
        }
    )
    general_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralNote",
            "type": "Element",
        }
    )
    availability_to_promise_list_of_attachment: Optional[AvailabilityToPromiseListOfAttachment] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseListOfAttachment",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseItemDetail:
    availability_to_promise_base_item_detail: AvailabilityToPromiseBaseItemDetail = field(
        metadata={
            "name": "AvailabilityToPromiseBaseItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    availability_to_promise_delivery_detail: Optional[AvailabilityToPromiseDeliveryDetail] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseDeliveryDetail",
            "type": "Element",
        }
    )
    availability_to_promise_transport_detail: Optional[AvailabilityToPromiseTransportDetail] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseTransportDetail",
            "type": "Element",
        }
    )
    availability_to_promise_item_list_of_attachment: Optional[AvailabilityToPromiseItemListOfAttachment] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseItemListOfAttachment",
            "type": "Element",
        }
    )
    general_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralNote",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfAvailabilityToPromiseItemDetail:
    availability_to_promise_item_detail: List[AvailabilityToPromiseItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityToPromiseItemDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseDetail:
    list_of_availability_to_promise_item_detail: Optional[ListOfAvailabilityToPromiseItemDetail] = field(
        default=None,
        metadata={
            "name": "ListOfAvailabilityToPromiseItemDetail",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromise:
    availability_to_promise_header: AvailabilityToPromiseHeader = field(
        metadata={
            "name": "AvailabilityToPromiseHeader",
            "type": "Element",
            "required": True,
        }
    )
    availability_to_promise_detail: Optional[AvailabilityToPromiseDetail] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseDetail",
            "type": "Element",
        }
    )
    availability_to_promise_summary: Optional[AvailabilityToPromiseSummary] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseSummary",
            "type": "Element",
        }
    )
