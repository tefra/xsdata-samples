from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Identifier,
    Language,
    ListOfDimension,
    Location,
    Party,
    Reference,
    UnitOfMeasurement,
    ValidityDates,
)
from xcbl.models.order_request import ListOfPartyCoded


@dataclass(kw_only=True)
class KeyFigure:
    key_figure_id: str = field(
        metadata={
            "name": "KeyFigureID",
            "type": "Element",
            "required": True,
        }
    )
    key_figure_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyFigureName",
            "type": "Element",
        }
    )
    key_figure_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyFigureDescription",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class OtherCharacteristicAttribute:
    characteristic_attribute: "CharacteristicAttribute" = field(
        metadata={
            "name": "CharacteristicAttribute",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourceTargetId:
    class Meta:
        name = "SourceTargetID"

    source_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourceID",
            "type": "Element",
        }
    )
    target_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TargetID",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class TimeSeriesSummary:
    total_time_series_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalTimeSeriesData",
            "type": "Element",
        }
    )
    total_characteristic_combinations: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalCharacteristicCombinations",
            "type": "Element",
        }
    )
    total_key_figures: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalKeyFigures",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class CharacteristicAttributeName:
    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LocationAttributeName:
    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ProductAttributeName:
    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ReceiverParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourceKeyFigure:
    key_figure: KeyFigure = field(
        metadata={
            "name": "KeyFigure",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourceParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TargetKeyFigure:
    key_figure: KeyFigure = field(
        metadata={
            "name": "KeyFigure",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesBucket:
    validity_dates: ValidityDates = field(
        metadata={
            "name": "ValidityDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesId:
    class Meta:
        name = "TimeSeriesID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesPlanningData:
    source_target_id: SourceTargetId = field(
        metadata={
            "name": "SourceTargetID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesPlanningStep:
    source_target_id: SourceTargetId = field(
        metadata={
            "name": "SourceTargetID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesResponseId:
    class Meta:
        name = "TimeSeriesResponseID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesResponseSummary:
    time_series_summary: TimeSeriesSummary = field(
        metadata={
            "name": "TimeSeriesSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesSelection:
    source_target_id: SourceTargetId = field(
        metadata={
            "name": "SourceTargetID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesSystemType:
    source_target_id: SourceTargetId = field(
        metadata={
            "name": "SourceTargetID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesTimePeriod:
    validity_dates: ValidityDates = field(
        metadata={
            "name": "ValidityDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CharacteristicAttribute:
    characteristic_name: str = field(
        metadata={
            "name": "CharacteristicName",
            "type": "Element",
            "required": True,
        }
    )
    characteristic_attribute_id: str = field(
        metadata={
            "name": "CharacteristicAttributeID",
            "type": "Element",
            "required": True,
        }
    )
    characteristic_attribute_name: List[CharacteristicAttributeName] = field(
        default_factory=list,
        metadata={
            "name": "CharacteristicAttributeName",
            "type": "Element",
        }
    )
    characteristic_attribute_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharacteristicAttributeDescription",
            "type": "Element",
        }
    )
    list_of_dimension: Optional[ListOfDimension] = field(
        default=None,
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
        }
    )
    characteristic_attribute_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharacteristicAttributeNote",
            "type": "Element",
        }
    )
    other_characteristic_attribute: List[OtherCharacteristicAttribute] = field(
        default_factory=list,
        metadata={
            "name": "OtherCharacteristicAttribute",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class KeyFigureInformation:
    source_key_figure: Optional[SourceKeyFigure] = field(
        default=None,
        metadata={
            "name": "SourceKeyFigure",
            "type": "Element",
        }
    )
    target_key_figure: Optional[TargetKeyFigure] = field(
        default=None,
        metadata={
            "name": "TargetKeyFigure",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class TimeSeriesData:
    time_series_bucket: TimeSeriesBucket = field(
        metadata={
            "name": "TimeSeriesBucket",
            "type": "Element",
            "required": True,
        }
    )
    time_series_value: str = field(
        metadata={
            "name": "TimeSeriesValue",
            "type": "Element",
            "required": True,
        }
    )
    time_series_data_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeSeriesDataNote",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class TimeSeriesParty:
    source_party: Optional[SourceParty] = field(
        default=None,
        metadata={
            "name": "SourceParty",
            "type": "Element",
        }
    )
    receiver_party: Optional[ReceiverParty] = field(
        default=None,
        metadata={
            "name": "ReceiverParty",
            "type": "Element",
        }
    )
    list_of_party_coded: Optional[ListOfPartyCoded] = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class OtherLocationAttribute:
    characteristic_attribute: CharacteristicAttribute = field(
        metadata={
            "name": "CharacteristicAttribute",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OtherProductAttribute:
    characteristic_attribute: CharacteristicAttribute = field(
        metadata={
            "name": "CharacteristicAttribute",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourceCharacteristicsOther:
    characteristic_attribute: CharacteristicAttribute = field(
        metadata={
            "name": "CharacteristicAttribute",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TargetCharacteristicsOther:
    characteristic_attribute: CharacteristicAttribute = field(
        metadata={
            "name": "CharacteristicAttribute",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesHeader:
    time_series_issue_date: str = field(
        metadata={
            "name": "TimeSeriesIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    time_series_id: TimeSeriesId = field(
        metadata={
            "name": "TimeSeriesID",
            "type": "Element",
            "required": True,
        }
    )
    time_series_purpose_coded: str = field(
        metadata={
            "name": "TimeSeriesPurposeCoded",
            "type": "Element",
            "required": True,
        }
    )
    time_series_purpose_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeSeriesPurposeCodedOther",
            "type": "Element",
        }
    )
    time_series_time_period: Optional[TimeSeriesTimePeriod] = field(
        default=None,
        metadata={
            "name": "TimeSeriesTimePeriod",
            "type": "Element",
        }
    )
    time_series_system_type: Optional[TimeSeriesSystemType] = field(
        default=None,
        metadata={
            "name": "TimeSeriesSystemType",
            "type": "Element",
        }
    )
    time_series_planning_data: TimeSeriesPlanningData = field(
        metadata={
            "name": "TimeSeriesPlanningData",
            "type": "Element",
            "required": True,
        }
    )
    time_series_selection: Optional[TimeSeriesSelection] = field(
        default=None,
        metadata={
            "name": "TimeSeriesSelection",
            "type": "Element",
        }
    )
    time_series_planning_step: Optional[TimeSeriesPlanningStep] = field(
        default=None,
        metadata={
            "name": "TimeSeriesPlanningStep",
            "type": "Element",
        }
    )
    time_series_party: TimeSeriesParty = field(
        metadata={
            "name": "TimeSeriesParty",
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
    general_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralNotes",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class TimeSeriesKeyFigureData:
    time_series_key_figure_purpose_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeSeriesKeyFigurePurposeCoded",
            "type": "Element",
        }
    )
    time_series_key_figure_purpose_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeSeriesKeyFigurePurposeCodedOther",
            "type": "Element",
        }
    )
    time_series_key_figure_response_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeSeriesKeyFigureResponseCoded",
            "type": "Element",
        }
    )
    time_series_key_figure_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeSeriesKeyFigureResponseCodedOther",
            "type": "Element",
        }
    )
    characteristic_combination_id: str = field(
        metadata={
            "name": "CharacteristicCombinationID",
            "type": "Element",
            "required": True,
        }
    )
    key_figure_information: KeyFigureInformation = field(
        metadata={
            "name": "KeyFigureInformation",
            "type": "Element",
            "required": True,
        }
    )
    unit_of_measurement: UnitOfMeasurement = field(
        metadata={
            "name": "UnitOfMeasurement",
            "type": "Element",
            "required": True,
        }
    )
    time_series_data: List[TimeSeriesData] = field(
        default_factory=list,
        metadata={
            "name": "TimeSeriesData",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesResponseParty:
    time_series_party: TimeSeriesParty = field(
        metadata={
            "name": "TimeSeriesParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class BaseCharacteristicLocation:
    location_attribute_id: str = field(
        metadata={
            "name": "LocationAttributeID",
            "type": "Element",
            "required": True,
        }
    )
    location_attribute_name: List[LocationAttributeName] = field(
        default_factory=list,
        metadata={
            "name": "LocationAttributeName",
            "type": "Element",
        }
    )
    location_attribute_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocationAttributeDescription",
            "type": "Element",
        }
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
        }
    )
    location_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocationNotes",
            "type": "Element",
        }
    )
    other_location_attribute: Optional[OtherLocationAttribute] = field(
        default=None,
        metadata={
            "name": "OtherLocationAttribute",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class BaseCharacteristicProduct:
    product_attribute_id: str = field(
        metadata={
            "name": "ProductAttributeID",
            "type": "Element",
            "required": True,
        }
    )
    product_attribute_name: List[ProductAttributeName] = field(
        default_factory=list,
        metadata={
            "name": "ProductAttributeName",
            "type": "Element",
        }
    )
    product_attribute_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProductAttributeDescription",
            "type": "Element",
        }
    )
    list_of_dimension: Optional[ListOfDimension] = field(
        default=None,
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
        }
    )
    product_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProductNotes",
            "type": "Element",
        }
    )
    other_product_attribute: Optional[OtherProductAttribute] = field(
        default=None,
        metadata={
            "name": "OtherProductAttribute",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ChangedTimeSeriesHeader:
    time_series_header: TimeSeriesHeader = field(
        metadata={
            "name": "TimeSeriesHeader",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CharacteristicOther:
    source_characteristics_other: Optional[SourceCharacteristicsOther] = field(
        default=None,
        metadata={
            "name": "SourceCharacteristicsOther",
            "type": "Element",
        }
    )
    target_characteristics_other: Optional[TargetCharacteristicsOther] = field(
        default=None,
        metadata={
            "name": "TargetCharacteristicsOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfTimeSeriesKeyFigureData:
    time_series_key_figure_data: List[TimeSeriesKeyFigureData] = field(
        default_factory=list,
        metadata={
            "name": "TimeSeriesKeyFigureData",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfChangedTimeSeriesKeyFigureData:
    list_of_time_series_key_figure_data: ListOfTimeSeriesKeyFigureData = field(
        metadata={
            "name": "ListOfTimeSeriesKeyFigureData",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourceLocation:
    base_characteristic_location: BaseCharacteristicLocation = field(
        metadata={
            "name": "BaseCharacteristicLocation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourceProduct:
    base_characteristic_product: BaseCharacteristicProduct = field(
        metadata={
            "name": "BaseCharacteristicProduct",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourceProductGroup:
    base_characteristic_product: BaseCharacteristicProduct = field(
        metadata={
            "name": "BaseCharacteristicProduct",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TargetLocation:
    base_characteristic_location: BaseCharacteristicLocation = field(
        metadata={
            "name": "BaseCharacteristicLocation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TargetProduct:
    base_characteristic_product: BaseCharacteristicProduct = field(
        metadata={
            "name": "BaseCharacteristicProduct",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TargetProductGroup:
    base_characteristic_product: BaseCharacteristicProduct = field(
        metadata={
            "name": "BaseCharacteristicProduct",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesResponseHeader:
    time_series_response_issue_date: str = field(
        metadata={
            "name": "TimeSeriesResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    time_series_response_id: TimeSeriesResponseId = field(
        metadata={
            "name": "TimeSeriesResponseID",
            "type": "Element",
            "required": True,
        }
    )
    time_series_reference: TimeSeriesReference = field(
        metadata={
            "name": "TimeSeriesReference",
            "type": "Element",
            "required": True,
        }
    )
    time_series_planning_data: Optional[TimeSeriesPlanningData] = field(
        default=None,
        metadata={
            "name": "TimeSeriesPlanningData",
            "type": "Element",
        }
    )
    time_series_response_party: TimeSeriesResponseParty = field(
        metadata={
            "name": "TimeSeriesResponseParty",
            "type": "Element",
            "required": True,
        }
    )
    time_series_header_response_coded: str = field(
        metadata={
            "name": "TimeSeriesHeaderResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    time_series_header_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeSeriesHeaderResponseCodedOther",
            "type": "Element",
        }
    )
    changed_time_series_header: Optional[ChangedTimeSeriesHeader] = field(
        default=None,
        metadata={
            "name": "ChangedTimeSeriesHeader",
            "type": "Element",
        }
    )
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    general_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralNotes",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class CharacteristicLocation:
    source_location: Optional[SourceLocation] = field(
        default=None,
        metadata={
            "name": "SourceLocation",
            "type": "Element",
        }
    )
    target_location: Optional[TargetLocation] = field(
        default=None,
        metadata={
            "name": "TargetLocation",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class CharacteristicProduct:
    source_product: Optional[SourceProduct] = field(
        default=None,
        metadata={
            "name": "SourceProduct",
            "type": "Element",
        }
    )
    target_product: Optional[TargetProduct] = field(
        default=None,
        metadata={
            "name": "TargetProduct",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class CharacteristicProductGroup:
    source_product_group: Optional[SourceProductGroup] = field(
        default=None,
        metadata={
            "name": "SourceProductGroup",
            "type": "Element",
        }
    )
    target_product_group: Optional[TargetProductGroup] = field(
        default=None,
        metadata={
            "name": "TargetProductGroup",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class CharacteristicCombination:
    characteristic_combination_purpose_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharacteristicCombinationPurposeCoded",
            "type": "Element",
        }
    )
    characteristic_combination_purpose_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharacteristicCombinationPurposeCodedOther",
            "type": "Element",
        }
    )
    characteristic_combination_response_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharacteristicCombinationResponseCoded",
            "type": "Element",
        }
    )
    characteristic_combination_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharacteristicCombinationResponseCodedOther",
            "type": "Element",
        }
    )
    characteristic_combination_id: str = field(
        metadata={
            "name": "CharacteristicCombinationID",
            "type": "Element",
            "required": True,
        }
    )
    characteristic_product: Optional[CharacteristicProduct] = field(
        default=None,
        metadata={
            "name": "CharacteristicProduct",
            "type": "Element",
        }
    )
    characteristic_location: Optional[CharacteristicLocation] = field(
        default=None,
        metadata={
            "name": "CharacteristicLocation",
            "type": "Element",
        }
    )
    characteristic_product_group: Optional[CharacteristicProductGroup] = field(
        default=None,
        metadata={
            "name": "CharacteristicProductGroup",
            "type": "Element",
        }
    )
    characteristic_other: List[CharacteristicOther] = field(
        default_factory=list,
        metadata={
            "name": "CharacteristicOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfCharacteristicCombinations:
    characteristic_combination: List[CharacteristicCombination] = field(
        default_factory=list,
        metadata={
            "name": "CharacteristicCombination",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfChangedCharacteristicCombinations:
    list_of_characteristic_combinations: ListOfCharacteristicCombinations = field(
        metadata={
            "name": "ListOfCharacteristicCombinations",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesResponseDetail:
    time_series_detail_response_coded: str = field(
        metadata={
            "name": "TimeSeriesDetailResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    time_series_detail_response_coded_other: str = field(
        metadata={
            "name": "TimeSeriesDetailResponseCodedOther",
            "type": "Element",
            "required": True,
        }
    )
    list_of_changed_characteristic_combinations: Optional[ListOfChangedCharacteristicCombinations] = field(
        default=None,
        metadata={
            "name": "ListOfChangedCharacteristicCombinations",
            "type": "Element",
        }
    )
    list_of_changed_time_series_key_figure_data: Optional[ListOfChangedTimeSeriesKeyFigureData] = field(
        default=None,
        metadata={
            "name": "ListOfChangedTimeSeriesKeyFigureData",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class TimeSeriesResponse:
    time_series_response_header: TimeSeriesResponseHeader = field(
        metadata={
            "name": "TimeSeriesResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
    time_series_response_detail: TimeSeriesResponseDetail = field(
        metadata={
            "name": "TimeSeriesResponseDetail",
            "type": "Element",
            "required": True,
        }
    )
    time_series_response_summary: TimeSeriesResponseSummary = field(
        metadata={
            "name": "TimeSeriesResponseSummary",
            "type": "Element",
            "required": True,
        }
    )
