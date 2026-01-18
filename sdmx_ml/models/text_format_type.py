from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration, XmlPeriod

from sdmx_ml.models.data_type import DataType
from sdmx_ml.models.sentinel_value_type import SentinelValueType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class TextFormatType:
    """
    TextFormatType defines the information for describing a full range of
    text formats and may place restrictions on the values of the other
    attributes, referred to as "facets".

    :ivar sentinel_value: SentinelValue defines a value that has a
        special meaning within the text format representation of a
        component.
    :ivar text_type: The textType attribute provides a description of
        the datatype. If it is not specified, any valid characters may
        be included in the text field (it corresponds to the xs:string
        datatype of W3C XML Schema) within the constraints of the
        facets.
    :ivar is_sequence: The isSequence attribute indicates whether the
        values are intended to be ordered, and it may work in
        combination with the interval, startValue, and endValue
        attributes or the timeInterval, startTime, and endTime,
        attributes. If this attribute holds a value of true, a start
        value or time and a numeric or time interval must supplied. If
        an end value is not given, then the sequence continues
        indefinitely.
    :ivar interval: The interval attribute specifies the permitted
        interval (increment) in a sequence. In order for this to be
        used, the isSequence attribute must have a value of true.
    :ivar start_value: The startValue attribute is used in conjunction
        with the isSequence and interval attributes (which must be set
        in order to use this attribute). This attribute is used for a
        numeric sequence, and indicates the starting  point of the
        sequence. This value is mandatory for a numeric sequence to be
        expressed.
    :ivar end_value: The endValue attribute is used in conjunction with
        the isSequence and interval attributes (which must be set in
        order to use this attribute). This attribute is used for a
        numeric sequence, and indicates that ending point (if any) of
        the sequence.
    :ivar time_interval: The timeInterval attribute indicates the
        permitted duration in a time sequence. In order for this to be
        used, the isSequence attribute must have a value of true.
    :ivar start_time: The startTime attribute is used in conjunction
        with the isSequence and timeInterval attributes (which must be
        set in order to use this attribute). This attribute is used for
        a time sequence, and indicates the start time of the sequence.
        This value is mandatory for a time sequence to be expressed.
    :ivar end_time: The endTime attribute is used in conjunction with
        the isSequence and timeInterval attributes (which must be set in
        order to use this attribute). This attribute is used for a time
        sequence, and indicates that ending point (if any) of the
        sequence.
    :ivar min_length: The minLength attribute specifies the minimum and
        length of the value in characters.
    :ivar max_length: The maxLength attribute specifies the maximum
        length of the value in characters.
    :ivar min_value: The minValue attribute is used for inclusive and
        exclusive ranges, indicating what the lower bound of the range
        is. If this is used with an inclusive range, a valid value will
        be greater than or equal to the value specified here. If the
        inclusive and exclusive data type is not specified (e.g. this
        facet is used with an integer data type), the value is assumed
        to be inclusive.
    :ivar max_value: The maxValue attribute is used for inclusive and
        exclusive ranges, indicating what the upper bound of the range
        is. If this is used with an inclusive range, a valid value will
        be less than or equal to the value specified here. If the
        inclusive and exclusive data type is not specified (e.g. this
        facet is used with an integer data type), the value is assumed
        to be inclusive.
    :ivar decimals: The decimals attribute indicates the number of
        characters allowed after the decimal separator.
    :ivar pattern: The pattern attribute holds any regular expression
        permitted in the similar facet in W3C XML Schema.
    :ivar is_multi_lingual: The isMultiLingual attribute indicates for a
        text format of type "string", whether the value should allow for
        multiple values in different languages.
    """

    sentinel_value: tuple[SentinelValueType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SentinelValue",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    text_type: DataType = field(
        default=DataType.STRING,
        metadata={
            "name": "textType",
            "type": "Attribute",
        },
    )
    is_sequence: bool | None = field(
        default=None,
        metadata={
            "name": "isSequence",
            "type": "Attribute",
        },
    )
    interval: Decimal | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    start_value: Decimal | None = field(
        default=None,
        metadata={
            "name": "startValue",
            "type": "Attribute",
        },
    )
    end_value: Decimal | None = field(
        default=None,
        metadata={
            "name": "endValue",
            "type": "Attribute",
        },
    )
    time_interval: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "timeInterval",
            "type": "Attribute",
        },
    )
    start_time: XmlPeriod | XmlDate | XmlDateTime | str | None = field(
        default=None,
        metadata={
            "name": "startTime",
            "type": "Attribute",
            "pattern": r".{5}A1.*",
        },
    )
    end_time: XmlPeriod | XmlDate | XmlDateTime | str | None = field(
        default=None,
        metadata={
            "name": "endTime",
            "type": "Attribute",
            "pattern": r".{5}A1.*",
        },
    )
    min_length: int | None = field(
        default=None,
        metadata={
            "name": "minLength",
            "type": "Attribute",
        },
    )
    max_length: int | None = field(
        default=None,
        metadata={
            "name": "maxLength",
            "type": "Attribute",
        },
    )
    min_value: Decimal | None = field(
        default=None,
        metadata={
            "name": "minValue",
            "type": "Attribute",
        },
    )
    max_value: Decimal | None = field(
        default=None,
        metadata={
            "name": "maxValue",
            "type": "Attribute",
        },
    )
    decimals: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    pattern: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    is_multi_lingual: bool = field(
        default=True,
        metadata={
            "name": "isMultiLingual",
            "type": "Attribute",
        },
    )
