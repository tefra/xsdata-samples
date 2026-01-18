from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .hw_element_subtypes_enum import HwElementSubtypesEnum
from .hw_pin_connector import HwPinConnector
from .hw_pin_group_connector import HwPinGroupConnector
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class HwElementConnector:
    """
    This meta-class represents the ability to connect two hardware
    elements.

    The details of the connection can be refined by hwPinGroupConnection.

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
    :ivar hw_element_refs: This association connects two hardware
        elements.
    :ivar hw_pin_group_connections: This represents one particular
        connection between two hardware pin groups. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar hw_pin_connections: This represents one particular connection
        between two hardware pins. This connection shall be used if pin-
        to-pin-connection is to be described but no description of the
        connection between the hierarchical composition of HwPinGroups
        (using HwPinGroupConnector) is required. The upper multiplicity
        of this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was -1.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "HW-ELEMENT-CONNECTOR"

    desc: None | MultiLanguageOverviewParagraph = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: None | CategoryString = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: None | DocumentationBlock = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: None | AdminData = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    hw_element_refs: None | HwElementConnector.HwElementRefs = field(
        default=None,
        metadata={
            "name": "HW-ELEMENT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    hw_pin_group_connections: (
        None | HwElementConnector.HwPinGroupConnections
    ) = field(
        default=None,
        metadata={
            "name": "HW-PIN-GROUP-CONNECTIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    hw_pin_connections: None | HwElementConnector.HwPinConnections = field(
        default=None,
        metadata={
            "name": "HW-PIN-CONNECTIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: None | VariationPoint = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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

    @dataclass(kw_only=True)
    class HwElementRefs:
        hw_element_ref: list[HwElementConnector.HwElementRefs.HwElementRef] = (
            field(
                default_factory=list,
                metadata={
                    "name": "HW-ELEMENT-REF",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                    "max_occurs": 2,
                },
            )
        )

        @dataclass(kw_only=True)
        class HwElementRef(Ref):
            dest: HwElementSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass(kw_only=True)
    class HwPinGroupConnections:
        hw_pin_group_connector: list[HwPinGroupConnector] = field(
            default_factory=list,
            metadata={
                "name": "HW-PIN-GROUP-CONNECTOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class HwPinConnections:
        hw_pin_connector: list[HwPinConnector] = field(
            default_factory=list,
            metadata={
                "name": "HW-PIN-CONNECTOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
