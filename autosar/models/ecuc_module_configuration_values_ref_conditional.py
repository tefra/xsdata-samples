from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .ecuc_module_configuration_values_subtypes_enum import (
    EcucModuleConfigurationValuesSubtypesEnum,
)
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EcucModuleConfigurationValuesRefConditional:
    """
    This element was generated/modified due to an atpVariation stereotype.

    :ivar ecuc_module_configuration_values_ref:
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
        name = "ECUC-MODULE-CONFIGURATION-VALUES-REF-CONDITIONAL"

    ecuc_module_configuration_values_ref: (
        EcucModuleConfigurationValuesRefConditional.EcucModuleConfigurationValuesRef
        | None
    ) = field(
        default=None,
        metadata={
            "name": "ECUC-MODULE-CONFIGURATION-VALUES-REF",
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
    class EcucModuleConfigurationValuesRef(Ref):
        dest: EcucModuleConfigurationValuesSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
