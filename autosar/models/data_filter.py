from dataclasses import dataclass, field
from typing import Optional

from .data_filter_type_enum import DataFilterTypeEnum
from .positive_integer import PositiveInteger
from .unlimited_integer import UnlimitedInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DataFilter:
    """
    Base class for data filters.

    The type of the filter is specified in attribute dataFilterType. Some
    of the filter types require additional arguments which are specified as
    attributes of this class.

    :ivar data_filter_type: This attribute specifies the type of the
        filter.
    :ivar mask: Mask for old and new value.
    :ivar max: Value to specify the upper boundary
    :ivar min: Value to specify the lower boundary
    :ivar offset: Specifies the initial number of messages to occur
        before the first message is passed
    :ivar period: Specifies number of messages to occur before the
        message is passed again
    :ivar x: Value to compare with
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    """

    class Meta:
        name = "DATA-FILTER"

    data_filter_type: Optional[DataFilterTypeEnum] = field(
        default=None,
        metadata={
            "name": "DATA-FILTER-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mask: Optional[UnlimitedInteger] = field(
        default=None,
        metadata={
            "name": "MASK",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max: Optional[UnlimitedInteger] = field(
        default=None,
        metadata={
            "name": "MAX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    min: Optional[UnlimitedInteger] = field(
        default=None,
        metadata={
            "name": "MIN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    offset: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "OFFSET",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    period: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PERIOD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    x: Optional[UnlimitedInteger] = field(
        default=None,
        metadata={
            "name": "X",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
