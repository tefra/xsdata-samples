from __future__ import annotations

from dataclasses import dataclass, field

from .positive_integer import PositiveInteger
from .text_value_specification import TextValueSpecification

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class MetaDataItem:
    """
    This meta-class represents a single meta-data item.

    :ivar length: This attribute determines the length of the
        MetaDataItem at run-time.
    :ivar meta_data_item_type: This aggregation contributes the
        specification of the concrete meta-data item type.
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
        name = "META-DATA-ITEM"

    length: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    meta_data_item_type: None | TextValueSpecification = field(
        default=None,
        metadata={
            "name": "META-DATA-ITEM-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
