from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .admin_data import VariationPoint
from .api_principle_enum import ApiPrincipleEnum
from .boolean import Boolean
from .exclusive_area_subtypes_enum import ExclusiveAreaSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BswExclusiveAreaPolicy:
    """
    The ExclusiveArea for which the BSW Scheduler using this policy.

    :ivar enable_take_address: If set to true, the BSW Module is able to
        use the API reference for deriving a pointer to an object
    :ivar api_principle: Specifies for this ExclusiveArea if either one
        common set of Enter and Exit APIs for the whole BSW module is
        requested from the SchM or if the set of Enter and Exit APIs is
        expected per BswModuleEntity. The default value is "common".
    :ivar exclusive_area_ref: The ExclusiveArea for which the BSW
        Scheduler using this policy.
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
        name = "BSW-EXCLUSIVE-AREA-POLICY"

    enable_take_address: Boolean | None = field(
        default=None,
        metadata={
            "name": "ENABLE-TAKE-ADDRESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    api_principle: ApiPrincipleEnum | None = field(
        default=None,
        metadata={
            "name": "API-PRINCIPLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    exclusive_area_ref: BswExclusiveAreaPolicy.ExclusiveAreaRef | None = (
        field(
            default=None,
            metadata={
                "name": "EXCLUSIVE-AREA-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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
    class ExclusiveAreaRef(Ref):
        dest: ExclusiveAreaSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
