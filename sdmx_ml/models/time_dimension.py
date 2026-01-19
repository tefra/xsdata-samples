from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.time_dimension_type import TimeDimensionType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class TimeDimension(TimeDimensionType):
    """
    TimeDimension is a special dimension which designates the period in
    time in which the data identified by the full series key applies.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"
        )
