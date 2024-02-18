from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.shipping_schedule_response import (
    CommitmentLevelCoded,
    CommitmentLevelCodedOther,
    DetailResponseCoded,
    DetailResponseCodedOther,
    ForecastFrequencyCoded,
    ForecastFrequencyCodedOther,
    ItemQuantities,
    ItemReleaseStatusCoded,
    ItemReleaseStatusCodedOther,
    ItemResourceAuthorization,
    ItemScheduleReference,
    RecordKeepingYear,
    ReleaseNumber,
    RequestedResponse,
    ResponseType,
    ScheduleDates,
    ScheduleId,
    ScheduleNote,
    ScheduleParty,
    SchedulePurpose,
    ScheduleQuantities,
    ScheduleReference,
    ScheduleReferences,
    ScheduleResponseId,
    ScheduleResponseIssueDate,
    ScheduleTypeCoded,
    ScheduleTypeCodedOther,
    TotalNumberOfLineItems,
)
from xcbl.models.sourcing_result import (
    BuyerParty,
    CatalogReference,
    ConditionsOfSale,
    CountryOfDestination,
    CountryOfOrigin,
    FinalRecipient,
    HazardousMaterials,
    ItemContractReferences,
    ItemIdentifiers,
    LineItemNote,
    LineItemNum,
    LineItemType,
    ListOfAttachment,
    ListOfItemReferences,
    ListOfQuantityCoded,
    ListOfReferenceCoded,
    ListOfStructuredNote,
    MaxBackOrderQuantity,
    OffCatalogFlag,
    ParentItemNumber,
    QuantityQualifierCoded,
    QuantityQualifierCodedOther,
    SellerParty,
    TotalQuantity,
)
from xcbl.models.sourcing_result_response import Purpose
from xcbl.models.time_series_response import (
    ListOfContact,
    ListOfDimension,
    ListOfPartyCoded,
    Location,
)
from xcbl.models.trading_partner_user_information import (
    Language,
    ValidityDates,
)


