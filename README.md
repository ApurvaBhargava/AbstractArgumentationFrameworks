# Abstract Argumentation Frameworks

This repository contains two variants of abstract argumentative frameworks using lattice structure written by me- the first uses classical sets and the other uses probabilities for fuzzy set membership. Both frameworks aim to provide flexible and scalable solutions for argumentation theory, with the probabilistic extension offering deeper insights into decision-making under ambiguity.

## What is AAF?

An Abstract Argumentation Framework (AAF) is a formal structure used in argumentation theory to model and analyze the relationships between arguments. It provides a way to represent a set of arguments and the conflicts between them, allowing for the evaluation of which arguments can be accepted, rejected, or left in an undecided state.

An AAF consists of:

Arguments: These are individual claims or propositions that can be in favor of or against something. For example, "A is true" could be an argument.

Attack Relations: These represent the conflicts between arguments. If argument A attacks argument B, it means that if A is accepted, B should be rejected, and vice versa. The attack relationship is often represented as a directed graph where an edge from A to B indicates that A attacks B.

Formally, an AAF is defined as a tuple <$\mathbb{A}$, $\mathbb{R}$>

where A is a set of arguments,

and $\mathbb{R}$ \subseteq A x  A is a set of attack relations where each pair (A,B) \subsetq $\mathbb{R}$ means that argument A attacks argument B

## How does AAF work?

Arguments and Attacks:

Define a set of arguments and attack relationships.
Example: arguments = {"A", "B", "C"} and attacks = [("A", "B"), ("B", "C")].

Lattice Generation:

The powerset of arguments forms the lattice.
Each subset represents a possible set of accepted arguments.

Conflict-Free Check:

A set of arguments is conflict-free if no argument in the set attacks another.

Admissibility Check:

A set is admissible if:
It is conflict-free.
It can defend its arguments against attacks.

Grounded Extension:

The minimal admissible set is computed as the grounded extension.