from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from sdmx_ml.models.annotable_type import AnnotableType
from sdmx_ml.models.mapped_value_type import MappedValueType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class SingleValueMappingType(AnnotableType):
    """
    SingleValueMappingType defines a mapping with a single source and
    optional target.

    :ivar source_value: There should be a source value for each source
        represention (e.g. codelist, data type). Source values can be
        pattern matched by using regular expression or substrings using
        start/end indexes.
    :ivar target_value: The target value(s) is always an absolute
        string. However, if source value is a regular expression, the
        target value can output the capture group from the source.
    :ivar valid_from:
    :ivar valid_to:
    """

    source_value: MappedValueType | None = field(
        default=None,
        metadata={
            "name": "SourceValue",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        },
    )
    target_value: str | None = field(
        default=None,
        metadata={
            "name": "TargetValue",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    valid_from: XmlDate | None = field(
        default=None,
        metadata={
            "name": "validFrom",
            "type": "Attribute",
        },
    )
    valid_to: XmlDate | None = field(
        default=None,
        metadata={
            "name": "validTo",
            "type": "Attribute",
        },
    )
