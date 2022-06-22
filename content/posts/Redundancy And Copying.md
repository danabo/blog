---
date: 2021-06-23
lastmod: '2022-04-15T02:06:23-07:00'
tags:
- information
- physics
title: Redundancy And Copying
---








Information in our universe can be copied, as evidenced by the ubiquitous copying of computer memory, books and paper everywhere, and our ability to non-destructively see and hear everything around us. Information is **copied** (or [cloned](https://en.wikipedia.org/wiki/No-cloning_theorem)) when the state of one system, the target, becomes correlated with the state of another system, the source, without destructively altering the state of the source. Information is **moved**, on the other hand, when the state of the source is transferred to the target in a way that leaves the source's state erased or overwritten with something else. In general, information copying between two systems is a special case of increasing information redundancy between two systems. <!--more-->

$$
\\newcommand{\\0}{\\mathrm{false}}
\\newcommand{\\1}{\\mathrm{true}}
\\newcommand{\\mb}{\\mathbb}
\\newcommand{\\mc}{\\mathcal}
\\newcommand{\\mf}{\\mathfrak}
\\newcommand{\\and}{\\wedge}
\\newcommand{\\or}{\\vee}
\\newcommand{\\n}{\\bar}
\\newcommand{\\xor}{\\oplus}
\\newcommand{\\es}{\\emptyset}
\\newcommand{\\a}{\\alpha}
\\newcommand{\\b}{\\beta}
\\newcommand{\\s}{\\sigma}
\\newcommand{\\t}{\\tau}
\\newcommand{\\T}{\\Theta}
\\newcommand{\\D}{\\Delta}
\\newcommand{\\o}{\\omega}
\\newcommand{\\O}{\\Omega}
\\newcommand{\\x}{\\xi}
\\newcommand{\\z}{\\zeta}
\\newcommand{\\fa}{\\forall}
\\newcommand{\\ex}{\\exists}
\\newcommand{\\X}{\\mc{X}}
\\newcommand{\\Y}{\\mc{Y}}
\\newcommand{\\Z}{\\mc{Z}}
\\newcommand{\\P}{\\Psi}
\\newcommand{\\y}{\\psi}
\\newcommand{\\p}{\\phi}
\\newcommand{\\l}{\\lambda}
\\newcommand{\\B}{\\mb{B}}
\\newcommand{\\m}{\\times}
\\newcommand{\\N}{\\mb{N}}
\\newcommand{\\R}{\\mb{R}}
\\newcommand{\\I}{\\mb{I}}
\\newcommand{\\H}{\\mb{H}}
\\newcommand{\\e}{\\varepsilon}
\\newcommand{\\Env}{\\mf{E}}
\\newcommand{\\expt}\[2\]{\\mb{E}\_{#1}\\left\[#2\\right\]}
\\newcommand{\\set}\[1\]{\\left\\{#1\\right\\}}
\\newcommand{\\par}\[1\]{\\left(#1\\right)}
\\newcommand{\\vtup}\[1\]{\\left\\langle#1\\right\\rangle}
\\newcommand{\\abs}\[1\]{\\left\\lvert#1\\right\\rvert}
\\newcommand{\\inv}\[1\]{{#1}^{-1}}
\\newcommand{\\ceil}\[1\]{\\left\\lceil#1\\right\\rceil}
\\newcommand{\\dom}\[1\]{\_{\\mid #1}}
\\newcommand{\\df}{\\overset{\\mathrm{def}}{=}}
\\newcommand{\\M}{\\mc{M}}
\\newcommand{\\up}\[1\]{^{(#1)}}
\\newcommand{\\Dt}{{\\Delta t}}
\\newcommand{\\tr}{\\rightarrowtail}
\\newcommand{\\tx}{\\prec}
\\newcommand{\\qed}{\\ \\ \\blacksquare}
\\newcommand{\\c}{\\overline}
\\newcommand{\\A}{\\mf{A}}
\\newcommand{\\cA}{\\c{\\mf{A}}}
\\newcommand{\\fB}{\\mf{B}}
\\newcommand{\\dg}{\\dagger}
\\newcommand{\\do}\[2\]{\\underset{#1\\leadsto #2}{\\mathrm{do}}}
\\newcommand{\\lgfr}\[2\]{\\lg\\par{\\frac{#1}{#2}}}
\\newcommand{\\sys}\[2\]{\\left\[#2\\right\]\_{#1}}
$$

In {{< locallink "Physical Information" >}}, I defined conservation of information as the property that given some set $R \\subseteq \\O$, the time-evolved set $\\t\_\\Dt(R)$ is fully determined, and given $\\t\_\\Dt(R)$, the original set $R$ is fully determined. This is only true for all $R$ if $\\t\_\\Dt$ is a bijection. All of our theories of physics have bijective time-evolution, and so it would be reasonable to assume that information is conserved in our universe. That is to say, information is never lost through time-evolution.

The redundancy between two systems with state spaces $\\mf{A}$ and $\\mf{B}$ (as partitions of $\\O$) is quantified by their mutual information 

$$\\I(\\mf{A}, \\mf{B}) = \\mb{E}\_{a\\in\\mf{A}, b\\in\\mf{B}}\\Big\[i(a, b)\\Big\]\\,,$$

where $i(a,b) = \\lgfr{\\mu(a\\cap b)\\mu(\\O)}{\\mu(a)\\mu(b)}$ is the pointwise mutual information between $a$ and $b$ as calculated with the provided measure $\\mu$ (see {{< locallink "Physical Information" "mutual-information" >}} for details), and $\\O = \\bigcup\\mf{A} = \\bigcup\\mf{B}$ is the domain. Their mutual information $\\I(\\mf{A}, \\mf{B})$ is 0 when $\\mf{A}$ and $\\mf{B}$ are orthogonal. Since in my formulation, the state spaces of systems don't change over time, i.e. $\\mf{A}, \\mf{B}$ are fixed through time, then redundancy between systems does not change. If two systems are defined to be orthogonal, they remain orthogonal.

Given the constant redundancy between systems through time, it is surprising that information redundancy appears to change over time in our universe. Furthermore, you might naively conclude that redundancy cannot change over time in a universe that conserves information. How can changing information redundancy coexist with conservation of information?

It is interesting to note that in quantum physics information copying is not possible (see the [no-cloning theorem](https://en.wikipedia.org/wiki/No-cloning_theorem)), i.e. quantum information can only be moved around but not duplicated. If our universe is fundamentally quantum and information cannot be copied, then again, why does information appear to be copied everywhere? The answer lies in the distinction between quantum information, which cannot be copied, and classical information, which can be (this is out of scope for this post, but I might delve into quantum information theory in future posts).




# Intuition Pumps
Information can be copied under bijective time evolution if we restrict ourselves to a subset of the state space. That is to say, some initial states of the universe appear to time-evolve into redundant states, while other initial states, by necessity do not (for time-evolution to be bijective). Let's get a feel for how information copying under bijective time-evolution works by looking at a few toy universes in which information gets copied between systems over time.

For simplicity, I'll work with binary systems (two-state systems). We can create bigger systems by grouping many binary systems together into super-systems (each binary system is a sub-system). That is to say, the state spaces of these super-systems are binary tuples.

Formally, let $\\B = \\set{0,1}$ be the binary alphabet.
When I define system A to have the state space $A = \\B^k$, then a state of system A is $a \\in A$ where $a$ is a binary tuple. For example, $a = 001010\\dots0$.
When I define the state spaces for a few systems, say $A = \\B^n,\\ B=\\B^m,\\ C=\\B^p$, then the state space of the universe is the Cartesian product, $\\O = A\\times B\\times C$, and the state of the universe is the state tuple $\\o = (a,b,c) \\in \\O$, which can also regarded as one big binary tuple of length $n+m+p$.

Regarding time-evolution, here I'll work in discrete time, i.e. $t \\in \\mb{Z}$.
Then the family of bijective time-evolution functions on $\\O$ form the discrete group, $(\\set{\\t\_\\Dt\\mid t\\in\\mb{Z}},\\circ)$, where $\\t\_1$ is the group generator, i.e.

$$
\\t\_t = \\begin{cases}
    \\underbrace{\\t\_1\\circ\\dots\\circ\\t\_1}\_{t\\ \\mathrm{times}} & t > 0 \\\\
    \\o\\mapsto\\o & t = 0 \\\\
    \\underbrace{\\t^{-1}\_1\\circ\\dots\\circ\\t^{-1}\_1}\_{t\\ \\mathrm{times}} & t < 0 
\\end{cases}
$$

Thus, it's sufficient to define $\\t\_1$ in order to specify the entire family $\\set{\\t\_\\Dt\\mid t\\in\\mb{Z}}$.

Let's define some notation that will make it easy to define time-evolution functions.
For binary values $\\alpha,\\beta\\in\\B$,
- $\\alpha\\ \\beta \\in \\B^2$ is tuple concatenation
- $\\n{\\beta}$ is the NOT operation
- $\\alpha\\cdot \\beta$ is the AND operation 
- $\\alpha + \\beta$ is the OR operation 
- $\\alpha \\xor \\beta$ is the XOR operation

For binary $k$-tuples $a, b \\in \\B^k$,
- $a\_1$ is the first bit
- $a\_k$ is the last bit
- $a\_{i:j}$ is the slice $a\_i\\ a\_{i+1}\\ \\dots\\ a\_{j-1}\\ a\_j$
- $a\_{i:j}\\ b\_{k:\\ell}$ is tuple concatenation

## Simple Copier - style 1

Let's take a look at the simplest possible copier, where the state of one system is copied to the state of another system in one time-step. There are actually two different copiers of this size. I'll give them both.

We have two systems, A and B, with state spaces
$A = \\B$
$B = \\B$

The one-step time-evolution function is defined as 

$$
\\begin{aligned}
\\t\_1(a, b) &= \\begin{cases}(a,a) & b = 0 \\\\ (\\n{a}, a) & b = 1\\end{cases} \\\\
    &= (a \\xor b,\\ a)
\\end{aligned}
$$

 If $b=0$ initially, then $\\t\_1$ copies A's state to B's state. If $b=1$ initially, then $\\t\_1$ also copies A's state to B's state and additionally flips A's state.

To sanity check that this is indeed a bijection, here is its inverse:

$$
\\t\_{-1}(a, b) = (b,\\ a\\xor b)
$$

And here is the full I/O table for this function

$(0,0)\\mapsto(0,0)$
$(0,1)\\mapsto(1,0)$
$(1,0)\\mapsto(1,1)$
$(1,1)\\mapsto(0,1)$





Bijective time-evolution on finite state spaces necessarily creates cycles. Here are the cycles for $\\t\_1$:
$(0,0) \\to (0,0)$
$(0,1) \\to (1,0) \\to (1,1) \\to (0,1)$

## Simple Copier - style 2

This is another simplest copier that is almost the same as the first, save one difference.

$A = \\B$
$B = \\B$

$$
\\t\_1(a, b) = (a,\\ a\\xor b)
$$

$$
\\t\_{-1}(a, b) = (a,\\ a\\xor b)
$$

(This function is it's own inverse.)

The full I/O table for this function:

$(0,0)\\mapsto(0,0)$
$(0,1)\\mapsto(0,1)$
$(1,0)\\mapsto(1,1)$
$(1,1)\\mapsto(1,0)$





Bijective time-evolution on finite state spaces necessarily creates cycles. Here are the cycles for $\\t\_1$:
$(0,0) \\to (0,0)$
$(0,1) \\to (0,1)$
$(1,0) \\to (1,1) \\to (1,0)$

## Repeating Copier

This universe operates on the same principle as our simplest copier, but scaled up. Now system A is a $k$-tuple of binary states, and the second system is called E (for environment), which is an $m$-tuple presumed to be much bigger than A, i.e. $m >> k$. System A will continuously duplicate its state into the environment until the environment "fills up".

Define this universe:

$A  = \\B^k$
$E = \\B^m$

$$
\\t\_1(a,e) = ((a\_{k}\\xor e\_{m})\\ a\_{1:k-1},\\ a\_{k}\\ e\_{1:m-1})
$$

$$
\\t\_{-1}(a,e) = (a\_{2:k}\\ e\_1,\\ e\_{2:m}\\ (a\_1\\xor e\_1))
$$

Here's an example of a time evolution, where $k=4$ and $m=8$, and the initial state of the universe is $(a,\\ e) = (1011,\\ 00000000)$:

| A  | E      |
|----|--------|
|1011|00000000|
|1101|10000000|
|1110|11000000|
|0111|01100000|
|1011|10110000|
|1101|11011000|
|1110|11101100|
|0111|01110110|
|1011|10111011|
|0101|11011101|
|0010|11101110|
|0001|01110111|
|0000|10111011|
|1000|00111011|
|1100|00011101|
|1110|00001110|
|0111|00000111|
|0011|10000011|

As we can see, system A keeps copying its state into system E so long as the last bit of E's state remains zero. When that ceases to be true, system A's state is corrupted, and this time-evolution is no longer performing a copy operation, but a move operation, which is destructive.


If the environment is initialized to be "empty", i.e. contain all zeros, and $m$ is incredibly large, then system A will copy itself for *virtually* forever. We do not know whether our own universe has boundaries beyond what we can observe. Though empty space does appear to be empty, we do not know if it may fill up on long enough time scales, or if everything will continue to spread out forever. That is the difference between a finite and infinite $m$ in this example. (Though technically $m$ cannot be infinite here because then there would not be a last bit. I define some infinite environments below which fix this issue.)


## Mover

In contrast to copiers, movers do not preserve the state of system A. Here, we have two systems which swap their respective states over time.

$A = B = \\B^k$

$$
\\t\_1(a, b) = (a\_{2:k}\\ b\_1,\\ b\_{2:k}\\ a\_1)
$$

$$
\\t\_{-1}(a,b) = (b\_k\\ a\_{1:k-1},\\ a\_k\\ b\_{1:k-1})
$$

Example:


| A  | B  |
|----|----|
|0000|1011|
|0001|0110|
|0010|1100|
|0101|1000|
|1011|0000|
|0110|0001|
|1100|0010|
|1000|0101|
|0000|1011|

## Scrambler

$A = B = \\set{0,\\dots,k-1}$ are integer sets where $k$ is odd.

$$
\\t\_1(a,b) = \\Big(a+b \\pmod{k},\\ b-a \\pmod{k}\\Big)
$$

$$
\\t\_{-1}(a,b) = \\Big(\\frac{1}{2}(a-b) \\pmod{k},\\ \\frac{1}{2}(a+b) \\pmod{k}\\Big)
$$

(Addition and subtraction here mean integer arithmetic, rather than boolean operations.)

For example when $k=3$, the I/O table is

| $(a,b)$ | $\\t\_1(a,b)$ |
| ---- | ---- |
| $(0,0)$ | $(0,0)$ |
| $(0,1)$ | $(1,1)$ |
| $(0,2)$ | $(2,2)$ |
| $(1,0)$ | $(1,2)$ |
| $(1,1)$ | $(2,0)$ |
| $(1,2)$ | $(0,1)$ |
| $(2,0)$ | $(2,1)$ |
| $(2,1)$ | $(0,2)$ |
| $(2,2)$ | $(1,0)$ |

We will see later why I call this a scrambler.

## Infinite repeating copier - style 1
Here is an example of a copier with an infinite environment. I define a third system, X, which stores a "control bit". When the state of X is 0, forward time-evolution performs copy operations. Otherwise, something else happens. This control bit is needed to maintain $\\t\_1$ as a bijection.

$X = \\B$
$A  = \\B^k$
$E = \\B^\\infty$

$$
\\begin{aligned}
\\t\_1(x, a, e) &= \\begin{cases}
    (0,\\ a\_{k}\\ a\_{1:k-1},\\ a\_k\\ e) & x = 0 \\\\
    (0,\\ a,\\ e) & x = 1 \\and a\_1 \\neq e\_1 \\\\
    (1,\\ a\_{2:k}\\ a\_1,\\ e\_{2:\\infty})  & x = 1 \\and a\_1 = e\_1
\\end{cases}
\\end{aligned}
$$

$$
\\begin{aligned}
\\t\_{-1}(x, a, e) &= \\begin{cases}
    (0,\\ a\_{2:k}\\ a\_1,\\ e\_{2:\\infty}) & x = 0  \\and a\_1 = e\_1 \\\\
    (1,\\ a,\\ e) & x = 0 \\and a\_1 \\neq e\_1 \\\\
    (1,\\ a\_{k}\\ a\_{1:k-1},\\ a\_k\\ e)  & x = 1
\\end{cases}
\\end{aligned}
$$

We can see that in reverse time, the universe performs copy operations when the state of X is one. Thus in forward time, when $x=1$, an "uncopy" operation is performed. This can be thought of as reversing a copy operation, but if there was no previous copy and systems A and E just happen to be redundant in the right way, then this time-evolution is simply making A and E less redundant.


Examples:

|X| A  | E      |
|-|----|--------|
|0|1011|0000000…|
|0|1101|1000000…|
|0|1110|1100000…|
|0|0111|0110000…|
|0|1011|1011000…|
|0|1101|1101100…|
|0|1110|1110110…|
|0|0111|0111011…|
|0|1011|1011101…|


|X| A  | E      |
|-|----|--------|
|1|1011|1011000…|
|1|0111|0110000…|
|1|1110|1100000…|
|1|1101|1000000…|
|1|1011|0000000…|
|0|1011|0000000…|
|0|1101|1000000…|
|0|1110|1100000…|
|0|0111|0110000…|
|0|1011|1011000…|

To recap:
X is a switch that determines the "direction" of this system. 
$x=0$ means copy A to E
$x=1$ means "undo" the copy from A to E
If $x=1$ and $a\_1\\neq e\_1$, then an undo copy cannot be performed, and the state of X is flipped (the operating mode is changed from uncopy to copy).

The point of having two modes of operation is so that any combined state of A and E has a history that produces it, i.e. that $\\t\_1$ is surjective. If A and E are redundant in the right way, then their immediate history is a sequence of copy steps. However, if they are not redundant (in the right way), then their history is a sequence of uncopy steps which just happened to culminate with the current states.

## Infinite repeating copier - style 2

In this universe, the environment is infinite from the left and the right, i.e. states are $e\_{-\\infty:\\infty} \\in E$. I'll break up the environment into two halves, $E\_+$ containing indices $1$ to $\\infty$, and $E\_-$ containing indices $-\\infty$ to $0$.

$A  = \\B^k$
$E\_+ = \\B^\\infty$
$E\_- = \\B^\\infty$

$$
\\t\_1(e\_{-\\infty:0}, a, e\_{1:\\infty}) = (e\_{-\\infty:-1},\\ (e\_0\\xor a\_k)\\ a\_{1:k-1},\\ a\_k\\ e\_{1:\\infty})
$$

$$
\\t\_{-1}(e\_{-\\infty:0}, a, e\_{1:\\infty}) = (e\_{-\\infty:0}\\ (e\_1\\xor a\_1),\\ a\_{2:k}\\ e\_1,\\ e\_{2:\\infty})
$$

This time-evolution passes the left-side environment through A and copies A into the right-side environment. So long as the left-side environment's last bit is always zero, system A's state is preserved. Otherwise, system A is corrupted.

Examples:

| $E\_-$  | $A$| $E\_+$  |
|--------|----|--------|
|…0000000|1011|0000000…|
|…0000000|1101|1000000…|
|…0000000|1110|1100000…|
|…0000000|0111|0110000…|
|…0000000|1011|1011000…|
|…0000000|1101|1101100…|
|…0000000|1110|1110110…|
|…0000000|0111|0111011…|


| $E\_-$  | $A$| $E\_+$  |
|--------|----|--------|
|…1110111|1011|0000000…|
|…1111011|0101|1000000…|
|…1111101|0010|1100000…|
|…1111110|1001|0110000…|
|…1111111|1100|1011000…|
|…1111111|1110|0101100…|
|…1111111|1111|0010110…|
|…1111111|0111|1001011…|

# Definition of copying

In all of the "copier" examples above, what about their time evolution makes them copiers? What exactly do we mean when we say that they copy the information contained in system A to system E?

Ultimately, when information has been copied from A to E, then we can look at the state of E to gain information about the state of A. That implies the state spaces of A and E have become redundant (given that they were not to begin with). To understand how these systems can change in redundancy over time without actually altering definitions of their state spaces over time, let's go through the simple copier example again.

## Simple copier revisited

Recall that $\\t\_1$ is fully specified by this list of mappings:
$00\\mapsto00$
$01\\mapsto10$
$10\\mapsto11$
$11\\mapsto01$

I'm using binary strings in place of explicit tuples of digits for visual simplicity. I'll also start working in the partition-as-state-space framework (see {{< locallink "Physical Information" "information-theory-of-systems" >}}).

Let $\\O = \\set{00,01,10,11}$ be the universe's state space.
Let $\\mf{A} = \\set{\\set{00, 01}, \\set{10,11}}$ be the state space of system A. So A's state is the first bit.
Let $\\mf{B} = \\set{\\set{00, 10}, \\set{01, 11}}$ be the state space of system B. So B's state is the second bit.
Any state $a\\in\\mf{A}$ is the set of all states in $\\O$ for which system A is in the same state $a$, and likewise for $b\\in\\mf{B}$.

Notice that A and B are orthogonal, i.e.

$$
\\begin{aligned}
\\I(\\mf{A}, \\mf{B}) &= \\sum\_{a\\in\\mf{A}}\\sum\_{b\\in\\mf{B}} \\frac{\\abs{a\\cap b}}{\\abs{\\O}}i(a, b) \\\\
    &= \\sum\_{a\\in\\mf{A}}\\sum\_{b\\in\\mf{B}} \\frac{\\abs{a\\cap b}}{\\abs{\\O}}\\lgfr{\\abs{a\\cap b}\\abs{\\O}}{\\abs{a}\\abs{b}} \\\\
    &= \\sum\_{a\\in\\mf{A}}\\sum\_{b\\in\\mf{B}} \\frac{1}{4}\\lgfr{1\\cdot 4}{2\\cdot 2} \\\\
    &= 0\\,,
\\end{aligned}
$$

where $\\O = \\bigcup\\mf{A} = \\bigcup\\mf{B}$.

(Here I am using the counting measure, $\\mu(R) = \\abs{R}$ for $R\\subseteq\\O$).

This is a way of quantifying how decoupled the two systems are, where 0 is maximum decoupling, meaning that A can be in any state and B can be in any state.

I believe that what intuitively makes this universe a copier is that if we vary A's initial state, then the state of both A and B vary together later in time. To see what I mean, choose the intervention set $J = \\set{00, 10}$, which varies A's state while keeping B's state at zero (this is just a state of B). The effect set one step into the future is $\\t\_1(J) = \\set{00, 11}$. In our representation of A's state as the first bit and B's state as the second bit, all the outcomes in the effect set are ones where A and B have equal states, i.e. $00$ and $11$.

Consider the state spaces of A and B restricted to the sets $J$ and $\\t\_1(J)$:
$\\mf{A}\\dom{J} = \\set{\\set{00}, \\set{10}},\\ \\mf{B}\\dom{J} = \\set{\\set{00, 10}, \\set{}}$.
$\\mf{A}\\dom{\\t\_1(J)} = \\mf{B}\\dom{\\t\_1(J)} = \\set{\\set{00}, \\set{11}}$.

(For any partition $\\mf{P}$ and set $R$, the notation $\\mf{P}\\dom{R} \\df \\set{p \\cap R \\mid p \\in \\mf{P}}$ is the sub-partition restricted to the domain $R$.)

How redundant are these state spaces? It is straight forward to calculate:
$\\I(\\mf{A}\\dom{J}, \\mf{B}\\dom{J}) = \\I(\\mf{A}, \\mf{B} \\mid J) = 0$.
$\\I(\\mf{A}\\dom{\\t\_1(J)}, \\mf{B}\\dom{\\t\_1(J)}) = \\I(\\mf{A}, \\mf{B} \\mid \\t\_1(J)) = \\H(\\mf{A}\\dom{\\t\_1(J)}) = 1$.


($\\I(\\mf{A}, \\mf{B} \\mid R) = \\I(\\mf{A}\\dom{R}, \\mf{B}\\dom{R})$ because $\\O$ in $\\I(\\cdot, \\cdot)$ is determined by the arguments, i.e. $\\O = \\bigcup\\mf{A}\\dom{R} = \\bigcup\\mf{B}\\dom{R} = R$.)


An example of calculating conditional mutual information:

$$
\\begin{aligned}
\\I(\\mf{A}, \\mf{B} \\mid J) &= \\sum\_{a\\in\\mf{A}}\\sum\_{b\\in\\mf{B}} \\frac{\\abs{a\\cap b\\cap J}}{\\abs{J}}i(a, b \\mid J) \\\\
    &= \\sum\_{a\\in\\mf{A}}\\sum\_{b\\in\\mf{B}} \\frac{\\abs{a\\cap b\\cap J}}{\\abs{J}}\\lgfr{\\abs{a\\cap b\\cap J}\\abs{J}}{\\abs{a\\cap J}\\abs{b\\cap J}} \\\\
    &= \\frac{1}{2}\\lgfr{1\\cdot 2}{1\\cdot 2} +  \\frac{1}{2}\\lgfr{1\\cdot 2}{1\\cdot 2} + 0 + 0 \\\\
    &= 0\\,.
\\end{aligned}
$$




We can see that the redundancy has increased from time 0 to time 1.
At time 0, system B can only be in the state $\\set{00, 10}$, while system A can be in either state $\\set{00}$ or $\\set{10}$. In this sense, A's state is independent of B.
Meanwhile, at time 1, if A is in state $\\set{00}$ then B must be in state $\\set{00}$, and if A is in state $\\set{11}$ then B must be in state $\\set{11}$. This is maximal redundancy. Hence, system A's state is duplicated in system B.

$\\t\_1$ copies the state of A to B, but information is conserved overall. This apparent contradiction is explained by the assumption that $\\O$ is restricted to $J$. Though $\\t\_1$ is bijective on $\\O$, the image $\\t\_1(J)$ does not equal $J$.

### Uncopying

Because $\\t\_1$ is cyclic, the universe must eventually return to its initial state. That means any copying done will eventually be undone. We can see this if we compute two-step time-evolution:

$J = \\set{00, 10}$ as before.
$\\t\_1(J) = \\set{00, 11}$
$\\t\_2(J) = \\set{00, 01}$
==> $\\mf{A}\\dom{\\t\_2(J)} = \\set{\\set{00, 01}, \\set{}},\\ \\mf{B}\\dom{\\t\_2(J)} = \\set{\\set{00}, \\set{01}}$
$\\I(\\mf{A}\\dom{\\t\_2(R)}, \\mf{B}\\dom{\\t\_2(R)}) = \\I(\\mf{A}, \\mf{B} \\mid \\t\_2(R)) = 0$

So $\\I(\\mf{A}, \\mf{B} \\mid \\t\_2(R)) - \\I(\\mf{A}, \\mf{B} \\mid \\t\_1(R)) = -1$.
Time-step 1 to 2 "uncopies".

### Relativity of redundancy

The analysis above uses the intervention set $J$ that varies system A. What if we use the intervention set that varies system B? 

Let $J = \\set{00, 01}$, which varies system B while holding system A fixed. This intervention set gives us the causal effect of system B from system A's perspective. Then we have
$\\t\_1(J) = \\set{00, 10}$.
$\\mf{A}\\dom{J} = \\set{\\set{00, 01}, \\set{}},\\ \\mf{B}\\dom{J} = \\set{\\set{00}, \\set{01}}$.
$\\mf{A}\\dom{\\t\_1(J)} = \\set{\\set{00}, \\set{10}}$.
$\\mf{B}\\dom{\\t\_1(J)} = \\set{\\set{00, 10}, \\set{}}$.
Thus $\\I(\\mf{A}, \\mf{B} \\mid J) = \\I(\\mf{A}, \\mf{B} \\mid \\t\_1(J)) = 0$.

Now it appears that the redundancy between A and B doesn't change over time! In fact, from A's perspective, information is being moved from A to B (but not duplicated), as evidenced by $\\I(\\mf{B}, \\t\_1(J)) = 1$, which is maximal.

So from A's perspective information is being moved to B (while also moving B to A), and simultaneously from B's perspective, information is being copied to B (destroying B's initial state). How peculiar.

## Copying vs redundancy

In general, I define the **redundancy** between $\\A$ and $\\fB$ due to domain restriction $J\\subseteq\\O$ as

$$
\\rho \\df \\I(\\mf{A}, \\mf{B} \\mid J)\\,,
$$

(rho for "redundancy") and the **change in redundancy** due to domain restriction $J \\subseteq \\O$ over time period $\\Dt$ as

$$
\\D\\rho = \\I(\\mf{A}, \\mf{B} \\mid \\t\_\\Dt(J)) - \\I(\\mf{A}, \\mf{B} \\mid J)\\,.
$$

If $\\D\\rho > 0$ then redundancy between systems A and B has increased in the time interval $\\Dt$. Likewise, if $\\D\\rho < 0$ then redundancy has decreased, and if $\\D\\rho = 0$ there is no change in redundancy.

For arbitrary systems A and B, I say that information has been copied from system A to system B in the time interval $\\Dt$ when system A (in the past) causally effects both system A in the future and system B in the future. Formally, let $J$ be an intervention set varying the state of system A while holding system A's environment fixed, i.e. $J \\in \\cA$ where $\\cA$ is a partition complement of A. Then system A has copied some of its information to system B iff

$$
\\H(\\A \\mid \\t\_\\Dt(J)) > 0\\quad\\mathrm{and}\\quad\\H(\\fB \\mid \\t\_\\Dt(J)) > 0\\,.
$$

Recall from {{< locallink "Causality And Information" "effect-on" >}}, that $\\H(\\A \\mid \\t\_\\Dt(J))$ is the quantity of causal effect that system A has on system A in the future, and $\\H(\\fB \\mid \\t\_\\Dt(J))$ is the quantity of causal effect that system A has on system B in the future (assuming that $J$ varies system A).

Using the identities

$$
\\H(\\A\\otimes\\fB \\mid \\t\_\\Dt(J)) = \\H(\\A \\mid \\t\_\\Dt(J)) + \\H(\\fB \\mid \\t\_\\Dt(J)) - \\I(\\A,\\fB \\mid \\t\_\\Dt(J))
$$

(This is just one way of defining conditional mutual information, e.g. [Wikipedia](https://en.wikipedia.org/wiki/Conditional_mutual_information#Some_identities).)

and

$$
\\I(\\A\\otimes\\mf{B}, \\t\_\\Dt(J)) = \\I(\\A, \\t\_\\Dt(J)) + \\I(\\mf{B}, \\t\_\\Dt(J)) + \\I(\\A, \\mf{B} \\mid \\t\_\\Dt(J)) - \\I(\\A, \\mf{B})
$$

(see {{< locallink "Physical Information" "general-case" >}})

we see that for $\\H(\\A \\mid \\t\_\\Dt(J)) + \\H(\\fB \\mid \\t\_\\Dt(J)) > \\H(\\A\\otimes\\fB \\mid \\t\_\\Dt(J))$ to be the case then $\\I(\\A,\\fB \\mid \\t\_\\Dt(J))$ must be non-zero. Thus, for system A to have a large causal effect on both system A and system B (in the future), there needs to be redundancy between A and B. We also see that  $\\I(\\A, \\mf{B} \\mid \\t\_\\Dt(J))$ is bounded above by $\\I(\\A\\otimes\\mf{B}, \\t\_\\Dt(J)) + \\I(\\A, \\mf{B})$. This puts a limit on how much information redundancy there can be, and thus how much information can be copied.

## Scrambler revisited

Given system A and its environment, with respective state spaces $\\A, \\cA$, and respective intervention sets $J^\\dg \\in \\cA$ (varying system A) and $J \\in \\A$ (varying the environment),
is there any necessary relationship between $\\I(\\A, \\cA \\mid \\t\_\\Dt(J))$ and $\\I(\\A, \\cA \\mid \\t\_\\Dt(J^\\dg))$? That is to say, if system A copies its information to the environment, then can the environment also copy its information to system A?

It would be easy to think the answer is no. Copying requires duplication. If system A's state is copied to the environment, then its own state should remain in tact (otherwise this is merely information moving). For the environment to copy information to A, the state of A would need to be overwritten. Here is the apparent contradiction.

I'll now construct a setup where a system and its environment simultaneously copy their entire states onto each other without contradiction, i.e. $\\I(\\A, \\cA \\mid \\t\_\\Dt(J)) = h(J)$ and $\\I(\\A, \\cA \\mid \\t\_\\Dt(J^\\dg)) = h(J^\\dg)$ are both at their maximums.


Let's consider the smallest scrambler ([#Scrambler](#scrambler)) where $k=3$:

$A = B = \\set{0,1,2}$

$$
\\t\_1(a,b) = \\Big(a+b \\pmod{3},\\ b-a \\pmod{3}\\Big)
$$

The I/O table is

| $ab$ | $\\t\_1(ab)$ |
| ---- | ---- |
| $00$ | $00$ |
| $01$ | $11$ |
| $02$ | $22$ |
| $10$ | $12$ |
| $11$ | $20$ |
| $12$ | $01$ |
| $20$ | $21$ |
| $21$ | $02$ |
| $22$ | $10$ |

Using the partition formulation of systems A and B:
$\\A = \\set{a\\up{0},a\\up{1},a\\up{2}} = \\set{\\set{00,01,02},\\set{10,11,12},\\set{20,21,22}}$
$\\fB = \\set{b\\up{0},b\\up{1},b\\up{2}} = \\set{\\set{00,10,20},\\set{01,11,21},\\set{02,12,22}}$

I will show that $\\I(\\A, \\fB \\mid \\t(a\\up{0}))$ and $\\I(\\A, \\fB \\mid \\t(b\\up{0}))$ are simultaneously at their maximum values. This suggests that, counterintuitively, information can be simultaneously copied from A to B, and from B to A.

$a\\up{0} = \\set{00,01,02}$
$b\\up{0} = \\set{00,10,20}$
$\\t\_1(a\\up{0}) = \\set{00, 11, 22}$
$\\t\_1(b\\up{0}) = \\set{00, 12, 21}$

$\\A\\dom{a\\up{0}} = \\set{\\set{00,01,02},\\set{}}$
$\\fB\\dom{a\\up{0}} = \\set{\\set{00},\\set{01},\\set{02}}$
$\\A\\dom{\\t\_1(a\\up{0})} = \\set{\\set{00},\\set{11},\\set{22}}$
$\\fB\\dom{\\t\_1(a\\up{0})} = \\set{\\set{00},\\set{11},\\set{22}}$
$\\I(\\A, \\fB \\mid a\\up{0})) = 0$
$\\I(\\A,\\fB\\mid \\t\_1(a\\up{0})) = \\lgfr{1\\cdot 3}{1\\cdot 1} = \\lg(3) = h(a\\up{0})$
$\\H(\\A \\mid \\t\_1(a\\up{0})) = \\H(\\fB \\mid \\t\_1(a\\up{0})) = \\lg(a\\up{0})$

$\\A\\dom{b\\up{0}} = \\set{\\set{00},\\set{10},\\set{20}}$
$\\fB\\dom{b\\up{0}} = \\set{\\set{00,10,20},\\set{}}$
$\\A\\dom{\\t\_1(b\\up{0})} = \\set{\\set{00},\\set{12},\\set{21}}$
$\\fB\\dom{\\t\_1(b\\up{0})} = \\set{\\set{00},\\set{12},\\set{21}}$
$\\I(\\A, \\fB \\mid b\\up{0})) = 0$
$\\I(\\A,\\fB\\mid \\t\_1(b\\up{0})) = \\lg(3) = h(b\\up{0})$
$\\H(\\A \\mid \\t\_1(b\\up{0})) = \\H(\\fB \\mid \\t\_1(b\\up{0})) = \\lg(3)$

So $\\I(\\A,\\fB\\mid \\t\_1(a\\up{0})) = h(a\\up{0})$ and $\\I(\\A,\\fB\\mid \\t\_1(b\\up{0})) = h(b\\up{0})$ which are their respective maximum values (because $\\I(\\A,\\fB) = 0$ and $\\I(\\A\\otimes\\fB, R) = h(R)$ for any $R\\subseteq\\O$).


# Is Redundancy Fictitious?


The appearance of copied state is due to the representation of systems that we use. Notice that my proposed definition of copying and redundancy each rely on state partitions to be provided. If we just had a universe consisting of state space $\\O$ and bijective time-evolution $\\t\_\\Dt$, without any systems defined within the universe, there would not be any apparent copying or redundancy.

Take the simple copier again. I defined the state space as $\\O = \\set{00,01,10,11}$. The representation of theses states as binary strings begs the copying interpretation. What if instead I stripped away the extraneous representation of these states so that they became featureless objects? Like this:

$$
\\O = \\set{\\o\_1, \\o\_2, \\o\_3, \\o\_4}
$$

where $\\t\_1$ has the following I/O table:
$\\o\_1 \\mapsto \\o\_1$
$\\o\_2 \\mapsto \\o\_3$
$\\o\_3 \\mapsto \\o\_4$
$\\o\_4 \\mapsto \\o\_2$

Now the possible states in $\\O$ don't have any inherent interpretation, representation, or meaning. Their only feature is that they can be distinguished, i.e. they have identity. Combined with the time-evolution function $\\t\_1$, the only structure that is apparent here are the cycles $\\o\_1 \\to \\o\_1$ and $\\o\_2 \\to \\o\_3 \\to \\o\_4 \\to \\o\_1$.

We can go ahead and define whatever systems we like (having arbitrary state spaces). However, there are two trivial systems for this toy universe.

System T, whose states are the cycles:

$$
\\mf{T} = \\set{\\set{\\o\_1}, \\set{\\o\_2, \\o\_3, \\o\_4}}\\,.
$$

System O, whose states are all singleton:

$$
\\mf{O} = \\set{\\set{\\o\_1}, \\set{\\o\_2}, \\set{\\o\_3}, \\set{\\o\_4}}\\,.
$$

Both these systems' states never change through time, i.e. $\\t\_1(\\set{\\o\_1}) = \\set{\\o\_1}$ and $\\t\_1(\\set{\\o\_2, \\o\_3, \\o\_4}) = \\set{\\o\_2, \\o\_3, \\o\_4}$, and obviously $\\t\_1(\\mf{O}) = \\mf{O}$.

It is easy to show that using any of the sets in $\\mf{T}$ or $\\mf{O}$ as intervention sets $J$ results in no change in redundancy over time, i.e. $\\I(\\mf{T}, \\mf{O} \\mid J) = \\I(\\mf{T}, \\mf{O} \\mid \\t\_\\Dt(J))$ for all $\\Dt$.


For any universe defined by $\\O$ and $\\t\_\\Dt$, there is always a trivial system $\\mf{T}$ whose states (equivalence classes) consist of the cycles on $\\O$ under time evolution, and a trivial system consisting of the singleton partition $\\mf{O}$ on $\\O$. Both systems are always static through time, and their redundancy doesn't change over time. Thus, for any universe, there is always a definition of two systems s.t. copying is not taking place and redundancy is not appearing over time.

Clearly, redundancy and copying are relative phenomena - specifically relative to a particular system in the universe. This begs the question: Is the delineation between systems is objective or arbitrary. That is to say, what makes system A have the particular state space $\\A$, what makes system B have the particular state space $\\fB$, etc. ?  See {{< locallink "Preferred Representation Problem" >}}.


The observation of redundancy between two systems A and B implies any of
1. $\\I(\\A, \\fB) > 0$, i.e. your working definition of the systems in the universe contains redundancy.
2. $\\I(\\A, \\fB \\mid J) > 0$, i.e. you are restricting the state space of the universe, i.e. making assumptions about what states the universe cannot be in.


The observation that redundancy in the universe increases over time implies any of
1. $\\A\\up{t+\\Dt} \\neq \\A\\up{t}$ or $\\fB\\up{t+\\Dt} \\neq \\fB\\up{t}$, i.e. your definition of the state spaces of systems A and B is changing over time.
2. $\\I(\\A, \\fB \\mid \\t\_\\Dt(J)) > 0$ you are restricting the state space of the universe (making assumptions), and the time evolution of that restricted domain is causing redundancy to change over time.



# The Problem Of Assumptions In Intelligence

Why does our universe appear to have redundancy?

Given that information copying and redundancy appear all around us, we must conclude that our brains operate on a state space with which there is naturally a lot of redundancy between systems (as we delineate them).

It is important to draw a distinction between physical information that systems have ({{< locallink "Physical Information" "systems-have-information" >}}) and the conscious perception of information in intelligent and sentient systems. The former depends on the objective existence of both a universe state space $\\O$ and the state space of that system, e.g. $\\mf{A}$. The latter may be entirely independent of the former, i.e. an intelligent system might be aware of very different information than the system physically has. For an intelligent system to know what information it physically has would require it to have meta-information about itself, i.e. information about its own state space and state.

The problem of assumptions is to explain what assumptions intelligent life make about their surroundings, and whether those assumptions are arbitrary or can be derived from some principles or evolutionary history of life on Earth. The answer to this question should also tell us what assumptions (or inductive biases or priors, to use machine learning terminology) to build into artificial intelligence in order for it to be general purpose, at least to the extent that humans are.

## Alternative framing

Another way of framing the problem of assumptions:

Let $a\\up{t} \\in \\A$ be a state of system A. Then if system A has the information $\\O\\tr a\\up{t}$, it has information about its own future and the future of some other system B, quantified by $\\I(\\A, \\t\_\\Dt(a\\up{t}))$ and $\\I(\\fB, \\t\_\\Dt(a\\up{t}))$. Furthermore, if $\\I(\\mf{A}, \\mf{B} \\mid \\t\_\\Dt(a\\up{t})) > 0$, then system A "knows" that system A and B will be redundant in the future, given the information $\\O\\tr\\t\_\\Dt(a\\up{t})$. However, when that future time arrives, system A no longer has the information $\\O\\tr\\t\_\\Dt(a\\up{t})$, but instead has the information $\\O\\tr\\t\_\\Dt(a\\up{t+\\Dt})$. Note that necessarily $a\\up{t}\\neq a\\up{t+\\Dt}$ in order for $\\I(\\mf{A}, \\mf{B} \\mid \\t\_\\Dt(a\\up{t})) > 0$ to hold. So although there would be redundancy between systems A and B knowing $\\O\\tr\\t\_\\Dt(a\\up{t})$, system A no longer has that information and the appearance of redundancy is lost when time $t+\\Dt$ arrives.

For redundancy to exist in the present moment, rather than the past or the future, there needs to be such an additional assumption, i.e. an a priori narrowing down of $\\O$ to some smaller domain that makes otherwise orthogonal systems redundant. This assumption is not physical, as I've defined physical information. Yet all living things make such assumptions in their operation. See {{< locallink "The Origin Of Assumptions In Living Systems" >}}.

In {{< locallink "Causality And Information" "information-about-entails-effect-on" >}}, I concluded that the only way for a system to have information about another system's future is for the former system to causally determine the latter system. However, that is clearly not true in our universe. You can look at a map and drive on a sequence of streets you've never been on before, and yet you knew those streets would be there and where they would lead. You did not cause the streets to be as they were. You were able to have information about the streets because the map and the streets (as systems) have redundant information. In general, all life depends on information redundancy and environment prediction to survive and propagate. Life itself is a product of information redundancy - i.e. living organisms are self-replicators, and DNA stores the information that gets copied when an organism reproduces.

Perhaps the redundancies we perceive might offer clues as to the restricted state spaces human brains consciously operate under (i.e. assumptions our brains make).
