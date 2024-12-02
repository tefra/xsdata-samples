from dataclasses import dataclass, field
from typing import Optional

from .meta_data_item import MetaDataItem
from .ref import Ref
from .variable_data_prototype_subtypes_enum import (
    VariableDataPrototypeSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class MetaDataItemSet:
    """
    This meta-class represents the ability to define a set of meta-data items to be
    used in SenderReceiverInterfaces.

    :ivar data_element_refs: This reference identifies the dataElement
        for which the ordered list of meta-data items is defined.
    :ivar meta_data_items: This aggregation represents the ordered
        definition of meta-data items.
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
        name = "META-DATA-ITEM-SET"

    data_element_refs: Optional["MetaDataItemSet.DataElementRefs"] = field(
        default=None,
        metadata={
            "name": "DATA-ELEMENT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    meta_data_items: Optional["MetaDataItemSet.MetaDataItems"] = field(
        default=None,
        metadata={
            "name": "META-DATA-ITEMS",
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

    @dataclass
    class DataElementRefs:
        data_element_ref: list[
            "MetaDataItemSet.DataElementRefs.DataElementRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "DATA-ELEMENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class DataElementRef(Ref):
            dest: Optional[VariableDataPrototypeSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class MetaDataItems:
        meta_data_item: list[MetaDataItem] = field(
            default_factory=list,
            metadata={
                "name": "META-DATA-ITEM",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
