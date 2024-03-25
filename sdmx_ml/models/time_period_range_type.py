from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class TimePeriodRangeType:
    """
    TimePeriodRangeType defines a time period, and indicates whether it is
    inclusive in a range.

    :ivar value:
    :ivar is_inclusive: The isInclusive attribute, when true, indicates
        that the time period specified is included in the range.
    """

    value: str = field(
        default="",
        metadata={
            "pattern": r".{5}A1.*",
        },
    )
    is_inclusive: bool = field(
        default=True,
        metadata={
            "name": "isInclusive",
            "type": "Attribute",
        },
    )
