from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .cs_transformer_error_reaction_enum import CsTransformerErrorReactionEnum
from .data_prototype_transformation_props import (
    DataPrototypeTransformationProps,
)
from .positive_integer import PositiveInteger
from .ref import Ref
from .transformation_technology_subtypes_enum import (
    TransformationTechnologySubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EndToEndTransformationISignalPropsConditional:
    """
    This element was generated/modified due to an atpVariation stereotype.

    :ivar cs_error_reaction: Defines whether the transformer chain of
        client/server communication coordinates an autonomous error
        reaction together with the RTE or whether any error reaction is
        the responsibility of the application.
    :ivar data_prototype_transformation_propss: Fine granular modeling
        of TransfromationProps on the level of DataPrototypes.
    :ivar transformer_ref: Reference to the TransformationTechnology
        description that contains transformer specific and ISignal
        independent configuration properties.
    :ivar data_ids:
    :ivar data_length: Length of payload and E2E header in bits.
    :ivar max_data_length: Maximum length of payload and E2E header in
        bits.
    :ivar min_data_length: Minimum length of payload and E2E header in
        bits.
    :ivar source_id: This attribute represents a unique numerical
        identifier identifying the source of a certain transmission. In
        case of C/S communication, this ID uniquely identifies the
        client. Note: ID is used for protection against masquerading.
        The details concerning the maximum number of values (this
        information is specific for each E2E profile) applicable for
        this attribute are controlled by a semantic constraint that
        depends on the category of the EndToEndProtection.
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
        name = "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL"

    cs_error_reaction: CsTransformerErrorReactionEnum | None = field(
        default=None,
        metadata={
            "name": "CS-ERROR-REACTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_prototype_transformation_propss: (
        EndToEndTransformationISignalPropsConditional.DataPrototypeTransformationPropss
        | None
    ) = field(
        default=None,
        metadata={
            "name": "DATA-PROTOTYPE-TRANSFORMATION-PROPSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transformer_ref: (
        EndToEndTransformationISignalPropsConditional.TransformerRef | None
    ) = field(
        default=None,
        metadata={
            "name": "TRANSFORMER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_ids: EndToEndTransformationISignalPropsConditional.DataIds | None = (
        field(
            default=None,
            metadata={
                "name": "DATA-IDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    data_length: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "DATA-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_data_length: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "MAX-DATA-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    min_data_length: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "MIN-DATA-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    source_id: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "SOURCE-ID",
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

    @dataclass
    class DataPrototypeTransformationPropss:
        data_prototype_transformation_props: list[
            DataPrototypeTransformationProps
        ] = field(
            default_factory=list,
            metadata={
                "name": "DATA-PROTOTYPE-TRANSFORMATION-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class TransformerRef(Ref):
        dest: TransformationTechnologySubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class DataIds:
        """
        :ivar data_id: This represents a unique numerical identifier.
            Note: ID is used for protection against masquerading. The
            details concerning the maximum number of values (this
            information is specific for each E2E profile) applicable for
            this attribute are controlled by a semantic constraint that
            depends on the category of the EndToEndProtection.
        """

        data_id: list[PositiveInteger] = field(
            default_factory=list,
            metadata={
                "name": "DATA-ID",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
