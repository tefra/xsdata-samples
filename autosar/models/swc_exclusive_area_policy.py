from dataclasses import dataclass, field
from typing import Optional
from .admin_data import VariationPoint
from .api_principle_enum import ApiPrincipleEnum
from .exclusive_area_subtypes_enum import ExclusiveAreaSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwcExclusiveAreaPolicy:
    """Options how to generate the ExclusiveArea related APIs.

    If no SwcExclusiveAreaPolicy is specified for an ExclusiveArea the
    default values apply.

    :ivar api_principle: Specifies for this ExclusiveArea if either one
        common set of Enter and Exit APIs for the whole software
        component is requested from the Rte or if the set of Enter and
        Exit APIs is expected per RunnableEntity. The default value is
        "common".
    :ivar exclusive_area_ref: This reference represents the
        ExclusiveArea for which the policy applies.
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
        name = "SWC-EXCLUSIVE-AREA-POLICY"

    api_principle: Optional[ApiPrincipleEnum] = field(
        default=None,
        metadata={
            "name": "API-PRINCIPLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    exclusive_area_ref: Optional[
        "SwcExclusiveAreaPolicy.ExclusiveAreaRef"
    ] = field(
        default=None,
        metadata={
            "name": "EXCLUSIVE-AREA-REF",
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
    class ExclusiveAreaRef(Ref):
        dest: Optional[ExclusiveAreaSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
