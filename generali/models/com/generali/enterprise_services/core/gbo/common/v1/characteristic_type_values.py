from dataclasses import dataclass, field
from typing import List

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.characteristic_value_type import (
    CharacteristicValueType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class CharacteristicTypeValues:
    """
    :ivar value: <description xmlns="">A value of the
        characteristic.</description>
    """

    class Meta:
        global_type = False

    value: List[CharacteristicValueType] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "min_occurs": 1,
        },
    )
