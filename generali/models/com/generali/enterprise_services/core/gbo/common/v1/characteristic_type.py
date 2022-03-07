from dataclasses import dataclass, field
from typing import List, Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_simple_component_type import BaseSimpleComponentType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.characteristic_value_type import CharacteristicValueType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class CharacteristicType(BaseSimpleComponentType):
    """<description xmlns="">A characteristic, a name and value.

    An Example might be Colour="Black" or Memory="32
    GBytes".</description>
    """
    values: Optional["CharacteristicType.Values"] = field(
        default=None,
        metadata={
            "name": "Values",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "required": True,
        }
    )

    @dataclass
    class Values:
        """
        :ivar value: <description xmlns="">A value of the
            characteristic.</description>
        """
        value: List[CharacteristicValueType] = field(
            default_factory=list,
            metadata={
                "name": "Value",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
                "min_occurs": 1,
            }
        )
