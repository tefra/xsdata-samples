from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from tpdb.models.name import Name
from tpdb.models.type_mod import Type
from tpdb.models.var import Var


@dataclass
class RhsFunapp:
    class Meta:
        global_type = False

    name: Name | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    arg: list[RhsFunappArg] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RhsLambda:
    """
    :ivar var:
    :ivar type_value:
    :ivar funapp:
    :ivar lambda_value: the type is the type of the bound variable
    :ivar application: an application of a function (first term) on an
        argument (second term): (first second)
    """

    class Meta:
        global_type = False

    var: list[Var] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    type_value: Type | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    funapp: RhsFunapp | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lambda_value: RhsLambda | None = field(
        default=None,
        metadata={
            "name": "lambda",
            "type": "Element",
        },
    )
    application: RhsApplication | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RhsApplication:
    """
    :ivar funapp:
    :ivar var:
    :ivar lambda_value: the type is the type of the bound variable
    :ivar application: an application of a function (first term) on an
        argument (second term): (first second)
    """

    class Meta:
        global_type = False

    funapp: list[RhsFunapp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    var: list[Var] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    lambda_value: list[RhsLambda] = field(
        default_factory=list,
        metadata={
            "name": "lambda",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    application: list[RhsApplication] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 1,
        },
    )


@dataclass
class RhsFunappArg:
    """
    :ivar funapp:
    :ivar var:
    :ivar lambda_value: the type is the type of the bound variable
    :ivar application: an application of a function (first term) on an
        argument (second term): (first second)
    """

    class Meta:
        global_type = False

    funapp: RhsFunapp | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    var: Var | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lambda_value: RhsLambda | None = field(
        default=None,
        metadata={
            "name": "lambda",
            "type": "Element",
        },
    )
    application: RhsApplication | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
