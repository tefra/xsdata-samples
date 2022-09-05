from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    CarrierId,
    Identifier,
    ItemPackagingReference,
    Language,
    ListOfAttachment,
    ListOfDateCoded,
    ListOfReferenceCoded,
    ListOfTransportEquipment,
    Location,
    Party,
    Purpose,
    Quantity,
    Reference,
    TermsOfDelivery,
    TransitDirection,
    TransportMeans,
    TransportMode,
)
from xcbl.models.order_request import (
    ItemIdentifiers,
    LineItemNum,
    LineItemType,
    ListOfNameValueSet,
    ListOfPackageDetail,
    ListOfQuantityCoded,
    ListOfStructuredNote,
    ParentItemNumber,
)
from xcbl.models.planning_schedule import (
    ScheduleOrderReference,
    ScheduleParty,
)


@dataclass(kw_only=True)
class DestinationRef:
    route_id: str = field(
        metadata={
            "name": "RouteID",
            "type": "Element",
            "required": True,
        }
    )
    location_id: str = field(
        metadata={
            "name": "LocationID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class GoodsCondition:
    element_identifier_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElementIdentifierCoded",
            "type": "Element",
        }
    )
    element_identifier_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElementIdentifierCodedOther",
            "type": "Element",
        }
    )
    identifying_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentifyingReference",
            "type": "Element",
        }
    )
    delivery_stage_qualifier_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeliveryStageQualifierCoded",
            "type": "Element",
        }
    )
    delivery_stage_qualifier_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeliveryStageQualifierOther",
            "type": "Element",
        }
    )
    goods_condition_coded: str = field(
        metadata={
            "name": "GoodsConditionCoded",
            "type": "Element",
            "required": True,
        }
    )
    goods_condition_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "GoodsConditionCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ServiceLevel:
    service_level_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceLevelCoded",
            "type": "Element",
        }
    )
    service_level_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceLevelCodedOther",
            "type": "Element",
        }
    )
    service_level_reason_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceLevelReasonCoded",
            "type": "Element",
        }
    )
    service_level_reason_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceLevelReasonCodedOther",
            "type": "Element",
        }
    )
    service_level_responsibility_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceLevelResponsibilityCoded",
            "type": "Element",
        }
    )
    service_level_responsibility_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceLevelResponsibilityCodedOther",
            "type": "Element",
        }
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
    schedule_order_reference: Optional[ScheduleOrderReference] = field(
        default=None,
        metadata={
            "name": "ScheduleOrderReference",
            "type": "Element",
        }
    )
    release_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReleaseNumber",
            "type": "Element",
        }
    )
    change_order_sequence_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChangeOrderSequenceNumber",
            "type": "Element",
        }
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
class LadingQuantity:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
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
    discrepancy_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscrepancyCoded",
            "type": "Element",
        }
    )
    discrepancy_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscrepancyCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfDestinationRef:
    destination_ref: List[DestinationRef] = field(
        default_factory=list,
        metadata={
            "name": "DestinationRef",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfGoodsCondition:
    goods_condition: List[GoodsCondition] = field(
        default_factory=list,
        metadata={
            "name": "GoodsCondition",
            "type": "Element",
            "min_occurs": 1,
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
class TransportLocation:
    location: Location = field(
        metadata={
            "name": "Location",
            "type": "Element",
            "required": True,
        }
    )
    location_id: str = field(
        metadata={
            "name": "LocationID",
            "type": "Element",
            "required": True,
        }
    )
    sequence: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sequence",
            "type": "Element",
        }
    )
    estimated_arrival_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EstimatedArrivalDate",
            "type": "Element",
        }
    )
    actual_arrival_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ActualArrivalDate",
            "type": "Element",
        }
    )
    estimated_departure_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EstimatedDepartureDate",
            "type": "Element",
        }
    )
    actual_departure_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ActualDepartureDate",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class TransportMeansIdentifier:
    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TransportMeansReference:
    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class EndTransportLocation:
    transport_location: TransportLocation = field(
        metadata={
            "name": "TransportLocation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class GoodsReceiptDeliveryDetail:
    item_packaging_reference: Optional[ItemPackagingReference] = field(
        default=None,
        metadata={
            "name": "ItemPackagingReference",
            "type": "Element",
        }
    )
    list_of_destination_ref: Optional[ListOfDestinationRef] = field(
        default=None,
        metadata={
            "name": "ListOfDestinationRef",
            "type": "Element",
        }
    )
    requested_delivery_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestedDeliveryDate",
            "type": "Element",
        }
    )
    ship_by_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShipByDate",
            "type": "Element",
        }
    )
    other_item_dates: Optional[OtherItemDates] = field(
        default=None,
        metadata={
            "name": "OtherItemDates",
            "type": "Element",
        }
    )
    item_ship_to_party: Optional[ItemShipToParty] = field(
        default=None,
        metadata={
            "name": "ItemShipToParty",
            "type": "Element",
        }
    )
    item_ship_from_party: Optional[ItemShipFromParty] = field(
        default=None,
        metadata={
            "name": "ItemShipFromParty",
            "type": "Element",
        }
    )
    terms_of_delivery: Optional[TermsOfDelivery] = field(
        default=None,
        metadata={
            "name": "TermsOfDelivery",
            "type": "Element",
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
    purchase_order_line_item_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurchaseOrderLineItemNumber",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class InterimTransportLocation:
    transport_location: TransportLocation = field(
        metadata={
            "name": "TransportLocation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfGoodsReceiptOrderReference:
    goods_receipt_order_reference: List[GoodsReceiptOrderReference] = field(
        default_factory=list,
        metadata={
            "name": "GoodsReceiptOrderReference",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfLineItemGoodsCondition:
    line_item_goods_condition: List[LineItemGoodsCondition] = field(
        default_factory=list,
        metadata={
            "name": "LineItemGoodsCondition",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class StartTransportLocation:
    transport_location: TransportLocation = field(
        metadata={
            "name": "TransportLocation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TransportQuantities:
    lading_quantity: Optional[LadingQuantity] = field(
        default=None,
        metadata={
            "name": "LadingQuantity",
            "type": "Element",
        }
    )
    list_of_quantity_coded: Optional[ListOfQuantityCoded] = field(
        default=None,
        metadata={
            "name": "ListOfQuantityCoded",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class GoodsReceiptReferences:
    asnreference: Optional[Asnreference] = field(
        default=None,
        metadata={
            "name": "ASNReference",
            "type": "Element",
        }
    )
    list_of_goods_receipt_order_reference: Optional[ListOfGoodsReceiptOrderReference] = field(
        default=None,
        metadata={
            "name": "ListOfGoodsReceiptOrderReference",
            "type": "Element",
        }
    )
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfGoodsReceiptItemOrderReference:
    goods_receipt_item_order_reference: List[GoodsReceiptItemOrderReference] = field(
        default_factory=list,
        metadata={
            "name": "GoodsReceiptItemOrderReference",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class TransportLocationList:
    start_transport_location: StartTransportLocation = field(
        metadata={
            "name": "StartTransportLocation",
            "type": "Element",
            "required": True,
        }
    )
    interim_transport_location: List[InterimTransportLocation] = field(
        default_factory=list,
        metadata={
            "name": "InterimTransportLocation",
            "type": "Element",
        }
    )
    end_transport_location: EndTransportLocation = field(
        metadata={
            "name": "EndTransportLocation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class GoodsReceiptLineItemReferences:
    asnreference: Optional[Asnreference] = field(
        default=None,
        metadata={
            "name": "ASNReference",
            "type": "Element",
        }
    )
    asnline_item_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ASNLineItemNumber",
            "type": "Element",
        }
    )
    list_of_goods_receipt_item_order_reference: Optional[ListOfGoodsReceiptItemOrderReference] = field(
        default=None,
        metadata={
            "name": "ListOfGoodsReceiptItemOrderReference",
            "type": "Element",
        }
    )
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class TransportRouting:
    transport_route_id: str = field(
        metadata={
            "name": "TransportRouteID",
            "type": "Element",
            "required": True,
        }
    )
    transport_mode: Optional[TransportMode] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
        }
    )
    transport_means: Optional[TransportMeans] = field(
        default=None,
        metadata={
            "name": "TransportMeans",
            "type": "Element",
        }
    )
    transport_means_identifier: Optional[TransportMeansIdentifier] = field(
        default=None,
        metadata={
            "name": "TransportMeansIdentifier",
            "type": "Element",
        }
    )
    transport_means_reference: Optional[TransportMeansReference] = field(
        default=None,
        metadata={
            "name": "TransportMeansReference",
            "type": "Element",
        }
    )
    transport_requirement_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportRequirementCoded",
            "type": "Element",
        }
    )
    transport_requirement_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportRequirementCodedOther",
            "type": "Element",
        }
    )
    carrier_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CarrierName",
            "type": "Element",
        }
    )
    carrier_id: Optional[CarrierId] = field(
        default=None,
        metadata={
            "name": "CarrierID",
            "type": "Element",
        }
    )
    transport_quantities: Optional[TransportQuantities] = field(
        default=None,
        metadata={
            "name": "TransportQuantities",
            "type": "Element",
        }
    )
    cust_shipping_contract_num: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustShippingContractNum",
            "type": "Element",
        }
    )
    service_level: Optional[ServiceLevel] = field(
        default=None,
        metadata={
            "name": "ServiceLevel",
            "type": "Element",
        }
    )
    shipping_instructions: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShippingInstructions",
            "type": "Element",
        }
    )
    transport_leg_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportLegCoded",
            "type": "Element",
        }
    )
    transport_leg_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportLegCodedOther",
            "type": "Element",
        }
    )
    list_of_transport_equipment: Optional[ListOfTransportEquipment] = field(
        default=None,
        metadata={
            "name": "ListOfTransportEquipment",
            "type": "Element",
        }
    )
    transit_direction: Optional[TransitDirection] = field(
        default=None,
        metadata={
            "name": "TransitDirection",
            "type": "Element",
        }
    )
    transport_location_list: TransportLocationList = field(
        metadata={
            "name": "TransportLocationList",
            "type": "Element",
            "required": True,
        }
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
    quantity_difference: Optional[QuantityDifference] = field(
        default=None,
        metadata={
            "name": "QuantityDifference",
            "type": "Element",
        }
    )
    list_of_line_item_goods_condition: Optional[ListOfLineItemGoodsCondition] = field(
        default=None,
        metadata={
            "name": "ListOfLineItemGoodsCondition",
            "type": "Element",
        }
    )
    unacceptable_packaging: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnacceptablePackaging",
            "type": "Element",
        }
    )
    goods_receipt_line_item_references: Optional[GoodsReceiptLineItemReferences] = field(
        default=None,
        metadata={
            "name": "GoodsReceiptLineItemReferences",
            "type": "Element",
        }
    )
    goods_receipt_delivery_detail: Optional[GoodsReceiptDeliveryDetail] = field(
        default=None,
        metadata={
            "name": "GoodsReceiptDeliveryDetail",
            "type": "Element",
        }
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        }
    )
    list_of_name_value_set: Optional[ListOfNameValueSet] = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        }
    )
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        }
    )
    goods_receipt_detail_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "GoodsReceiptDetailNote",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfTransportRouting:
    transport_routing: List[TransportRouting] = field(
        default_factory=list,
        metadata={
            "name": "TransportRouting",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class GoodsReceiptHeader:
    goods_receipt_id: str = field(
        metadata={
            "name": "GoodsReceiptID",
            "type": "Element",
            "required": True,
        }
    )
    goods_receipt_issue_date: str = field(
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
    goods_receipt_type_coded: str = field(
        metadata={
            "name": "GoodsReceiptTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    goods_receipt_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "GoodsReceiptTypeCodedOther",
            "type": "Element",
        }
    )
    list_of_goods_condition: Optional[ListOfGoodsCondition] = field(
        default=None,
        metadata={
            "name": "ListOfGoodsCondition",
            "type": "Element",
        }
    )
    goods_receipt_references: Optional[GoodsReceiptReferences] = field(
        default=None,
        metadata={
            "name": "GoodsReceiptReferences",
            "type": "Element",
        }
    )
    delivery_complete: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeliveryComplete",
            "type": "Element",
        }
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
    terms_of_delivery: List[TermsOfDelivery] = field(
        default_factory=list,
        metadata={
            "name": "TermsOfDelivery",
            "type": "Element",
        }
    )
    list_of_transport_routing: Optional[ListOfTransportRouting] = field(
        default=None,
        metadata={
            "name": "ListOfTransportRouting",
            "type": "Element",
        }
    )
    goods_receipt_header_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "GoodsReceiptHeaderNote",
            "type": "Element",
        }
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        }
    )
    list_of_name_value_set: Optional[ListOfNameValueSet] = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        }
    )
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfGoodsReceiptItemDetail:
    goods_receipt_item_detail: List[GoodsReceiptItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "GoodsReceiptItemDetail",
            "type": "Element",
            "min_occurs": 1,
        }
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
    list_of_goods_receipt_package_detail: Optional[ListOfGoodsReceiptPackageDetail] = field(
        default=None,
        metadata={
            "name": "ListOfGoodsReceiptPackageDetail",
            "type": "Element",
        }
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
    goods_receipt_detail: Optional[GoodsReceiptDetail] = field(
        default=None,
        metadata={
            "name": "GoodsReceiptDetail",
            "type": "Element",
        }
    )
