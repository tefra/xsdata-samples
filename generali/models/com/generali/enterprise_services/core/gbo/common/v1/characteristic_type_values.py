from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.characteristic_value_type import (
    CharacteristicValueType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass(kw_only=True)
class CharacteristicTypeValues:
    """
    :ivar value: <description xmlns="">A value of the
        characteristic.</description>
    """

    class Meta:
        global_type = False

    value: list[CharacteristicValueType] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "min_occurs": 1,
        },
    )
