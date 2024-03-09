from dataclasses import dataclass, field
from typing import List, Optional

from .admin_data import VariationPoint
from .cs_transformer_error_reaction_enum import CsTransformerErrorReactionEnum
from .data_prototype_transformation_props import (
    DataPrototypeTransformationProps,
)
from .ref import Ref
from .transformation_technology_subtypes_enum import (
    TransformationTechnologySubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class UserDefinedTransformationISignalPropsConditional:
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
        name = "USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL"

    cs_error_reaction: Optional[CsTransformerErrorReactionEnum] = field(
        default=None,
        metadata={
            "name": "CS-ERROR-REACTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_prototype_transformation_propss: Optional[
        "UserDefinedTransformationISignalPropsConditional.DataPrototypeTransformationPropss"
    ] = field(
        default=None,
        metadata={
            "name": "DATA-PROTOTYPE-TRANSFORMATION-PROPSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transformer_ref: Optional[
        "UserDefinedTransformationISignalPropsConditional.TransformerRef"
    ] = field(
        default=None,
        metadata={
            "name": "TRANSFORMER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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
    class DataPrototypeTransformationPropss:
        data_prototype_transformation_props: List[
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
        dest: Optional[TransformationTechnologySubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
