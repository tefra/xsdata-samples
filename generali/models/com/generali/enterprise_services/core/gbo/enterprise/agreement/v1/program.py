from dataclasses import dataclass

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.program_gbotype import (
    ProgramGbotype,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class Program(ProgramGbotype):
    class Meta:
        namespace = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
