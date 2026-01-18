from __future__ import annotations

from dataclasses import dataclass

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.program_gbotype import (
    ProgramGbotype,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass(kw_only=True)
class Program(ProgramGbotype):
    class Meta:
        namespace = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
