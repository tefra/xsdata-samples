from dataclasses import dataclass

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class UkspecifiedQuantitySolidFuelCodeType(CodeType):
    """
    A codelist restricting a code to the set that can be sold in the UK for solid
    fuel.
    """

    class Meta:
        name = "UKSpecifiedQuantitySolidFuelCodeType"
