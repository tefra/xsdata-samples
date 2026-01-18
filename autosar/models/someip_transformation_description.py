from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    DocumentationBlock,
    VariationPoint,
)
from .byte_order_enum import ByteOrderEnum
from .category_string import CategoryString
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SomeipTransformationDescription:
    """
    The SOMEIPTransformationDescription is used to specify SOME/IP
    transformer specific attributes.

    :ivar desc: This represents a general but brief (one paragraph)
        description what the object in question is about. It is only one
        paragraph! Desc is intended to be collected into overview
        tables. This property helps a human reader to identify the
        object in question. More elaborate documentation, (in particlar
        how the object is built or used) should go to "introduction".
    :ivar category: The category is a keyword that specializes the
        semantics of the Describable. It affects the expected existence
        of attributes and the applicability of constraints.
    :ivar introduction: This represents more information about how the
        object in question is built or is used. Therefore it is a
        DocumentationBlock.
    :ivar admin_data: This represents the administrative data for the
        describable object.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar alignment: Defines the padding for alignment purposes that
        will be added by the SOME/IP transformer after the serialized
        data of the variable data length data element. The alignment
        shall be specified in Bits.
    :ivar byte_order: Defines which byte order shall be serialized by
        the SOME/IP transformer
    :ivar interface_version: The interface version the SOME/IP
        transformer shall use.
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
        name = "SOMEIP-TRANSFORMATION-DESCRIPTION"

    desc: MultiLanguageOverviewParagraph | None = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: CategoryString | None = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: DocumentationBlock | None = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: AdminData | None = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: VariationPoint | None = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    alignment: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "ALIGNMENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    byte_order: ByteOrderEnum | None = field(
        default=None,
        metadata={
            "name": "BYTE-ORDER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    interface_version: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "INTERFACE-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
