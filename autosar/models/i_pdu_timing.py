from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .time_value import TimeValue
from .transmission_mode_declaration import TransmissionModeDeclaration

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class IPduTiming:
    """
    AUTOSAR COM provides the possibility to define two different
    TRANSMISSION MODES for each IPdu.

    The Transmission Mode of an IPdu that is valid at a specific point in
    time is selected using the values of the signals that are mapped to
    this IPdu. For each IPdu a Transmission Mode Selector is defined. The
    Transmission Mode Selector is calculated by evaluating the conditions
    for a subset of signals (class TransmissionModeCondition in the System
    Template). The Transmission Mode Selector is defined to be true, if at
    least one Condition evaluates to true and is defined to be false, if
    all Conditions evaluate to false.

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
    :ivar minimum_delay: Minimum Delay in seconds between successive
        transmissions of this I-PDU, independent of the Transmission
        Mode.
    :ivar transmission_mode_declaration: AUTOSAR COM allows configuring
        statically two different transmission modes for each I-PDU (True
        and False). The Transmission Mode Selector evaluates the
        conditions for a subset of signals and decides the transmission
        mode. It is possible to switch between the transmission modes
        during runtime.
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
        name = "I-PDU-TIMING"

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
    minimum_delay: None | TimeValue = field(
        default=None,
        metadata={
            "name": "MINIMUM-DELAY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transmission_mode_declaration: None | TransmissionModeDeclaration = field(
        default=None,
        metadata={
            "name": "TRANSMISSION-MODE-DECLARATION",
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
