from dataclasses import dataclass, field

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1"


@dataclass
class ExtendedRecordTypeBusinessLines:
    class Meta:
        global_type = False

    business_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "BusinessLine",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
