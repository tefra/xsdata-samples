from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    DocumentationBlock,
)
from .category_string import CategoryString
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .someip_transformation_i_signal_props_conditional import (
    SomeipTransformationISignalPropsConditional,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class SomeipTransformationISignalProps:
    """
    The class SOMEIPTransformationISignalProps specifies ISignal specific
    configuration properties for SOME/IP transformer attributes.

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
    :ivar someip_transformation_i_signal_props_variants: This element
        was generated/modified due to an atpVariation stereotype.
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
        name = "SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS"

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
    someip_transformation_i_signal_props_variants: (
        None
        | SomeipTransformationISignalProps.SomeipTransformationISignalPropsVariants
    ) = field(
        default=None,
        metadata={
            "name": "SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS",
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
    class SomeipTransformationISignalPropsVariants:
        someip_transformation_i_signal_props_conditional: list[
            SomeipTransformationISignalPropsConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
