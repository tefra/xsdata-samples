from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ScnPolicyRef:
    """
    An individual SCN policy.
    """

    class Meta:
        name = "scn_policy_ref"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 2048,
            "pattern": r"([hH][tT][tT][pP]|[hH][tT][tT][pP][sS]|[fF][tT][pP])://.*",
        },
    )
