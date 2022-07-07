from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Language,
    ListOfAttachment,
    ListOfReferenceCoded,
    Purpose,
    Reference,
)
from xcbl.models.order_request import (
    BuyerParty,
    ListOfStructuredNote,
    SellerParty,
)
from xcbl.models.planning_schedule import (
    LocationGroupedPlanningDetail,
    MaterialGroupedPlanningDetail,
    PlanningScheduleHeader,
    PlanningScheduleSummary,
)


@dataclass
class ResponseType:
    response_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResponseTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    response_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResponseTypeCodedOther",
            "type": "Element",
        }
    )


@dataclass
class ChangedLocationGroupedPlanningDetail:
    location_grouped_planning_detail: Optional[LocationGroupedPlanningDetail] = field(
        default=None,
        metadata={
            "name": "LocationGroupedPlanningDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ChangedMaterialGroupedPlanningDetail:
    material_grouped_planning_detail: Optional[MaterialGroupedPlanningDetail] = field(
        default=None,
        metadata={
            "name": "MaterialGroupedPlanningDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ChangedPlanningScheduleHeader:
    planning_schedule_header: Optional[PlanningScheduleHeader] = field(
        default=None,
        metadata={
            "name": "PlanningScheduleHeader",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OriginalLocationGroupedPlanningDetail:
    location_grouped_planning_detail: Optional[LocationGroupedPlanningDetail] = field(
        default=None,
        metadata={
            "name": "LocationGroupedPlanningDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OriginalMaterialGroupedPlanningDetail:
    material_grouped_planning_detail: Optional[MaterialGroupedPlanningDetail] = field(
        default=None,
        metadata={
            "name": "MaterialGroupedPlanningDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OriginalPlanningScheduleHeader:
    planning_schedule_header: Optional[PlanningScheduleHeader] = field(
        default=None,
        metadata={
            "name": "PlanningScheduleHeader",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PlanningScheduleResponseSummary:
    planning_schedule_summary: Optional[PlanningScheduleSummary] = field(
        default=None,
        metadata={
            "name": "PlanningScheduleSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ScheduleReference:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LocationGroupedPlanningResponse:
    detail_response_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "DetailResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    detail_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "DetailResponseCodedOther",
            "type": "Element",
        }
    )
    original_location_grouped_planning_detail: Optional[OriginalLocationGroupedPlanningDetail] = field(
        default=None,
        metadata={
            "name": "OriginalLocationGroupedPlanningDetail",
            "type": "Element",
        }
    )
    changed_location_grouped_planning_detail: Optional[ChangedLocationGroupedPlanningDetail] = field(
        default=None,
        metadata={
            "name": "ChangedLocationGroupedPlanningDetail",
            "type": "Element",
        }
    )
    line_item_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineItemNote",
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
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        }
    )


@dataclass
class MaterialGroupedPlanningResponse:
    detail_response_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "DetailResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    detail_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "DetailResponseCodedOther",
            "type": "Element",
        }
    )
    original_material_grouped_planning_detail: Optional[OriginalMaterialGroupedPlanningDetail] = field(
        default=None,
        metadata={
            "name": "OriginalMaterialGroupedPlanningDetail",
            "type": "Element",
        }
    )
    changed_material_grouped_planning_detail: Optional[ChangedMaterialGroupedPlanningDetail] = field(
        default=None,
        metadata={
            "name": "ChangedMaterialGroupedPlanningDetail",
            "type": "Element",
        }
    )
    line_item_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineItemNote",
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
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        }
    )


@dataclass
class PlanningScheduleResponseHeader:
    schedule_response_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScheduleResponseID",
            "type": "Element",
            "required": True,
        }
    )
    schedule_response_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScheduleResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    schedule_reference: Optional[ScheduleReference] = field(
        default=None,
        metadata={
            "name": "ScheduleReference",
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
    buyer_party: Optional[BuyerParty] = field(
        default=None,
        metadata={
            "name": "BuyerParty",
            "type": "Element",
            "required": True,
        }
    )
    seller_party: Optional[SellerParty] = field(
        default=None,
        metadata={
            "name": "SellerParty",
            "type": "Element",
            "required": True,
        }
    )
    purpose: Optional[Purpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )
    response_type: Optional[ResponseType] = field(
        default=None,
        metadata={
            "name": "ResponseType",
            "type": "Element",
            "required": True,
        }
    )
    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    original_planning_schedule_header: Optional[OriginalPlanningScheduleHeader] = field(
        default=None,
        metadata={
            "name": "OriginalPlanningScheduleHeader",
            "type": "Element",
        }
    )
    changed_planning_schedule_header: Optional[ChangedPlanningScheduleHeader] = field(
        default=None,
        metadata={
            "name": "ChangedPlanningScheduleHeader",
            "type": "Element",
        }
    )
    planning_schedule_response_header_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlanningScheduleResponseHeaderNote",
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
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        }
    )


@dataclass
class ListOfLocationGroupedPlanningResponse:
    location_grouped_planning_response: List[LocationGroupedPlanningResponse] = field(
        default_factory=list,
        metadata={
            "name": "LocationGroupedPlanningResponse",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfMaterialGroupedPlanningResponse:
    material_grouped_planning_response: List[MaterialGroupedPlanningResponse] = field(
        default_factory=list,
        metadata={
            "name": "MaterialGroupedPlanningResponse",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class PlanningScheduleResponse:
    planning_schedule_response_header: Optional[PlanningScheduleResponseHeader] = field(
        default=None,
        metadata={
            "name": "PlanningScheduleResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_location_grouped_planning_response: Optional[ListOfLocationGroupedPlanningResponse] = field(
        default=None,
        metadata={
            "name": "ListOfLocationGroupedPlanningResponse",
            "type": "Element",
            "required": True,
        }
    )
    list_of_material_grouped_planning_response: Optional[ListOfMaterialGroupedPlanningResponse] = field(
        default=None,
        metadata={
            "name": "ListOfMaterialGroupedPlanningResponse",
            "type": "Element",
            "required": True,
        }
    )
    planning_schedule_response_summary: Optional[PlanningScheduleResponseSummary] = field(
        default=None,
        metadata={
            "name": "PlanningScheduleResponseSummary",
            "type": "Element",
        }
    )
