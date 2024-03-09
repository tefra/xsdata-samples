from dataclasses import dataclass

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class UomAmountOfInformationSicodeType(CodeType):
    """
    A codelist for the amount of information (SI version).
    """

    class Meta:
        name = "UomAmountOfInformationSICodeType"
