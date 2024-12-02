from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from sdmx_ml.models.annotable_type import AnnotableType
from sdmx_ml.models.mapped_value_type import MappedValueType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ValueMappingType(AnnotableType):
    """
    ValueMappingType defines a mapping of multiple sources to multiple targets.

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

    source_value: tuple[MappedValueType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SourceValue",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
    target_value: tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TargetValue",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    valid_from: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "validFrom",
            "type": "Attribute",
        },
    )
    valid_to: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "validTo",
            "type": "Attribute",
        },
    )
