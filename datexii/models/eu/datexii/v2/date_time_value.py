from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from datexii.models.eu.datexii.v2.data_value import DataValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class DateTimeValue(DataValue):
    """
    A measured or calculated value of an instance in time.

    :ivar date_time: A time stamp defining an instance in time.
    :ivar date_time_value_extension:
    """

    date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "dateTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    date_time_value_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "dateTimeValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
