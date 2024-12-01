from dataclasses import dataclass, field
from typing import Any, Union

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from sdmx_ml.models.structured_text import StructuredText
from sdmx_ml.models.text import Text
from sdmx_ml.models.value_type import ValueType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class ObservationalTimePeriodValueType(ValueType):
    """
    ObservationalTimePeriodValueType is a refinement of SimpleValueType limiting
    the content to be an observational time period.
    """

    content: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    value: Union[XmlPeriod, XmlDate, XmlDateTime, str] = field(
        default="",
        metadata={
            "pattern": r".{5}A1.*",
        },
    )
