from dataclasses import dataclass, field
from typing import List
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.cover_gbotype import CoverGbotype

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


@dataclass
class ProgramGbotypeCovers:
    class Meta:
        global_type = False

    cover: List[CoverGbotype] = field(
        default_factory=list,
        metadata={
            "name": "Cover",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
