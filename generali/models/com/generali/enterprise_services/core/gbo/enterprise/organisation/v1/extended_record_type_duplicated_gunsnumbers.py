from dataclasses import dataclass, field

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1"


@dataclass
class ExtendedRecordTypeDuplicatedGunsnumbers:
    class Meta:
        global_type = False

    duplicated_gunsnumber: list[str] = field(
        default_factory=list,
        metadata={
            "name": "DuplicatedGUNSNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "length": 10,
            "pattern": r"G([0-9]{9})",
        },
    )
