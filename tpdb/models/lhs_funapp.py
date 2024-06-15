from dataclasses import dataclass, field
from typing import List, Optional

from tpdb.models.name import Name
from tpdb.models.type_mod import TypeType
from tpdb.models.var import Var


@dataclass
class LhsFunapp:
    class Meta:
        global_type = False

    name: Optional[Name] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    arg: List["LhsFunappArg"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class LhsLambda:
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

    var: List[Var] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    type_value: Optional[TypeType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    funapp: Optional[LhsFunapp] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lambda_value: Optional["LhsLambda"] = field(
        default=None,
        metadata={
            "name": "lambda",
            "type": "Element",
        },
    )
    application: Optional["LhsApplication"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class LhsApplication:
    """
    :ivar funapp:
    :ivar var:
    :ivar lambda_value: the type is the type of the bound variable
    :ivar application: an application of a function (first term) on an
        argument (second term): (first second)
    """

    class Meta:
        global_type = False

    funapp: List[LhsFunapp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    var: List[Var] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    lambda_value: List[LhsLambda] = field(
        default_factory=list,
        metadata={
            "name": "lambda",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    application: List["LhsApplication"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 1,
        },
    )


@dataclass
class LhsFunappArg:
    """
    :ivar funapp:
    :ivar var:
    :ivar lambda_value: the type is the type of the bound variable
    :ivar application: an application of a function (first term) on an
        argument (second term): (first second)
    """

    class Meta:
        global_type = False

    funapp: Optional[LhsFunapp] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    var: Optional[Var] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lambda_value: Optional[LhsLambda] = field(
        default=None,
        metadata={
            "name": "lambda",
            "type": "Element",
        },
    )
    application: Optional[LhsApplication] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
