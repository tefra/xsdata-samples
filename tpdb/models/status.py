from dataclasses import dataclass, field
from typing import Optional

from tpdb.models.maybe import Maybe
from tpdb.models.no import No
from tpdb.models.yes import Yes


@dataclass
class Status:
    """This tag shows the termination status of this problem, if known.

    The reason for using sub-elements is that &lt;yes/&gt; can
    optionally be extended by complexity bound information.
    """

    class Meta:
        name = "status"

    no: Optional[No] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    maybe: Optional[Maybe] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    yes: Optional[Yes] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
