# Abstract Argumentation Frameworks

This repository contains two variants of abstract argumentation methods using lattice structure written by me-- the first uses classical sets and the other uses probabilities for fuzzy set membership. Both methods aim to provide a fundamental mathematical structure for argumentation, with the probabilistic extension offering a way to take decisions under uncertainty (all arguments are not equally probable).

## What is AAF?

An Abstract Argumentation Framework (AAF) is a formal structure used in argumentation theory to model and analyze the relationships between arguments. It provides a way to represent a set of arguments and the conflicts between them, allowing for the evaluation of which arguments can be accepted, rejected, or left in an undecided state. An AAF consists of:

- Arguments: These are individual claims or propositions that can be in favor of or against something. For example, "A is true" could be an argument.

- Attack Relations: These represent the conflicts between arguments. If argument A attacks argument B, it means that if A is accepted, B should be rejected, and vice versa.

Formally, an AAF is defined as a tuple <***A***, ***R***>

where ***A*** is a set of arguments,

and ***R*** ⊆ ***A*** × ***A*** is a set of attack relations where each pair (A,B) ⊆ ***R*** means argument A attacks argument B.

## How does AAF work?

- Arguments and Attacks
  - Define a set of arguments and attack relationships.
  - In the probabilistic set up, also assign individual probabilities.

- Lattice Generation
  - The powerset of arguments forms the lattice.
  - Each subset represents a possible set of accepted arguments.
  - In the probabilistic set up, assign joint probabilities to each subset.

- Conflict-Free Check
  - A set of arguments is conflict-free if no argument in the set attacks another.
  - In the probabilistic set up, a set of arguments will also be considered conflict-free if their joint probability is below a conflict threshold. 

- Admissibility Check
  - A set is admissible if:
    - it is conflict-free.
    - it can defend its arguments against attacks.
  - In the probabilistic set up, check if there's no defender or if the strongest defender is weaker than the attacker (lower probability).

- Grounded Extension
  - The minimal admissible set is computed as the grounded extension.
