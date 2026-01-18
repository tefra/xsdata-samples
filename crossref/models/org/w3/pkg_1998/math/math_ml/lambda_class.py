from __future__ import annotations

from dataclasses import dataclass, field

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
    List,
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
class LambdaType:
    class Meta:
        name = "lambda.class"
        namespace = "http://www.w3.org/1998/Math/MathML"

    bvar: list[Bvar] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    domainofapplication: list[Domainofapplication] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    condition: list[Condition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    lowlimit: list[Lowlimit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    uplimit: list[Uplimit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    apply: Apply | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    bind: Bind | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ci: Ci | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cn: Cn | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    csymbol: Csymbol | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cbytes: Cbytes | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cerror: Cerror | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cs: Cs | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    share: Share | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    piecewise: Piecewise | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    declare: Declare | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    fn: Fn | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    reln: Reln | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    interval: Interval | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    moment: Moment | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    log: Log | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ln: Ln | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    image: Image | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    codomain: Codomain | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    domain: Domain | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ident: Ident | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    inverse: Inverse | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lambda_value: Lambda | None = field(
        default=None,
        metadata={
            "name": "lambda",
            "type": "Element",
        },
    )
    compose: Compose | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    quotient: Quotient | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    divide: Divide | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    minus: Minus | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    power: Power | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    rem: Rem | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    root: Root | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    factorial: Factorial | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    abs: Abs | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    conjugate: Conjugate | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arg: Arg | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    real: Real | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    imaginary: Imaginary | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    floor: Floor | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ceiling: Ceiling | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    exp: Exp | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    min: Min | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    max: Max | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lcm: Lcm | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    gcd: Gcd | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    times: Times | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    plus: Plus | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xor: Xor | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    or_value: Or | None = field(
        default=None,
        metadata={
            "name": "or",
            "type": "Element",
        },
    )
    and_value: And | None = field(
        default=None,
        metadata={
            "name": "and",
            "type": "Element",
        },
    )
    not_value: Not | None = field(
        default=None,
        metadata={
            "name": "not",
            "type": "Element",
        },
    )
    equivalent: Equivalent | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    implies: Implies | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    exists: Exists | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    forall: Forall | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    leq: Leq | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    geq: Geq | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lt: Lt | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    gt: Gt | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    eq: Eq | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tendsto: Tendsto | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    factorof: Factorof | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    approx: Approx | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    neq: Neq | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    int_value: Int | None = field(
        default=None,
        metadata={
            "name": "int",
            "type": "Element",
        },
    )
    diff: Diff | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    partialdiff: Partialdiff | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    laplacian: Laplacian | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    curl: Curl | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    grad: Grad | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    divergence: Divergence | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    list_value: List | None = field(
        default=None,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    set: Set | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cartesianproduct: Cartesianproduct | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    intersect: Intersect | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    union: UnionType | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    setdiff: Setdiff | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    notprsubset: Notprsubset | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    notsubset: Notsubset | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    notin: Notin | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    in_value: In | None = field(
        default=None,
        metadata={
            "name": "in",
            "type": "Element",
        },
    )
    prsubset: Prsubset | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    subset: Subset | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    card: Card | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sum: Sum | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    product: Product | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    limit: Limit | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arctanh: Arctanh | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arcsinh: Arcsinh | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arcsech: Arcsech | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arcsec: Arcsec | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arccsch: Arccsch | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arccsc: Arccsc | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arccoth: Arccoth | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arccot: Arccot | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arccosh: Arccosh | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arctan: Arctan | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arccos: Arccos | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arcsin: Arcsin | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    coth: Coth | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    csch: Csch | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sech: Sech | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tanh: Tanh | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cosh: Cosh | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sinh: Sinh | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cot: Cot | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    csc: Csc | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sec: Sec | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tan: Tan | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cos: Cos | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sin: Sin | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    mode: Mode | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    median: Median | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    variance: Variance | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sdev: Sdev | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    mean: Mean | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    matrixrow: Matrixrow | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    matrix: Matrix | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    vector: Vector | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    transpose: Transpose | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    determinant: Determinant | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    selector: Selector | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    outerproduct: Outerproduct | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    scalarproduct: Scalarproduct | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    vectorproduct: Vectorproduct | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    emptyset: Emptyset | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    primes: Primes | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    complexes: Complexes | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    naturalnumbers: Naturalnumbers | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    rationals: Rationals | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    reals: Reals | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    integers: Integers | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    infinity: Infinity | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    eulergamma: Eulergamma | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    pi: Pi | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    false: FalseType | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    true: TrueType | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    notanumber: Notanumber | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    imaginaryi: Imaginaryi | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    exponentiale: Exponentiale | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    xref: object | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: list[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        },
    )
    style: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    href: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other: object | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    encoding: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    definition_url: str | None = field(
        default=None,
        metadata={
            "name": "definitionURL",
            "type": "Attribute",
        },
    )
