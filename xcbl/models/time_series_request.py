from dataclasses import dataclass, field
from typing import Optional

from xcbl.models.time_series_response import (
    CharacteristicCombinationId,
    KeyFigureInformation,
    ListOfCharacteristicCombinations,
    TimeSeriesHeader,
    TimeSeriesSummary,
    UnitOfMeasurement,
)


@dataclass(kw_only=True)
class KeyFigureNotes:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class KeyFigurePurposeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class KeyFigurePurposeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class KeyFigureData:
    key_figure_purpose_coded: KeyFigurePurposeCoded | None = field(
        default=None,
        metadata={
            "name": "KeyFigurePurposeCoded",
            "type": "Element",
        },
    )
    key_figure_purpose_coded_other: KeyFigurePurposeCodedOther | None = (
        field(
            default=None,
            metadata={
                "name": "KeyFigurePurposeCodedOther",
                "type": "Element",
            },
        )
    )
    characteristic_combination_id: CharacteristicCombinationId | None = (
        field(
            default=None,
            metadata={
                "name": "CharacteristicCombinationID",
                "type": "Element",
            },
        )
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
    key_figure_notes: KeyFigureNotes | None = field(
        default=None,
        metadata={
            "name": "KeyFigureNotes",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TimeSeriesRequestHeader:
    time_series_header: TimeSeriesHeader = field(
        metadata={
            "name": "TimeSeriesHeader",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSeriesRequestSummary:
    time_series_summary: TimeSeriesSummary = field(
        metadata={
            "name": "TimeSeriesSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfKeyFigureData:
    key_figure_data: list[KeyFigureData] = field(
        default_factory=list,
        metadata={
            "name": "KeyFigureData",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class TimeSeriesRequestDetail:
    list_of_characteristic_combinations: ListOfCharacteristicCombinations | None = field(
        default=None,
        metadata={
            "name": "ListOfCharacteristicCombinations",
            "type": "Element",
        },
    )
    list_of_key_figure_data: ListOfKeyFigureData | None = field(
        default=None,
        metadata={
            "name": "ListOfKeyFigureData",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TimeSeriesRequest:
    time_series_request_header: TimeSeriesRequestHeader = field(
        metadata={
            "name": "TimeSeriesRequestHeader",
            "type": "Element",
            "required": True,
        }
    )
    time_series_request_detail: TimeSeriesRequestDetail = field(
        metadata={
            "name": "TimeSeriesRequestDetail",
            "type": "Element",
            "required": True,
        }
    )
    time_series_request_summary: TimeSeriesRequestSummary = field(
        metadata={
            "name": "TimeSeriesRequestSummary",
            "type": "Element",
            "required": True,
        }
    )
