# Elementary proofs of Dumont–Sidorov–Thomas growth bounds

## Mathematics

Haobo Ma — ChronoAI Pte Ltd, Singapore  
Wenlin Zhang — National University of Singapore; ChronoAI Pte Ltd, Singapore

Let `b(k,ell,n)` count finite radix-`ell` representations of `n` with
digits from zero through `k`, counted once independently of trailing zeros.
The note proves:

- The least bound with upper logarithmic exponent at least `r-1` is
  `ell^r-1`, for every integer `r>=2`. A two-digit bound gives a uniform
  strictly smaller exponent at every smaller bound. Thus the first
  linear-maximum bound is `ell^2-1`, answering Calkin and Wilf's question.
- For `2<=q<=ell` and `(q-1)(ell+1)<=k<=q*ell-1`, the upper exponent is
  `log(q)/log(ell)`. Intervals containing adjacent bounds answer Coons's
  strict-adjacency question negatively.
- The lower exponent is zero for `ell-1<=k<=2*ell-2`. At every bound
  `a*ell-1`, both exponents equal `log(a)/log(ell)`, by an exact summatory
  identity. This also supplies the corrected growth exponent for the
  formula printed as Coons's Theorem 4.

The plateau and general summatory identity are prior results of Dumont,
Sidorov and Thomas (1999), Propositions 6.8–6.9:
https://doi.org/10.4064/aa-88-4-371-396.
Protasov (2000) gives related extrema and exponents; Feng, Liardet and
Thomas (2014), page 50, explicitly record the singleton witness for zero
lower exponents. Baker's 2015 thesis gives the full convergence criterion,
with its converse proof credited to Stephan Wagner. De Castro and
collaborators (2018) give the binary carry bijection. The same linear-gap
exponent appears in the later IRSI note, displaying an update of
11 November 2026: https://irsi.ai/notes/calkin-wilf-cw2/.
The note presents elementary reproofs and applications, not a first
settlement of the previously published statements.
Every stated infinite conclusion has a written proof or an identified
prior theorem; finite comparisons are supplementary.

The primary posing source is Michael Coons, *The Calkin–Wilf problems on
ell-ary partition functions*, arXiv:2611.08109v1, Section 1, CW2, and
Section 3, last paragraph, final display and following sentence:
https://arxiv.org/html/2611.08109v1.
The original Calkin–Wilf question is Section 10, printed page 18,
Question 2, of their author-hosted preprint:
https://www.math.clemson.edu/~calkin/Papers/calkin_wilf_binary_partitions_unpublished.pdf.

## Source and companion files

- `note.tex`: complete LaTeX source with embedded bibliography.
- `note.pdf`: companion mathematical note.
- `verify.py`: standard-library-only exact-integer checker.
- `verification.json`: expected checker output, including all ranges.
- `metadata.json`: authors, license, mathematical scope, and source links.
- `SHA256SUMS`: hashes of the source-package members.

Build the extracted source using Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively, with the packages listed in `note.tex` installed:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

The bibliography is embedded, so a separate BibTeX pass is unnecessary.
The PDF is supplied separately from the source archive.

Run the checker with Python 3.10 or later:

```sh
python3 verify.py > verification-local.json
python3 -c 'import json; assert json.load(open("verification-local.json")) == json.load(open("verification.json"))'
```

The checker compares generating-product coefficients with an independent
units-digit recurrence for radices 2 through 10. The main coefficient
range is `0<=n<=5000`; higher thresholds `r=3,4` also use `0<=n<=2000`.
It checks quotient upper bounds, attaining carry constructions, two-digit
branching bounds, critical linear identities, unique-digit inputs, and
the general summatory identity, including multipliers exceeding the radix.
The finite computations establish exactly those finite instances, not
the limiting or universal statements.

## Pinned Lean statements

The source file is
https://github.com/the-omega-institute/trureturing/blob/87004d7eb03533d5078ed293778a5b22c8d99aa2/D5/S1/Digit/CoonsAdjacentGrowthRefutation.lean.
Its namespace is `D5.S1.Digit.CoonsAdjacentGrowthRefutation`.

- `count_upper`: radix four, `k<=6`, `n<4^(m+1)`, count at most `2^m`.
- `count_repunit`: radix four, `5<=k<=6`, repunit count exactly `2^m`.
- `tail_supremum`: radix four, `5<=k<=6`, every natural tail has supremum `1/2`.
- `exponent_eq_half`: radix four, `5<=k<=6`, upper exponent `1/2`.
- `result`: negation of the universal strict upper-exponent comparison.

The thresholds, larger plateaux, all lower exponents, and general
summatory identity have the written proofs in `note.tex`; they are
not statements of those pinned declarations.

## License

Copyright 2026 Haobo Ma and Wenlin Zhang.
CC BY 4.0 (`cc-by-4.0`): https://creativecommons.org/licenses/by/4.0/.
