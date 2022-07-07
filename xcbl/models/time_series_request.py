from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import UnitOfMeasurement
from xcbl.models.time_series_response import (
    KeyFigureInformation,
    ListOfCharacteristicCombinations,
    TimeSeriesHeader,
    TimeSeriesSummary,
)


@dataclass
class KeyFigureData:
    key_figure_purpose_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyFigurePurposeCoded",
            "type": "Element",
        }
    )
    key_figure_purpose_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyFigurePurposeCodedOther",
            "type": "Element",
        }
    )
    characteristic_combination_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharacteristicCombinationID",
            "type": "Element",
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
    key_figure_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyFigureNotes",
            "type": "Element",
        }
    )


@dataclass
class TimeSeriesRequestHeader:
    time_series_header: Optional[TimeSeriesHeader] = field(
        default=None,
        metadata={
            "name": "TimeSeriesHeader",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TimeSeriesRequestSummary:
    time_series_summary: Optional[TimeSeriesSummary] = field(
        default=None,
        metadata={
            "name": "TimeSeriesSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfKeyFigureData:
    key_figure_data: List[KeyFigureData] = field(
        default_factory=list,
        metadata={
            "name": "KeyFigureData",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TimeSeriesRequestDetail:
    list_of_characteristic_combinations: Optional[ListOfCharacteristicCombinations] = field(
        default=None,
        metadata={
            "name": "ListOfCharacteristicCombinations",
            "type": "Element",
        }
    )
    list_of_key_figure_data: Optional[ListOfKeyFigureData] = field(
        default=None,
        metadata={
            "name": "ListOfKeyFigureData",
            "type": "Element",
        }
    )


@dataclass
class TimeSeriesRequest:
    time_series_request_header: Optional[TimeSeriesRequestHeader] = field(
        default=None,
        metadata={
            "name": "TimeSeriesRequestHeader",
            "type": "Element",
            "required": True,
        }
    )
    time_series_request_detail: Optional[TimeSeriesRequestDetail] = field(
        default=None,
        metadata={
            "name": "TimeSeriesRequestDetail",
            "type": "Element",
            "required": True,
        }
    )
    time_series_request_summary: Optional[TimeSeriesRequestSummary] = field(
        default=None,
        metadata={
            "name": "TimeSeriesRequestSummary",
            "type": "Element",
            "required": True,
        }
    )
