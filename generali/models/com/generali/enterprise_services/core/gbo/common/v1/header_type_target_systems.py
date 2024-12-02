from dataclasses import dataclass, field

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class HeaderTypeTargetSystems:
    class Meta:
        global_type = False

    target_system: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TargetSystem",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
