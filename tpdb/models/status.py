from dataclasses import dataclass, field

from tpdb.models.maybe import Maybe
from tpdb.models.no import No
from tpdb.models.yes import Yes


@dataclass
class Status:
    """
    This tag shows the termination status of this problem, if known.

    The reason for using sub-elements is that &lt;yes/&gt; can optionally
    be extended by complexity bound information.
    """

    class Meta:
        name = "status"

    no: No | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    maybe: Maybe | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    yes: Yes | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
