from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.lhs_funapp import (
    LhsApplication,
    LhsFunapp,
    LhsLambda,
)
from tpdb.models.var import Var


@dataclass
class Lhs:
    """
    :ivar funapp:
    :ivar var:
    :ivar lambda_value: the type is the type of the bound variable
    :ivar application: an application of a function (first term) on an
        argument (second term): (first second)
    """

    class Meta:
        name = "lhs"

    funapp: None | LhsFunapp = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    var: None | Var = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lambda_value: None | LhsLambda = field(
        default=None,
        metadata={
            "name": "lambda",
            "type": "Element",
        },
    )
    application: None | LhsApplication = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
