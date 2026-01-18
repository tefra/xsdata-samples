from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.characteristic_type import (
    CharacteristicType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class CharacteristicsType:
    """
    <description xmlns="">The set of characteristics for a business
    object.</description>.

    :ivar characteristic: <description xmlns="">A characteristic, a name
        and value. An Example might be Colour="Black" or Memory="32
        GBytes".</description>
    """

    characteristic: list[CharacteristicType] = field(
        default_factory=list,
        metadata={
            "name": "Characteristic",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "min_occurs": 1,
        },
    )
