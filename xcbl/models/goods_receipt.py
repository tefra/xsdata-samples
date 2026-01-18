from __future__ import annotations

from dataclasses import dataclass, field

from xcbl.models.order_confirmation import DeliveryComplete
from xcbl.models.remittance_advice import PurchaseOrderLineItemNumber
from xcbl.models.shipping_schedule import ListOfPackageDetail
from xcbl.models.shipping_schedule_response import (
    ListOfTransportRouting,
    LocationId,
    ReleaseNumber,
    RouteId,
    ScheduleOrderReference,
    ScheduleParty,
)
from xcbl.models.sourcing_result import (
    ItemIdentifiers,
    ItemPackagingReference,
    LineItemNum,
    LineItemType,
    ListOfAttachment,
    ListOfDateCoded,
    ListOfNameValueSet,
    ListOfReferenceCoded,
    ListOfStructuredNote,
    ParentItemNumber,
    Quantity,
    RequestedDeliveryDate,
    TermsOfDelivery,
)
from xcbl.models.sourcing_result_response import Purpose
from xcbl.models.time_series_response import Party
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import Language


@dataclass(kw_only=True)
class AsnlineItemNumber:
    class Meta:
        name = "ASNLineItemNumber"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ChangeOrderSequenceNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DeliveryStageQualifierCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DeliveryStageQualifierOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DiscrepancyCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DiscrepancyCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ElementIdentifierCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ElementIdentifierCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class GoodsConditionCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class GoodsConditionCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class GoodsReceiptDetailNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class GoodsReceiptHeaderNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class GoodsReceiptId:
    class Meta:
        name = "GoodsReceiptID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class GoodsReceiptIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class GoodsReceiptTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class GoodsReceiptTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class IdentifyingReference:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ShipByDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class UnacceptablePackaging:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Asnreference:
    class Meta:
        name = "ASNReference"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class DestinationRef:
    route_id: RouteId = field(
        metadata={
            "name": "RouteID",
            "type": "Element",
            "required": True,
        }
    )
    location_id: LocationId = field(
        metadata={
            "name": "LocationID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class GoodsCondition:
    element_identifier_coded: None | ElementIdentifierCoded = field(
        default=None,
        metadata={
            "name": "ElementIdentifierCoded",
            "type": "Element",
        },
    )
    element_identifier_coded_other: None | ElementIdentifierCodedOther = field(
        default=None,
        metadata={
            "name": "ElementIdentifierCodedOther",
            "type": "Element",
        },
    )
    identifying_reference: None | IdentifyingReference = field(
        default=None,
        metadata={
            "name": "IdentifyingReference",
            "type": "Element",
        },
    )
    delivery_stage_qualifier_coded: None | DeliveryStageQualifierCoded = field(
        default=None,
        metadata={
            "name": "DeliveryStageQualifierCoded",
            "type": "Element",
        },
    )
    delivery_stage_qualifier_other: None | DeliveryStageQualifierOther = field(
        default=None,
        metadata={
            "name": "DeliveryStageQualifierOther",
            "type": "Element",
        },
    )
    goods_condition_coded: GoodsConditionCoded = field(
        metadata={
            "name": "GoodsConditionCoded",
            "type": "Element",
            "required": True,
        }
    )
    goods_condition_coded_other: None | GoodsConditionCodedOther = field(
        default=None,
        metadata={
            "name": "GoodsConditionCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class GoodsReceiptLanguage:
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class GoodsReceiptOrderReference:
    schedule_order_reference: None | ScheduleOrderReference = field(
        default=None,
        metadata={
            "name": "ScheduleOrderReference",
            "type": "Element",
        },
    )
    release_number: None | ReleaseNumber = field(
        default=None,
        metadata={
            "name": "ReleaseNumber",
            "type": "Element",
        },
    )
    change_order_sequence_number: None | ChangeOrderSequenceNumber = field(
        default=None,
        metadata={
            "name": "ChangeOrderSequenceNumber",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class GoodsReceiptParty:
    schedule_party: ScheduleParty = field(
        metadata={
            "name": "ScheduleParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class GoodsReceiptPurpose:
    purpose: Purpose = field(
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ItemShipFromParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ItemShipToParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfGoodsReceiptPackageDetail:
    list_of_package_detail: ListOfPackageDetail = field(
        metadata={
            "name": "ListOfPackageDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OtherItemDates:
    list_of_date_coded: ListOfDateCoded = field(
        metadata={
            "name": "ListOfDateCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuantityDifference:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuantityReceived:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuantityShipped:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class GoodsReceiptItemOrderReference:
    goods_receipt_order_reference: GoodsReceiptOrderReference = field(
        metadata={
            "name": "GoodsReceiptOrderReference",
            "type": "Element",
            "required": True,
        }
    )
    purchase_order_line_item_number: None | PurchaseOrderLineItemNumber = (
        field(
            default=None,
            metadata={
                "name": "PurchaseOrderLineItemNumber",
                "type": "Element",
            },
        )
    )


@dataclass(kw_only=True)
class LineItemGoodsCondition:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )
    goods_condition: GoodsCondition = field(
        metadata={
            "name": "GoodsCondition",
            "type": "Element",
            "required": True,
        }
    )
    discrepancy_coded: None | DiscrepancyCoded = field(
        default=None,
        metadata={
            "name": "DiscrepancyCoded",
            "type": "Element",
        },
    )
    discrepancy_coded_other: None | DiscrepancyCodedOther = field(
        default=None,
        metadata={
            "name": "DiscrepancyCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfDestinationRef:
    destination_ref: list[DestinationRef] = field(
        default_factory=list,
        metadata={
            "name": "DestinationRef",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfGoodsCondition:
    goods_condition: list[GoodsCondition] = field(
        default_factory=list,
        metadata={
            "name": "GoodsCondition",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfGoodsReceiptOrderReference:
    goods_receipt_order_reference: list[GoodsReceiptOrderReference] = field(
        default_factory=list,
        metadata={
            "name": "GoodsReceiptOrderReference",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class GoodsReceiptDeliveryDetail:
    item_packaging_reference: None | ItemPackagingReference = field(
        default=None,
        metadata={
            "name": "ItemPackagingReference",
            "type": "Element",
        },
    )
    list_of_destination_ref: None | ListOfDestinationRef = field(
        default=None,
        metadata={
            "name": "ListOfDestinationRef",
            "type": "Element",
        },
    )
    requested_delivery_date: None | RequestedDeliveryDate = field(
        default=None,
        metadata={
            "name": "RequestedDeliveryDate",
            "type": "Element",
        },
    )
    ship_by_date: None | ShipByDate = field(
        default=None,
        metadata={
            "name": "ShipByDate",
            "type": "Element",
        },
    )
    other_item_dates: None | OtherItemDates = field(
        default=None,
        metadata={
            "name": "OtherItemDates",
            "type": "Element",
        },
    )
    item_ship_to_party: None | ItemShipToParty = field(
        default=None,
        metadata={
            "name": "ItemShipToParty",
            "type": "Element",
        },
    )
    item_ship_from_party: None | ItemShipFromParty = field(
        default=None,
        metadata={
            "name": "ItemShipFromParty",
            "type": "Element",
        },
    )
    terms_of_delivery: None | TermsOfDelivery = field(
        default=None,
        metadata={
            "name": "TermsOfDelivery",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class GoodsReceiptReferences:
    asnreference: None | Asnreference = field(
        default=None,
        metadata={
            "name": "ASNReference",
            "type": "Element",
        },
    )
    list_of_goods_receipt_order_reference: (
        None | ListOfGoodsReceiptOrderReference
    ) = field(
        default=None,
        metadata={
            "name": "ListOfGoodsReceiptOrderReference",
            "type": "Element",
        },
    )
    list_of_reference_coded: None | ListOfReferenceCoded = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfGoodsReceiptItemOrderReference:
    goods_receipt_item_order_reference: list[
        GoodsReceiptItemOrderReference
    ] = field(
        default_factory=list,
        metadata={
            "name": "GoodsReceiptItemOrderReference",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfLineItemGoodsCondition:
    line_item_goods_condition: list[LineItemGoodsCondition] = field(
        default_factory=list,
        metadata={
            "name": "LineItemGoodsCondition",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class GoodsReceiptHeader:
    goods_receipt_id: GoodsReceiptId = field(
        metadata={
            "name": "GoodsReceiptID",
            "type": "Element",
            "required": True,
        }
    )
    goods_receipt_issue_date: GoodsReceiptIssueDate = field(
        metadata={
            "name": "GoodsReceiptIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    goods_receipt_purpose: GoodsReceiptPurpose = field(
        metadata={
            "name": "GoodsReceiptPurpose",
            "type": "Element",
            "required": True,
        }
    )
    goods_receipt_type_coded: GoodsReceiptTypeCoded = field(
        metadata={
            "name": "GoodsReceiptTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    goods_receipt_type_coded_other: None | GoodsReceiptTypeCodedOther = field(
        default=None,
        metadata={
            "name": "GoodsReceiptTypeCodedOther",
            "type": "Element",
        },
    )
    list_of_goods_condition: None | ListOfGoodsCondition = field(
        default=None,
        metadata={
            "name": "ListOfGoodsCondition",
            "type": "Element",
        },
    )
    goods_receipt_references: None | GoodsReceiptReferences = field(
        default=None,
        metadata={
            "name": "GoodsReceiptReferences",
            "type": "Element",
        },
    )
    delivery_complete: None | DeliveryComplete = field(
        default=None,
        metadata={
            "name": "DeliveryComplete",
            "type": "Element",
        },
    )
    goods_receipt_language: GoodsReceiptLanguage = field(
        metadata={
            "name": "GoodsReceiptLanguage",
            "type": "Element",
            "required": True,
        }
    )
    goods_receipt_party: GoodsReceiptParty = field(
        metadata={
            "name": "GoodsReceiptParty",
            "type": "Element",
            "required": True,
        }
    )
    terms_of_delivery: list[TermsOfDelivery] = field(
        default_factory=list,
        metadata={
            "name": "TermsOfDelivery",
            "type": "Element",
        },
    )
    list_of_transport_routing: None | ListOfTransportRouting = field(
        default=None,
        metadata={
            "name": "ListOfTransportRouting",
            "type": "Element",
        },
    )
    goods_receipt_header_note: None | GoodsReceiptHeaderNote = field(
        default=None,
        metadata={
            "name": "GoodsReceiptHeaderNote",
            "type": "Element",
        },
    )
    list_of_structured_note: None | ListOfStructuredNote = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    list_of_name_value_set: None | ListOfNameValueSet = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        },
    )
    list_of_attachment: None | ListOfAttachment = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class GoodsReceiptLineItemReferences:
    asnreference: None | Asnreference = field(
        default=None,
        metadata={
            "name": "ASNReference",
            "type": "Element",
        },
    )
    asnline_item_number: None | AsnlineItemNumber = field(
        default=None,
        metadata={
            "name": "ASNLineItemNumber",
            "type": "Element",
        },
    )
    list_of_goods_receipt_item_order_reference: (
        None | ListOfGoodsReceiptItemOrderReference
    ) = field(
        default=None,
        metadata={
            "name": "ListOfGoodsReceiptItemOrderReference",
            "type": "Element",
        },
    )
    list_of_reference_coded: None | ListOfReferenceCoded = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class GoodsReceiptItemDetail:
    line_item_num: LineItemNum = field(
        metadata={
            "name": "LineItemNum",
            "type": "Element",
            "required": True,
        }
    )
    line_item_type: LineItemType = field(
        metadata={
            "name": "LineItemType",
            "type": "Element",
            "required": True,
        }
    )
    parent_item_number: ParentItemNumber = field(
        metadata={
            "name": "ParentItemNumber",
            "type": "Element",
            "required": True,
        }
    )
    item_identifiers: ItemIdentifiers = field(
        metadata={
            "name": "ItemIdentifiers",
            "type": "Element",
            "required": True,
        }
    )
    quantity_shipped: QuantityShipped = field(
        metadata={
            "name": "QuantityShipped",
            "type": "Element",
            "required": True,
        }
    )
    quantity_received: QuantityReceived = field(
        metadata={
            "name": "QuantityReceived",
            "type": "Element",
            "required": True,
        }
    )
    quantity_difference: None | QuantityDifference = field(
        default=None,
        metadata={
            "name": "QuantityDifference",
            "type": "Element",
        },
    )
    list_of_line_item_goods_condition: None | ListOfLineItemGoodsCondition = (
        field(
            default=None,
            metadata={
                "name": "ListOfLineItemGoodsCondition",
                "type": "Element",
            },
        )
    )
    unacceptable_packaging: None | UnacceptablePackaging = field(
        default=None,
        metadata={
            "name": "UnacceptablePackaging",
            "type": "Element",
        },
    )
    goods_receipt_line_item_references: (
        None | GoodsReceiptLineItemReferences
    ) = field(
        default=None,
        metadata={
            "name": "GoodsReceiptLineItemReferences",
            "type": "Element",
        },
    )
    goods_receipt_delivery_detail: None | GoodsReceiptDeliveryDetail = field(
        default=None,
        metadata={
            "name": "GoodsReceiptDeliveryDetail",
            "type": "Element",
        },
    )
    list_of_structured_note: None | ListOfStructuredNote = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    list_of_name_value_set: None | ListOfNameValueSet = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        },
    )
    list_of_attachment: None | ListOfAttachment = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        },
    )
    goods_receipt_detail_note: None | GoodsReceiptDetailNote = field(
        default=None,
        metadata={
            "name": "GoodsReceiptDetailNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfGoodsReceiptItemDetail:
    goods_receipt_item_detail: list[GoodsReceiptItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "GoodsReceiptItemDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class GoodsReceiptDetail:
    list_of_goods_receipt_item_detail: ListOfGoodsReceiptItemDetail = field(
        metadata={
            "name": "ListOfGoodsReceiptItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    list_of_goods_receipt_package_detail: (
        None | ListOfGoodsReceiptPackageDetail
    ) = field(
        default=None,
        metadata={
            "name": "ListOfGoodsReceiptPackageDetail",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class GoodsReceipt:
    goods_receipt_header: GoodsReceiptHeader = field(
        metadata={
            "name": "GoodsReceiptHeader",
            "type": "Element",
            "required": True,
        }
    )
    goods_receipt_detail: None | GoodsReceiptDetail = field(
        default=None,
        metadata={
            "name": "GoodsReceiptDetail",
            "type": "Element",
        },
    )
