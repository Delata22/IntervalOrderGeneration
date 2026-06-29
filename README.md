# Generating Interval Orders

Exhaustive and efficient generation of all non-isomorphic **interval orders**.

This repository holds a technical report produced during research work at the
**LRE (Laboratoire de Recherche de l'EPITA)**.

- **Author:** Gurvan Estable
- **Supervisors:** Uli Fahrenberg, Hugo Bazille
- **Reference:** Technical Report no. 202507-techrep-estable, July 2025 (rev. 1.0)
- **Report:** [`202507-techrep-estable.pdf`](202507-techrep-estable.pdf)

## Abstract

The exhaustive and efficient generation of all non-isomorphic interval orders is
a major challenge. This report presents a generation method that solves this
problem by avoiding expensive isomorphism tests. Leveraging the *sparse
decomposition* of interval orders, we introduce a **canonical signature** that
uniquely represents each structure, regardless of element labels. This approach
lets us define *prototypes* — irreducible orders that serve as building blocks.
The main contribution is a **two-step algorithm** that first generates these
prototypes and then systematically derives all possible interval orders from
them. The method proves effective, enabling the generation of all orders **up to
14 elements**.

## Key ideas

- **Sparse decomposition** of interval orders into posets with interfaces (iposets).
- A **canonical signature** that identifies a structure independently of its
  element labels, removing the need for costly pairwise isomorphism tests.
- **Prototypes**: irreducible interval orders used as building blocks.
- A **two-step generation algorithm**: generate prototypes, then derive every
  interval order from them.

## Code

The implementation (Python, no external dependencies) lives alongside the report:

- `interval_orders/` — core library: prototype generation (`proto_generator.py`),
  matrix completion and order generation (`generator.py`), hat generation
  (`hat_generator.py`), bit helpers (`bin_utils.py`).
- `scripts/` — benchmarks and tests (`benchmark-*.py`, `test.py`).
- `tree_generation/` — full and subset generation experiments.

Run from the repository root, e.g.:

```bash
python -m scripts.test
```

## Keywords

poset, iposet, interval order, generation

## License

The technical report is distributed under the **GNU Free Documentation License**,
Version 1.2 or later (© LRE).