@dataclass(kw_only=True)
class PlanningScheduleHeaderNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PlanningScheduleResponseHeaderNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ScheduleIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class BasePlanningDetail:
    line_item_num: LineItemNum = field(
        metadata={
            "name": "LineItemNum",
            "type": "Element",
            "required": True,
        }
    )
    line_item_type: Optional[LineItemType] = field(
        default=None,
        metadata={
            "name": "LineItemType",
            "type": "Element",
        },
    )
    parent_item_number: Optional[ParentItemNumber] = field(
        default=None,
        metadata={
            "name": "ParentItemNumber",
            "type": "Element",
        },
    )
    item_identifiers: Optional[ItemIdentifiers] = field(
        default=None,
        metadata={
            "name": "ItemIdentifiers",
            "type": "Element",
        },
    )
    list_of_dimension: Optional[ListOfDimension] = field(
        default=None,
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
        },
    )
    total_quantity: Optional[TotalQuantity] = field(
        default=None,
        metadata={
            "name": "TotalQuantity",
            "type": "Element",
        },
    )
    max_back_order_quantity: Optional[MaxBackOrderQuantity] = field(
        default=None,
        metadata={
            "name": "MaxBackOrderQuantity",
            "type": "Element",
        },
    )
    list_of_quantity_coded: Optional[ListOfQuantityCoded] = field(
        default=None,
        metadata={
            "name": "ListOfQuantityCoded",
            "type": "Element",
        },
    )
    off_catalog_flag: Optional[OffCatalogFlag] = field(
        default=None,
        metadata={
            "name": "OffCatalogFlag",
            "type": "Element",
        },
    )
    catalog_reference: Optional[CatalogReference] = field(
        default=None,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
        },
    )
    item_contract_references: Optional[ItemContractReferences] = field(
        default=None,
        metadata={
            "name": "ItemContractReferences",
            "type": "Element",
        },
    )
    list_of_item_references: Optional[ListOfItemReferences] = field(
        default=None,
        metadata={
            "name": "ListOfItemReferences",
            "type": "Element",
        },
    )
    country_of_origin: Optional[CountryOfOrigin] = field(
        default=None,
        metadata={
            "name": "CountryOfOrigin",
            "type": "Element",
        },
    )
    country_of_destination: Optional[CountryOfDestination] = field(
        default=None,
        metadata={
            "name": "CountryOfDestination",
            "type": "Element",
        },
    )
    final_recipient: Optional[FinalRecipient] = field(
        default=None,
        metadata={
            "name": "FinalRecipient",
            "type": "Element",
        },
    )
    list_of_party_coded: Optional[ListOfPartyCoded] = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        },
    )
    conditions_of_sale: Optional[ConditionsOfSale] = field(
        default=None,
        metadata={
            "name": "ConditionsOfSale",
            "type": "Element",
        },
    )
    hazardous_materials: Optional[HazardousMaterials] = field(
        default=None,
        metadata={
            "name": "HazardousMaterials",
            "type": "Element",
        },
    )
    record_keeping_year: Optional[RecordKeepingYear] = field(
        default=None,
        metadata={
            "name": "RecordKeepingYear",
            "type": "Element",
        },
    )
    item_schedule_reference: Optional[ItemScheduleReference] = field(
        default=None,
        metadata={
            "name": "ItemScheduleReference",
            "type": "Element",
        },
    )
    forecast_frequency_coded: ForecastFrequencyCoded = field(
        metadata={
            "name": "ForecastFrequencyCoded",
            "type": "Element",
            "required": True,
        }
    )
    forecast_frequency_coded_other: Optional[
        ForecastFrequencyCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "ForecastFrequencyCodedOther",
            "type": "Element",
        },
    )
    item_quantities: Optional[ItemQuantities] = field(
        default=None,
        metadata={
            "name": "ItemQuantities",
            "type": "Element",
        },
    )
    item_release_status_coded: Optional[ItemReleaseStatusCoded] = field(
        default=None,
        metadata={
            "name": "ItemReleaseStatusCoded",
            "type": "Element",
        },
    )
    item_release_status_coded_other: Optional[
        ItemReleaseStatusCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "ItemReleaseStatusCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PlanningScheduleHeader:
    schedule_id: ScheduleId = field(
        metadata={
            "name": "ScheduleID",
            "type": "Element",
            "required": True,
        }
    )
    schedule_issue_date: ScheduleIssueDate = field(
        metadata={
            "name": "ScheduleIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    schedule_references: Optional[ScheduleReferences] = field(
        default=None,
        metadata={
            "name": "ScheduleReferences",
            "type": "Element",
        },
    )
    release_number: Optional[ReleaseNumber] = field(
        default=None,
        metadata={
            "name": "ReleaseNumber",
            "type": "Element",
        },
    )
    schedule_purpose: SchedulePurpose = field(
        metadata={
            "name": "SchedulePurpose",
            "type": "Element",
            "required": True,
        }
    )
    requested_response: Optional[RequestedResponse] = field(
        default=None,
        metadata={
            "name": "RequestedResponse",
            "type": "Element",
        },
    )
    schedule_type_coded: ScheduleTypeCoded = field(
        metadata={
            "name": "ScheduleTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    schedule_type_coded_other: Optional[ScheduleTypeCodedOther] = field(
        default=None,
        metadata={
            "name": "ScheduleTypeCodedOther",
            "type": "Element",
        },
    )
    quantity_qualifier_coded: QuantityQualifierCoded = field(
        metadata={
            "name": "QuantityQualifierCoded",
            "type": "Element",
            "required": True,
        }
    )
    quantity_qualifier_coded_other: Optional[
        QuantityQualifierCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "QuantityQualifierCodedOther",
            "type": "Element",
        },
    )
    validity_dates: Optional[ValidityDates] = field(
        default=None,
        metadata={
            "name": "ValidityDates",
            "type": "Element",
        },
    )
    schedule_party: ScheduleParty = field(
        metadata={
            "name": "ScheduleParty",
            "type": "Element",
            "required": True,
        }
    )
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    planning_schedule_header_note: Optional[
        PlanningScheduleHeaderNote
    ] = field(
        default=None,
        metadata={
            "name": "PlanningScheduleHeaderNote",
            "type": "Element",
        },
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PlanningScheduleSummary:
    total_number_of_line_items: TotalNumberOfLineItems = field(
        metadata={
            "name": "TotalNumberOfLineItems",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ScheduleDetail:
    commitment_level_coded: CommitmentLevelCoded = field(
        metadata={
            "name": "CommitmentLevelCoded",
            "type": "Element",
            "required": True,
        }
    )
    commitment_level_coded_other: Optional[CommitmentLevelCodedOther] = field(
        default=None,
        metadata={
            "name": "CommitmentLevelCodedOther",
            "type": "Element",
        },
    )
    schedule_dates: ScheduleDates = field(
        metadata={
            "name": "ScheduleDates",
            "type": "Element",
            "required": True,
        }
    )
    schedule_quantities: ScheduleQuantities = field(
        metadata={
            "name": "ScheduleQuantities",
            "type": "Element",
            "required": True,
        }
    )
    item_resource_authorization: Optional[ItemResourceAuthorization] = field(
        default=None,
        metadata={
            "name": "ItemResourceAuthorization",
            "type": "Element",
        },
    )
    schedule_note: Optional[ScheduleNote] = field(
        default=None,
        metadata={
            "name": "ScheduleNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ChangedPlanningScheduleHeader:
    planning_schedule_header: PlanningScheduleHeader = field(
        metadata={
            "name": "PlanningScheduleHeader",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfScheduleDetail:
    schedule_detail: List[ScheduleDetail] = field(
        default_factory=list,
        metadata={
            "name": "ScheduleDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class OriginalPlanningScheduleHeader:
    planning_schedule_header: PlanningScheduleHeader = field(
        metadata={
            "name": "PlanningScheduleHeader",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PlanningScheduleResponseSummary:
    planning_schedule_summary: PlanningScheduleSummary = field(
        metadata={
            "name": "PlanningScheduleSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LocationPlanningItemDetail:
    base_planning_detail: BasePlanningDetail = field(
        metadata={
            "name": "BasePlanningDetail",
            "type": "Element",
            "required": True,
        }
    )
    list_of_schedule_detail: ListOfScheduleDetail = field(
        metadata={
            "name": "ListOfScheduleDetail",
            "type": "Element",
            "required": True,
        }
    )
    line_item_note: Optional[LineItemNote] = field(
        default=None,
        metadata={
            "name": "LineItemNote",
            "type": "Element",
        },
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class LocationSchedule:
    location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
        },
    )
    list_of_contact: Optional[ListOfContact] = field(
        default=None,
        metadata={
            "name": "ListOfContact",
            "type": "Element",
        },
    )
    list_of_schedule_detail: ListOfScheduleDetail = field(
        metadata={
            "name": "ListOfScheduleDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PlanningScheduleResponseHeader:
    schedule_response_id: ScheduleResponseId = field(
        metadata={
            "name": "ScheduleResponseID",
            "type": "Element",
            "required": True,
        }
    )
    schedule_response_issue_date: ScheduleResponseIssueDate = field(
        metadata={
            "name": "ScheduleResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    schedule_reference: ScheduleReference = field(
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
        },
    )
    buyer_party: BuyerParty = field(
        metadata={
            "name": "BuyerParty",
            "type": "Element",
            "required": True,
        }
    )
    seller_party: SellerParty = field(
        metadata={
            "name": "SellerParty",
            "type": "Element",
            "required": True,
        }
    )
    purpose: Purpose = field(
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )
    response_type: ResponseType = field(
        metadata={
            "name": "ResponseType",
            "type": "Element",
            "required": True,
        }
    )
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    original_planning_schedule_header: Optional[
        OriginalPlanningScheduleHeader
    ] = field(
        default=None,
        metadata={
            "name": "OriginalPlanningScheduleHeader",
            "type": "Element",
        },
    )
    changed_planning_schedule_header: Optional[
        ChangedPlanningScheduleHeader
    ] = field(
        default=None,
        metadata={
            "name": "ChangedPlanningScheduleHeader",
            "type": "Element",
        },
    )
    planning_schedule_response_header_note: Optional[
        PlanningScheduleResponseHeaderNote
    ] = field(
        default=None,
        metadata={
            "name": "PlanningScheduleResponseHeaderNote",
            "type": "Element",
        },
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfLocationPlanningItemDetail:
    location_planning_item_detail: List[LocationPlanningItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "LocationPlanningItemDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfLocationSchedule:
    location_schedule: List[LocationSchedule] = field(
        default_factory=list,
        metadata={
            "name": "LocationSchedule",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class LocationGroupedPlanningDetail:
    location: Location = field(
        metadata={
            "name": "Location",
            "type": "Element",
            "required": True,
        }
    )
    list_of_contact: Optional[ListOfContact] = field(
        default=None,
        metadata={
            "name": "ListOfContact",
            "type": "Element",
        },
    )
    list_of_location_planning_item_detail: ListOfLocationPlanningItemDetail = (
        field(
            metadata={
                "name": "ListOfLocationPlanningItemDetail",
                "type": "Element",
                "required": True,
            }
        )
    )


@dataclass(kw_only=True)
class MaterialGroupedPlanningDetail:
    base_planning_detail: BasePlanningDetail = field(
        metadata={
            "name": "BasePlanningDetail",
            "type": "Element",
            "required": True,
        }
    )
    list_of_location_schedule: ListOfLocationSchedule = field(
        metadata={
            "name": "ListOfLocationSchedule",
            "type": "Element",
            "required": True,
        }
    )
    line_item_note: Optional[LineItemNote] = field(
        default=None,
        metadata={
            "name": "LineItemNote",
            "type": "Element",
        },
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ChangedLocationGroupedPlanningDetail:
    location_grouped_planning_detail: LocationGroupedPlanningDetail = field(
        metadata={
            "name": "LocationGroupedPlanningDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ChangedMaterialGroupedPlanningDetail:
    material_grouped_planning_detail: MaterialGroupedPlanningDetail = field(
        metadata={
            "name": "MaterialGroupedPlanningDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OriginalLocationGroupedPlanningDetail:
    location_grouped_planning_detail: LocationGroupedPlanningDetail = field(
        metadata={
            "name": "LocationGroupedPlanningDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OriginalMaterialGroupedPlanningDetail:
    material_grouped_planning_detail: MaterialGroupedPlanningDetail = field(
        metadata={
            "name": "MaterialGroupedPlanningDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LocationGroupedPlanningResponse:
    detail_response_coded: DetailResponseCoded = field(
        metadata={
            "name": "DetailResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    detail_response_coded_other: Optional[DetailResponseCodedOther] = field(
        default=None,
        metadata={
            "name": "DetailResponseCodedOther",
            "type": "Element",
        },
    )
    original_location_grouped_planning_detail: Optional[
        OriginalLocationGroupedPlanningDetail
    ] = field(
        default=None,
        metadata={
            "name": "OriginalLocationGroupedPlanningDetail",
            "type": "Element",
        },
    )
    changed_location_grouped_planning_detail: Optional[
        ChangedLocationGroupedPlanningDetail
    ] = field(
        default=None,
        metadata={
            "name": "ChangedLocationGroupedPlanningDetail",
            "type": "Element",
        },
    )
    line_item_note: Optional[LineItemNote] = field(
        default=None,
        metadata={
            "name": "LineItemNote",
            "type": "Element",
        },
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class MaterialGroupedPlanningResponse:
    detail_response_coded: DetailResponseCoded = field(
        metadata={
            "name": "DetailResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    detail_response_coded_other: Optional[DetailResponseCodedOther] = field(
        default=None,
        metadata={
            "name": "DetailResponseCodedOther",
            "type": "Element",
        },
    )
    original_material_grouped_planning_detail: Optional[
        OriginalMaterialGroupedPlanningDetail
    ] = field(
        default=None,
        metadata={
            "name": "OriginalMaterialGroupedPlanningDetail",
            "type": "Element",
        },
    )
    changed_material_grouped_planning_detail: Optional[
        ChangedMaterialGroupedPlanningDetail
    ] = field(
        default=None,
        metadata={
            "name": "ChangedMaterialGroupedPlanningDetail",
            "type": "Element",
        },
    )
    line_item_note: Optional[LineItemNote] = field(
        default=None,
        metadata={
            "name": "LineItemNote",
            "type": "Element",
        },
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfLocationGroupedPlanningResponse:
    location_grouped_planning_response: List[
        LocationGroupedPlanningResponse
    ] = field(
        default_factory=list,
        metadata={
            "name": "LocationGroupedPlanningResponse",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfMaterialGroupedPlanningResponse:
    material_grouped_planning_response: List[
        MaterialGroupedPlanningResponse
    ] = field(
        default_factory=list,
        metadata={
            "name": "MaterialGroupedPlanningResponse",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class PlanningScheduleResponse:
    planning_schedule_response_header: PlanningScheduleResponseHeader = field(
        metadata={
            "name": "PlanningScheduleResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_location_grouped_planning_response: Optional[
        ListOfLocationGroupedPlanningResponse
    ] = field(
        default=None,
        metadata={
            "name": "ListOfLocationGroupedPlanningResponse",
            "type": "Element",
        },
    )
    list_of_material_grouped_planning_response: Optional[
        ListOfMaterialGroupedPlanningResponse
    ] = field(
        default=None,
        metadata={
            "name": "ListOfMaterialGroupedPlanningResponse",
            "type": "Element",
        },
    )
    planning_schedule_response_summary: Optional[
        PlanningScheduleResponseSummary
    ] = field(
        default=None,
        metadata={
            "name": "PlanningScheduleResponseSummary",
            "type": "Element",
        },
    )
