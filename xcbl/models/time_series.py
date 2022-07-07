from dataclasses import dataclass, field
from typing import Optional
from xcbl.models.time_series_response import (
    ListOfCharacteristicCombinations,
    ListOfTimeSeriesKeyFigureData,
    TimeSeriesHeader,
    TimeSeriesSummary,
)


@dataclass
class TimeSeriesDetail:
    list_of_characteristic_combinations: Optional[ListOfCharacteristicCombinations] = field(
        default=None,
        metadata={
            "name": "ListOfCharacteristicCombinations",
            "type": "Element",
        }
    )
    list_of_time_series_key_figure_data: Optional[ListOfTimeSeriesKeyFigureData] = field(
        default=None,
        metadata={
            "name": "ListOfTimeSeriesKeyFigureData",
            "type": "Element",
        }
    )


@dataclass
class TimeSeries:
    time_series_header: Optional[TimeSeriesHeader] = field(
        default=None,
        metadata={
            "name": "TimeSeriesHeader",
            "type": "Element",
            "required": True,
        }
    )
    time_series_detail: Optional[TimeSeriesDetail] = field(
        default=None,
        metadata={
            "name": "TimeSeriesDetail",
            "type": "Element",
            "required": True,
        }
    )
    time_series_summary: Optional[TimeSeriesSummary] = field(
        default=None,
        metadata={
            "name": "TimeSeriesSummary",
            "type": "Element",
            "required": True,
        }
    )
