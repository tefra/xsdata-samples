from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from sdmx_ml.models.simple_component_value_type import SimpleComponentValueType
from sdmx_ml.models.time_range_value_type import TimeRangeValueType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class MemberSelectionType:
    """
    MemberSelectionType is an abstract base type which is used to provide a
    set of values for a referenced component.

    Implementations of this type will be based on a particular component
    type and refine the allowed values to reflect the types of values that
    are possible for that type of component.

    :ivar value_or_time_range:
    :ivar id: The id attribute provides the identifier for the component
        for which values are being provided. This base type allows for a
        nested identifier to be provided, for the purpose of referencing
        a nested component (i.e. a metadata attribute). However,
        specific implementations will restrict this representation to
        only allow single level identifiers where appropriate.
    :ivar include: The include attribute indicates whether the values
        provided for the referenced component are to be included or
        excluded from the region in which they are defined.
    :ivar remove_prefix: The removePrefix attribute indicates whether
        codes should keep or not the prefix, as defined in the extension
        of codelist.
    :ivar valid_from:
    :ivar valid_to:
    """

    value_or_time_range: tuple[
        SimpleComponentValueType | TimeRangeValueType, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Value",
                    "type": SimpleComponentValueType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "TimeRange",
                    "type": TimeRangeValueType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_\-]*(\.[A-Za-z][A-Za-z0-9_\-]*)*",
        }
    )
    include: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    remove_prefix: None | bool = field(
        default=None,
        metadata={
            "name": "removePrefix",
            "type": "Attribute",
        },
    )
    valid_from: None | XmlPeriod | XmlDate | XmlDateTime | str = field(
        default=None,
        metadata={
            "name": "validFrom",
            "type": "Attribute",
            "pattern": r".{5}A1.*",
        },
    )
    valid_to: None | XmlPeriod | XmlDate | XmlDateTime | str = field(
        default=None,
        metadata={
            "name": "validTo",
            "type": "Attribute",
            "pattern": r".{5}A1.*",
        },
    )
