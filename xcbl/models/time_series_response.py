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


@dataclass
class KeyFigure:
    key_figure_id: Optional[str] = field(
        default=None,
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


@dataclass
class OtherCharacteristicAttribute:
    characteristic_attribute: Optional["CharacteristicAttribute"] = field(
        default=None,
        metadata={
            "name": "CharacteristicAttribute",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
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


@dataclass
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


@dataclass
class CharacteristicAttributeName:
    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LocationAttributeName:
    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ProductAttributeName:
    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ReceiverParty:
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourceKeyFigure:
    key_figure: Optional[KeyFigure] = field(
        default=None,
        metadata={
            "name": "KeyFigure",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourceParty:
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TargetKeyFigure:
    key_figure: Optional[KeyFigure] = field(
        default=None,
        metadata={
            "name": "KeyFigure",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TimeSeriesBucket:
    validity_dates: Optional[ValidityDates] = field(
        default=None,
        metadata={
            "name": "ValidityDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TimeSeriesId:
    class Meta:
        name = "TimeSeriesID"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TimeSeriesPlanningData:
    source_target_id: Optional[SourceTargetId] = field(
        default=None,
        metadata={
            "name": "SourceTargetID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TimeSeriesPlanningStep:
    source_target_id: Optional[SourceTargetId] = field(
        default=None,
        metadata={
            "name": "SourceTargetID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TimeSeriesReference:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TimeSeriesResponseId:
    class Meta:
        name = "TimeSeriesResponseID"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TimeSeriesResponseSummary:
    time_series_summary: Optional[TimeSeriesSummary] = field(
        default=None,
        metadata={
            "name": "TimeSeriesSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TimeSeriesSelection:
    source_target_id: Optional[SourceTargetId] = field(
        default=None,
        metadata={
            "name": "SourceTargetID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TimeSeriesSystemType:
    source_target_id: Optional[SourceTargetId] = field(
        default=None,
        metadata={
            "name": "SourceTargetID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TimeSeriesTimePeriod:
    validity_dates: Optional[ValidityDates] = field(
        default=None,
        metadata={
            "name": "ValidityDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class CharacteristicAttribute:
    characteristic_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharacteristicName",
            "type": "Element",
            "required": True,
        }
    )
    characteristic_attribute_id: Optional[str] = field(
        default=None,
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


@dataclass
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


@dataclass
class TimeSeriesData:
    time_series_bucket: Optional[TimeSeriesBucket] = field(
        default=None,
        metadata={
            "name": "TimeSeriesBucket",
            "type": "Element",
            "required": True,
        }
    )
    time_series_value: Optional[str] = field(
        default=None,
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


@dataclass
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


@dataclass
class OtherLocationAttribute:
    characteristic_attribute: Optional[CharacteristicAttribute] = field(
        default=None,
        metadata={
            "name": "CharacteristicAttribute",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OtherProductAttribute:
    characteristic_attribute: Optional[CharacteristicAttribute] = field(
        default=None,
        metadata={
            "name": "CharacteristicAttribute",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourceCharacteristicsOther:
    characteristic_attribute: Optional[CharacteristicAttribute] = field(
        default=None,
        metadata={
            "name": "CharacteristicAttribute",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TargetCharacteristicsOther:
    characteristic_attribute: Optional[CharacteristicAttribute] = field(
        default=None,
        metadata={
            "name": "CharacteristicAttribute",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TimeSeriesHeader:
    time_series_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeSeriesIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    time_series_id: Optional[TimeSeriesId] = field(
        default=None,
        metadata={
            "name": "TimeSeriesID",
            "type": "Element",
            "required": True,
        }
    )
    time_series_purpose_coded: Optional[str] = field(
        default=None,
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
    time_series_planning_data: Optional[TimeSeriesPlanningData] = field(
        default=None,
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
    time_series_party: Optional[TimeSeriesParty] = field(
        default=None,
        metadata={
            "name": "TimeSeriesParty",
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
    general_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralNotes",
            "type": "Element",
        }
    )


@dataclass
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
    characteristic_combination_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharacteristicCombinationID",
            "type": "Element",
            "required": True,
        }
    )
    key_figure_information: Optional[KeyFigureInformation] = field(
        default=None,
        metadata={
            "name": "KeyFigureInformation",
            "type": "Element",
            "required": True,
        }
    )
    unit_of_measurement: Optional[UnitOfMeasurement] = field(
        default=None,
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


@dataclass
class TimeSeriesResponseParty:
    time_series_party: Optional[TimeSeriesParty] = field(
        default=None,
        metadata={
            "name": "TimeSeriesParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class BaseCharacteristicLocation:
    location_attribute_id: Optional[str] = field(
        default=None,
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


@dataclass
class BaseCharacteristicProduct:
    product_attribute_id: Optional[str] = field(
        default=None,
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


@dataclass
class ChangedTimeSeriesHeader:
    time_series_header: Optional[TimeSeriesHeader] = field(
        default=None,
        metadata={
            "name": "TimeSeriesHeader",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
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


@dataclass
class ListOfTimeSeriesKeyFigureData:
    time_series_key_figure_data: List[TimeSeriesKeyFigureData] = field(
        default_factory=list,
        metadata={
            "name": "TimeSeriesKeyFigureData",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfChangedTimeSeriesKeyFigureData:
    list_of_time_series_key_figure_data: Optional[ListOfTimeSeriesKeyFigureData] = field(
        default=None,
        metadata={
            "name": "ListOfTimeSeriesKeyFigureData",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourceLocation:
    base_characteristic_location: Optional[BaseCharacteristicLocation] = field(
        default=None,
        metadata={
            "name": "BaseCharacteristicLocation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourceProduct:
    base_characteristic_product: Optional[BaseCharacteristicProduct] = field(
        default=None,
        metadata={
            "name": "BaseCharacteristicProduct",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourceProductGroup:
    base_characteristic_product: Optional[BaseCharacteristicProduct] = field(
        default=None,
        metadata={
            "name": "BaseCharacteristicProduct",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TargetLocation:
    base_characteristic_location: Optional[BaseCharacteristicLocation] = field(
        default=None,
        metadata={
            "name": "BaseCharacteristicLocation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TargetProduct:
    base_characteristic_product: Optional[BaseCharacteristicProduct] = field(
        default=None,
        metadata={
            "name": "BaseCharacteristicProduct",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TargetProductGroup:
    base_characteristic_product: Optional[BaseCharacteristicProduct] = field(
        default=None,
        metadata={
            "name": "BaseCharacteristicProduct",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TimeSeriesResponseHeader:
    time_series_response_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeSeriesResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    time_series_response_id: Optional[TimeSeriesResponseId] = field(
        default=None,
        metadata={
            "name": "TimeSeriesResponseID",
            "type": "Element",
            "required": True,
        }
    )
    time_series_reference: Optional[TimeSeriesReference] = field(
        default=None,
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
    time_series_response_party: Optional[TimeSeriesResponseParty] = field(
        default=None,
        metadata={
            "name": "TimeSeriesResponseParty",
            "type": "Element",
            "required": True,
        }
    )
    time_series_header_response_coded: Optional[str] = field(
        default=None,
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
    language: Optional[Language] = field(
        default=None,
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


@dataclass
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


@dataclass
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


@dataclass
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


@dataclass
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
    characteristic_combination_id: Optional[str] = field(
        default=None,
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


@dataclass
class ListOfCharacteristicCombinations:
    characteristic_combination: List[CharacteristicCombination] = field(
        default_factory=list,
        metadata={
            "name": "CharacteristicCombination",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfChangedCharacteristicCombinations:
    list_of_characteristic_combinations: Optional[ListOfCharacteristicCombinations] = field(
        default=None,
        metadata={
            "name": "ListOfCharacteristicCombinations",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TimeSeriesResponseDetail:
    time_series_detail_response_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeSeriesDetailResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    time_series_detail_response_coded_other: Optional[str] = field(
        default=None,
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


@dataclass
class TimeSeriesResponse:
    time_series_response_header: Optional[TimeSeriesResponseHeader] = field(
        default=None,
        metadata={
            "name": "TimeSeriesResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
    time_series_response_detail: Optional[TimeSeriesResponseDetail] = field(
        default=None,
        metadata={
            "name": "TimeSeriesResponseDetail",
            "type": "Element",
            "required": True,
        }
    )
    time_series_response_summary: Optional[TimeSeriesResponseSummary] = field(
        default=None,
        metadata={
            "name": "TimeSeriesResponseSummary",
            "type": "Element",
            "required": True,
        }
    )
