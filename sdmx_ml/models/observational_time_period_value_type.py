from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from sdmx_ml.models.value_type import ValueType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/common"


@dataclass(frozen=True, kw_only=True)
class ObservationalTimePeriodValueType(ValueType):
    """
    ObservationalTimePeriodValueType is a refinement of SimpleValueType
    limiting the content to be an observational time period.
    """

    content: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    value: XmlPeriod | XmlDate | XmlDateTime | str = field(
        default="",
        metadata={
            "pattern": r".{5}A1.*",
        },
    )
