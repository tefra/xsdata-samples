from dataclasses import dataclass, field
from typing import Dict, List, Optional

from crossref.models.org.w3.pkg_1998.math.math_ml.abs import Abs
from crossref.models.org.w3.pkg_1998.math.math_ml.and_mod import And
from crossref.models.org.w3.pkg_1998.math.math_ml.approx import Approx
from crossref.models.org.w3.pkg_1998.math.math_ml.arccos import Arccos
from crossref.models.org.w3.pkg_1998.math.math_ml.arccosh import Arccosh
from crossref.models.org.w3.pkg_1998.math.math_ml.arccot import Arccot
from crossref.models.org.w3.pkg_1998.math.math_ml.arccoth import Arccoth
from crossref.models.org.w3.pkg_1998.math.math_ml.arccsc import Arccsc
from crossref.models.org.w3.pkg_1998.math.math_ml.arccsch import Arccsch
from crossref.models.org.w3.pkg_1998.math.math_ml.arcsec import Arcsec
from crossref.models.org.w3.pkg_1998.math.math_ml.arcsech import Arcsech
from crossref.models.org.w3.pkg_1998.math.math_ml.arcsin import Arcsin
from crossref.models.org.w3.pkg_1998.math.math_ml.arcsinh import Arcsinh
from crossref.models.org.w3.pkg_1998.math.math_ml.arctan import Arctan
from crossref.models.org.w3.pkg_1998.math.math_ml.arctanh import Arctanh
from crossref.models.org.w3.pkg_1998.math.math_ml.arg import Arg
from crossref.models.org.w3.pkg_1998.math.math_ml.card import Card
from crossref.models.org.w3.pkg_1998.math.math_ml.cartesianproduct import (
    Cartesianproduct,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.cbytes import Cbytes
from crossref.models.org.w3.pkg_1998.math.math_ml.ceiling import Ceiling
from crossref.models.org.w3.pkg_1998.math.math_ml.cerror import (
    Apply,
    Bind,
    Bvar,
    Cerror,
    Ci,
    Cn,
    Condition,
    Csymbol,
    Declare,
    Domainofapplication,
    Fn,
    ListType,
    Lowlimit,
    Piecewise,
    Reln,
    Set,
    Uplimit,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.codomain import Codomain
from crossref.models.org.w3.pkg_1998.math.math_ml.complexes import Complexes
from crossref.models.org.w3.pkg_1998.math.math_ml.compose import Compose
from crossref.models.org.w3.pkg_1998.math.math_ml.conjugate import Conjugate
from crossref.models.org.w3.pkg_1998.math.math_ml.cos import Cos
from crossref.models.org.w3.pkg_1998.math.math_ml.cosh import Cosh
from crossref.models.org.w3.pkg_1998.math.math_ml.cot import Cot
from crossref.models.org.w3.pkg_1998.math.math_ml.coth import Coth
from crossref.models.org.w3.pkg_1998.math.math_ml.cs import Cs
from crossref.models.org.w3.pkg_1998.math.math_ml.csc import Csc
from crossref.models.org.w3.pkg_1998.math.math_ml.csch import Csch
from crossref.models.org.w3.pkg_1998.math.math_ml.curl import Curl
from crossref.models.org.w3.pkg_1998.math.math_ml.determinant import (
    Determinant,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.diff import Diff
from crossref.models.org.w3.pkg_1998.math.math_ml.divergence import Divergence
from crossref.models.org.w3.pkg_1998.math.math_ml.divide import Divide
from crossref.models.org.w3.pkg_1998.math.math_ml.domain import Domain
from crossref.models.org.w3.pkg_1998.math.math_ml.emptyset import Emptyset
from crossref.models.org.w3.pkg_1998.math.math_ml.eq import Eq
from crossref.models.org.w3.pkg_1998.math.math_ml.equivalent import Equivalent
from crossref.models.org.w3.pkg_1998.math.math_ml.eulergamma import Eulergamma
from crossref.models.org.w3.pkg_1998.math.math_ml.exists import Exists
from crossref.models.org.w3.pkg_1998.math.math_ml.exp import Exp
from crossref.models.org.w3.pkg_1998.math.math_ml.exponentiale import (
    Exponentiale,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.factorial import Factorial
from crossref.models.org.w3.pkg_1998.math.math_ml.factorof import Factorof
from crossref.models.org.w3.pkg_1998.math.math_ml.false import FalseType
from crossref.models.org.w3.pkg_1998.math.math_ml.floor import Floor
from crossref.models.org.w3.pkg_1998.math.math_ml.forall import Forall
from crossref.models.org.w3.pkg_1998.math.math_ml.gcd import Gcd
from crossref.models.org.w3.pkg_1998.math.math_ml.geq import Geq
from crossref.models.org.w3.pkg_1998.math.math_ml.grad import Grad
from crossref.models.org.w3.pkg_1998.math.math_ml.gt import Gt
from crossref.models.org.w3.pkg_1998.math.math_ml.ident import Ident
from crossref.models.org.w3.pkg_1998.math.math_ml.image import Image
from crossref.models.org.w3.pkg_1998.math.math_ml.imaginary import Imaginary
from crossref.models.org.w3.pkg_1998.math.math_ml.imaginaryi import Imaginaryi
from crossref.models.org.w3.pkg_1998.math.math_ml.implies import Implies
from crossref.models.org.w3.pkg_1998.math.math_ml.in_mod import In
from crossref.models.org.w3.pkg_1998.math.math_ml.infinity import Infinity
from crossref.models.org.w3.pkg_1998.math.math_ml.int_mod import Int
from crossref.models.org.w3.pkg_1998.math.math_ml.integers import Integers
from crossref.models.org.w3.pkg_1998.math.math_ml.intersect import Intersect
from crossref.models.org.w3.pkg_1998.math.math_ml.interval import Interval
from crossref.models.org.w3.pkg_1998.math.math_ml.inverse import Inverse
from crossref.models.org.w3.pkg_1998.math.math_ml.lambda_mod import Lambda
from crossref.models.org.w3.pkg_1998.math.math_ml.laplacian import Laplacian
from crossref.models.org.w3.pkg_1998.math.math_ml.lcm import Lcm
from crossref.models.org.w3.pkg_1998.math.math_ml.leq import Leq
from crossref.models.org.w3.pkg_1998.math.math_ml.limit import Limit
from crossref.models.org.w3.pkg_1998.math.math_ml.ln import Ln
from crossref.models.org.w3.pkg_1998.math.math_ml.log import Log
from crossref.models.org.w3.pkg_1998.math.math_ml.lt import Lt
from crossref.models.org.w3.pkg_1998.math.math_ml.matrix import Matrix
from crossref.models.org.w3.pkg_1998.math.math_ml.matrixrow import Matrixrow
from crossref.models.org.w3.pkg_1998.math.math_ml.max import Max
from crossref.models.org.w3.pkg_1998.math.math_ml.mean import Mean
from crossref.models.org.w3.pkg_1998.math.math_ml.median import Median
from crossref.models.org.w3.pkg_1998.math.math_ml.min import Min
from crossref.models.org.w3.pkg_1998.math.math_ml.minus import Minus
from crossref.models.org.w3.pkg_1998.math.math_ml.mode import Mode
from crossref.models.org.w3.pkg_1998.math.math_ml.moment import Moment
from crossref.models.org.w3.pkg_1998.math.math_ml.naturalnumbers import (
    Naturalnumbers,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.neq import Neq
from crossref.models.org.w3.pkg_1998.math.math_ml.not_mod import Not
from crossref.models.org.w3.pkg_1998.math.math_ml.notanumber import Notanumber
from crossref.models.org.w3.pkg_1998.math.math_ml.notin import Notin
from crossref.models.org.w3.pkg_1998.math.math_ml.notprsubset import (
    Notprsubset,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.notsubset import Notsubset
from crossref.models.org.w3.pkg_1998.math.math_ml.or_mod import Or
from crossref.models.org.w3.pkg_1998.math.math_ml.outerproduct import (
    Outerproduct,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.partialdiff import (
    Partialdiff,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.pi import Pi
from crossref.models.org.w3.pkg_1998.math.math_ml.plus import Plus
from crossref.models.org.w3.pkg_1998.math.math_ml.power import Power
from crossref.models.org.w3.pkg_1998.math.math_ml.primes import Primes
from crossref.models.org.w3.pkg_1998.math.math_ml.product import Product
from crossref.models.org.w3.pkg_1998.math.math_ml.prsubset import Prsubset
from crossref.models.org.w3.pkg_1998.math.math_ml.quotient import Quotient
from crossref.models.org.w3.pkg_1998.math.math_ml.rationals import Rationals
from crossref.models.org.w3.pkg_1998.math.math_ml.real import Real
from crossref.models.org.w3.pkg_1998.math.math_ml.reals import Reals
from crossref.models.org.w3.pkg_1998.math.math_ml.rem import Rem
from crossref.models.org.w3.pkg_1998.math.math_ml.root import Root
from crossref.models.org.w3.pkg_1998.math.math_ml.scalarproduct import (
    Scalarproduct,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.sdev import Sdev
from crossref.models.org.w3.pkg_1998.math.math_ml.sec import Sec
from crossref.models.org.w3.pkg_1998.math.math_ml.sech import Sech
from crossref.models.org.w3.pkg_1998.math.math_ml.selector import Selector
from crossref.models.org.w3.pkg_1998.math.math_ml.setdiff import Setdiff
from crossref.models.org.w3.pkg_1998.math.math_ml.share import Share
from crossref.models.org.w3.pkg_1998.math.math_ml.sin import Sin
from crossref.models.org.w3.pkg_1998.math.math_ml.sinh import Sinh
from crossref.models.org.w3.pkg_1998.math.math_ml.subset import Subset
from crossref.models.org.w3.pkg_1998.math.math_ml.sum import Sum
from crossref.models.org.w3.pkg_1998.math.math_ml.tan import Tan
from crossref.models.org.w3.pkg_1998.math.math_ml.tanh import Tanh
from crossref.models.org.w3.pkg_1998.math.math_ml.tendsto import Tendsto
from crossref.models.org.w3.pkg_1998.math.math_ml.times import Times
from crossref.models.org.w3.pkg_1998.math.math_ml.transpose import Transpose
from crossref.models.org.w3.pkg_1998.math.math_ml.true import TrueType
from crossref.models.org.w3.pkg_1998.math.math_ml.union import UnionType
from crossref.models.org.w3.pkg_1998.math.math_ml.variance import Variance
from crossref.models.org.w3.pkg_1998.math.math_ml.vector import Vector
from crossref.models.org.w3.pkg_1998.math.math_ml.vectorproduct import (
    Vectorproduct,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.xor import Xor

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass
class NaryConstructorType:
    class Meta:
        name = "nary-constructor.class"
        namespace = "http://www.w3.org/1998/Math/MathML"

    bvar: List[Bvar] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    domainofapplication: List[Domainofapplication] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    condition: List[Condition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    lowlimit: List[Lowlimit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    uplimit: List[Uplimit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    apply: List[Apply] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    bind: List[Bind] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ci: List[Ci] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cn: List[Cn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    csymbol: List[Csymbol] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cbytes: List[Cbytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cerror: List[Cerror] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cs: List[Cs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    share: List[Share] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    piecewise: List[Piecewise] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    declare: List[Declare] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fn: List[Fn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    reln: List[Reln] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    interval: List[Interval] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    moment: List[Moment] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    log: List[Log] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ln: List[Ln] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    image: List[Image] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    codomain: List[Codomain] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    domain: List[Domain] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ident: List[Ident] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    inverse: List[Inverse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    lambda_value: List[Lambda] = field(
        default_factory=list,
        metadata={
            "name": "lambda",
            "type": "Element",
        },
    )
    compose: List[Compose] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    quotient: List[Quotient] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    divide: List[Divide] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    minus: List[Minus] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    power: List[Power] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    rem: List[Rem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    root: List[Root] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    factorial: List[Factorial] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    abs: List[Abs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    conjugate: List[Conjugate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arg: List[Arg] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    real: List[Real] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    imaginary: List[Imaginary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    floor: List[Floor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ceiling: List[Ceiling] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    exp: List[Exp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    min: List[Min] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    max: List[Max] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    lcm: List[Lcm] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    gcd: List[Gcd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    times: List[Times] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    plus: List[Plus] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    xor: List[Xor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    or_value: List[Or] = field(
        default_factory=list,
        metadata={
            "name": "or",
            "type": "Element",
        },
    )
    and_value: List[And] = field(
        default_factory=list,
        metadata={
            "name": "and",
            "type": "Element",
        },
    )
    not_value: List[Not] = field(
        default_factory=list,
        metadata={
            "name": "not",
            "type": "Element",
        },
    )
    equivalent: List[Equivalent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    implies: List[Implies] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    exists: List[Exists] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    forall: List[Forall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    leq: List[Leq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    geq: List[Geq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    lt: List[Lt] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    gt: List[Gt] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    eq: List[Eq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    tendsto: List[Tendsto] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    factorof: List[Factorof] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    approx: List[Approx] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    neq: List[Neq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    int_value: List[Int] = field(
        default_factory=list,
        metadata={
            "name": "int",
            "type": "Element",
        },
    )
    diff: List[Diff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    partialdiff: List[Partialdiff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    laplacian: List[Laplacian] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    curl: List[Curl] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    grad: List[Grad] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    divergence: List[Divergence] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    set: List[Set] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cartesianproduct: List[Cartesianproduct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    intersect: List[Intersect] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    union: List[UnionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    setdiff: List[Setdiff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    notprsubset: List[Notprsubset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    notsubset: List[Notsubset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    notin: List[Notin] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    in_value: List[In] = field(
        default_factory=list,
        metadata={
            "name": "in",
            "type": "Element",
        },
    )
    prsubset: List[Prsubset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    subset: List[Subset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    card: List[Card] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sum: List[Sum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    product: List[Product] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    limit: List[Limit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arctanh: List[Arctanh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arcsinh: List[Arcsinh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arcsech: List[Arcsech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arcsec: List[Arcsec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arccsch: List[Arccsch] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arccsc: List[Arccsc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arccoth: List[Arccoth] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arccot: List[Arccot] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arccosh: List[Arccosh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arctan: List[Arctan] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arccos: List[Arccos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arcsin: List[Arcsin] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    coth: List[Coth] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    csch: List[Csch] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sech: List[Sech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    tanh: List[Tanh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cosh: List[Cosh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sinh: List[Sinh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cot: List[Cot] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    csc: List[Csc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sec: List[Sec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    tan: List[Tan] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cos: List[Cos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sin: List[Sin] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mode: List[Mode] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    median: List[Median] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    variance: List[Variance] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sdev: List[Sdev] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mean: List[Mean] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    matrixrow: List[Matrixrow] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    matrix: List[Matrix] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    vector: List[Vector] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    transpose: List[Transpose] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    determinant: List[Determinant] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    selector: List[Selector] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    outerproduct: List[Outerproduct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    scalarproduct: List[Scalarproduct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    vectorproduct: List[Vectorproduct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    emptyset: List[Emptyset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    primes: List[Primes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    complexes: List[Complexes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    naturalnumbers: List[Naturalnumbers] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    rationals: List[Rationals] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    reals: List[Reals] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    integers: List[Integers] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    infinity: List[Infinity] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    eulergamma: List[Eulergamma] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    pi: List[Pi] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    false: List[FalseType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    true: List[TrueType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    notanumber: List[Notanumber] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    imaginaryi: List[Imaginaryi] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    exponentiale: List[Exponentiale] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    xref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    encoding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    definition_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "definitionURL",
            "type": "Attribute",
        },
    )
