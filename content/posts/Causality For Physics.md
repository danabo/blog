---
date: 2021-04-20
lastmod: '2021-05-19T15:34:39-07:00'
tags:
- physics
title: Causality For Physics
---

$$
\\newcommand{\\0}{\\mathrm{false}}
\\newcommand{\\1}{\\mathrm{true}}
\\newcommand{\\mb}{\\mathbb}
\\newcommand{\\mc}{\\mathcal}
\\newcommand{\\mf}{\\mathfrak}
\\newcommand{\\and}{\\wedge}
\\newcommand{\\or}{\\vee}
\\newcommand{\\a}{\\alpha}
\\newcommand{\\s}{\\sigma}
\\newcommand{\\t}{\\tau}
\\newcommand{\\T}{\\Theta}
\\newcommand{\\D}{\\Delta}
\\newcommand{\\d}{\\delta}
\\newcommand{\\dd}{\\mathrm{d}}
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
\\newcommand{\\E}{\\mb{E}}
\\newcommand{\\R}{\\mb{R}}
\\newcommand{\\e}{\\varepsilon}
\\newcommand{\\set}\[1\]{\\left\\{#1\\right\\}}
\\newcommand{\\par}\[1\]{\\left(#1\\right)}
\\newcommand{\\abs}\[1\]{\\left\\lvert#1\\right\\rvert}
\\newcommand{\\vtup}\[1\]{\\left\\langle#1\\right\\rangle}
\\newcommand{\\inv}\[1\]{{#1}^{-1}}
\\newcommand{\\ceil}\[1\]{\\left\\lceil#1\\right\\rceil}
\\newcommand{\\dom}\[2\]{#1\_{\\mid #2}}
\\newcommand{\\df}{\\overset{\\mathrm{def}}{=}}
\\newcommand{\\M}{\\mc{M}}
\\newcommand{\\up}\[1\]{^{(#1)}}
\\newcommand{\\Do}{\\mathrm{do}}
\\newcommand{\\do}\[2\]{\\underset{#1\\leadsto #2}{\\mathrm{do}}}
\\newcommand{\\restr}\[1\]{\_{\\mid{#1}}}
\\newcommand{\\dt}{{\\D t}}
\\newcommand{\\Dt}{{\\D t}}
\\newcommand{\\ddT}{{\\delta T}}
\\newcommand{\\Mid}{\\,\\middle|\\,}
\\newcommand{\\qed}{\\ \\ \\blacksquare}
$$




The definition of causality within physics is not a settled matter, perhaps surprisingly. My understanding is that this question is studied more by philosophers than physicists, as the field of physics tends to avoid interpretational problems. That is to say, theories like relativity or quantum mechanics are mathematically well defined and make predictions, so that's all there is to it, right? I'm not a physicist, so I will proceed to ask such questions.

I suspect that causality and information are intimately related. To initiate my pursuit to understand physical information, I am starting by trying to understand the role causality plays in physics. The [SEP](https://plato.stanford.edu/entries/causation-physics) outlines some of the conversation and ideas around causality and physics. I haven't read these ideas yet, but I want to take my own tabula rasa stab at the problem before reading about what other people have tried. I am familiar with Judea Pearl's notion of causality in machine learning and statistics, which I will attempt to apply to physics below.

# Causal Models
First, I'll outline Pearl's framework for causality. I used [Causality](http://bayes.cs.ucla.edu/BOOK-2K/) (Pearl) and [Elements of Causal Inference](https://mitpress.mit.edu/books/elements-causal-inference) (Peters, Janzing, Schölkopf) to learn about this topic.

Pearl assumes the world (or some part of it) can be represented by graph, where nodes represent potential observations, and their directed edges represent causal links. For example (from Pearl):

![](</Pasted image 20210412175938.png>)
The core idea in Pearl's causality is the **intervention**, which is a modification to the graph where a node is disconnected from all incoming arrows and held fixed at some value.

An example of an intervention:

![](</Pasted image 20210412175953.png>)
An intervention in this graph is a **graph surgery** (as Pearl calls it). Graph interventions correspond to real-world interventions. The intervention depicted above corresponds to someone forcing the sprinkler system to turn on (e.g. by switching the sprinkler system's setting from auto to manual). The sprinkler state is now causally independent of everything else in the graph, because we, the experimenters, have directly determined its state (we would need to be careful to ensure our own actions are not causally linked to the system we are studying). By observing the down stream effects of this change to the graph, the **causal effect** of the particular node $X\_3$ can be measured. That is the effect of $X\_3$, independent of other nodes like $X\_1$.

Generally Pearl places a probability distribution on graph node states, given by $P(X\_1=x\_1, X\_2=x\_2, X\_3=x\_3, \\dots)$, or using shorthand, $P(x\_1, x\_2, x\_3, \\dots)$. I'll use capital letters, $X\_i$, to denote graph nodes themselves (or random variables on graph nodes), and lowercase letters, $x\_i$, to denote a specific value that the correspond node takes on. So for example, node $X\_3$, the sprinkler state, could take on the values $\\mathrm{ON}$ or $\\mathrm{OFF}$. In the abstract, $X\_3$ takes on some value $x\_3$. Sometimes I'll introduce a "prime" tick, $x'\_3$, to denote some other value that may be distinct from $x\_3$.


There is an alternative **functional** perspective, where each node's value is a deterministic function of incoming values traveling along inward arrows, and an auxiliary noise input not depicted in the graph. Those noise inputs can themselves be determined (i.e. held fixed), but be pulled from an algorithmically random stream. I will stick to the deterministic perspective when I discuss physics, while recognizing that random physical processes can be viewed as deterministic but algorithmically random.

Quoting [Causality](http://bayes.cs.ucla.edu/BOOK-2K/), section 1.4.1, *Structural Equations*:
>  In its general form, a functional causal model consists of a set of equations of the form 
> $$x\_i = f\_i(pa\_i,u\_i),\\quad i=1,\\dots,n\\,,$$
> where $pa\_i$ (connoting parents) stands for the set of variables that directly determine the value of $X\_i$ and where the $U\_i$ represent errors (or “disturbances”) due to omitted factors.

That is to say, the parents $PA\_i$ of node $X\_i$ is the set of nodes with arrows pointing into $X\_i$. So in the example, $PA\_3 = \\set{X\_1}$ because $X\_1$ is the only node pointing into $X\_3$, and $PA\_4 = \\set{X\_2, X\_3}$ because both $X\_2$ and $X\_3$ point into $X\_4$. Node $X\_1$ is not a direct parent of $X\_4$.

$U\_i$ is an auxiliary input node to each $X\_i$ which is not depicted in the graph, which makes the output value $x\_i$ random. In my view, each value $u\_i$ is pulled from an algorithmically random stream. Given the set of values $pa\_i$ and value $u\_i$, the output of the function $f\_i$ is then able to be random.

A note about notation: It would not be correct to write $f\_i(PA\_i,U\_i)$ which passes the nodes themselves into the function $f\_i$. On the other hand, $f\_i(pa\_i,u\_i)$ is passing the values $pa\_i$ of the parent nodes $PA\_i$ and $u\_i$ of the noise input node $U\_i$ into the function.


## Do-Operator

If $P$ is the probability measure on the initial graph (e.g. figure 1.2 above), then what is the probability measure on the modified graph after taking an intervention (e.g. figure 1.4)? Pearl uses "do"-notation, which for the example above looks like this:

$$
P(x\_1, x\_2, x\_3, x\_4, x\_5 \\mid \\Do(X\_3 = \\mathrm{ON}))\\,.
$$

This is the probability of the vector of node values $(x\_1, x\_2, x\_3, x\_4, x\_5)$ given that the intervention setting node $X\_3$ to constant value $\\mathrm{ON}$ was taken. Note the notational similarity to conditional probability: $P(x\_1, x\_2, x\_3, x\_4, x\_5 \\mid X\_3 = \\mathrm{ON})$. Conditionalization is a different operation on the measure $P$ than the "do"-operator, but they are mathematically related and their similar notation is justified.


For an arbitrary graph with nodes $X\_1,\\dots,X\_n$, and probability measure $P$ on node values, the conditional probability of value vector $(x\_1, \\dots, x\_n)$ given $X\_i = x'\_i$ is

$$
P(x\_1, \\dots, x\_n \\mid x'\_i) = \\begin{cases}
    \\frac{P(x\_1, \\dots, x\_n)}{P(x'\_i)} & x\_i=x'\_i \\\\
    0 & x\_i \\neq x'\_i
\\end{cases}
$$

whereas the probability of $(x\_1, \\dots, x\_n)$ given that intervention $\\Do(X\_i = x'\_i)$ was taken is ([Causality](http://bayes.cs.ucla.edu/BOOK-2K/), eq 3.11)

$$
P(x\_1, \\dots, x\_n \\mid \\mathrm{do}(x'\_i)) = \\begin{cases}
    \\frac{P(x\_1, \\dots, x\_n)}{P(x'\_i \\mid pa\_i)} & x\_i=x'\_i \\\\
    0 & x\_i \\neq x'\_i
\\end{cases}
$$

Both operations are performing a **domain restriction** on $P$, in the sense that the resulting measure assigns 0 probability to all vectors $(x\_1, \\dots, x\_n)$ where $x\_i \\neq x'\_i$, for some constant $x'\_i$. The difference between them is that conditionalization, $P(x\_1, \\dots, x\_n \\mid x'\_i)$, simply rescales the resulting measure by $1/P(x'\_i)$ after domain restriction, whereas intervention, $P(x\_1, \\dots, x\_n \\mid \\mathrm{do}(x'\_i))$, re-weights every single probability independently by $1/P(x'\_i \\mid pa\_i)$, where $pa\_i$ is the set of values in $(x\_1, \\dots, x\_n)$ for the parent nodes $PA\_i$ of node $X\_i$. 

Rewriting $P(x\_1, \\dots, x\_n)$, we can see why multiplying by $1/P(x'\_i \\mid pa\_i)$ corresponds to an intervention:

$$
P(x\_1, \\dots, x\_n) = \\prod\_{j=1}^n P(x\_j \\mid pa\_j)\\,,
$$

by the chain rule of probability, because the graph also encodes which nodes are statistically independent, i.e. if $x\_k \\notin pa\_j$, then $P(x\_j \\mid x\_k) = P(x\_j)$.

The operation of removing the connections going into $X\_i$ from the parents $PA\_i$ is a matter of removing the term $P(x\_i \\mid pa\_i)$ by dividing it out.

This formulation of an intervention can be generalized further. Instead of setting $X\_i$ to a constant value $x'\_i$, in general, we can replace the node distribution $P(X\_i \\mid PA\_i)$ with the new distribution $Q(X\_i \\mid PA'\_i)$ where $PA'\_i$ is some new set of parents, which may or may not be the empty set, or equivalent to or overlap with the old parents $PA\_i$. If $PA'\_i$ is empty, that is equivalent to making $Q$ statistically independent where $Q(X\_i \\mid PA\_i) = Q(X\_i)$. We can get our constant-value intervention by choosing a delta distribution (one-hot for discrete $X\_i$, and Dirac delta for continuous $X\_i$) $Q(X\_i) = \\d\_{x'\_i}$ which is non-zero only if $X\_i = x'\_i$. Now this general-case intervention is replacing the term $P(X\_i \\mid PA\_i)$ with $Q(X\_i \\mid PA'\_i)$, which looks like this:

$$
\\begin{aligned}
& P\\left(x\_1, \\dots, x\_n \\Mid\\, \\Do\\left\\{P(x\_i\\mid pa\_i) \\to Q(x\_i\\mid pa'\_i)\\right\\}\\ \\right) \\\\ \\\\
&=
    P(x\_1, \\dots, x\_n)\\frac{Q(x\_i \\mid pa'\_i)}{P(x\_i \\mid pa\_i)}\\,.
\\end{aligned}
$$

When $Q(x\_i \\mid pa'\_i) = Q(x\_i) = \\d\_{x'\_i}$ this expression reduces to the constant-value intervention defined above.

In the functional perspective, an intervention replaces $f\_i(pa\_i, u\_i)$ with some other function $f'\_i(pa'\_i, u\_i)$.

## Causal Effect
In [Causality](http://bayes.cs.ucla.edu/BOOK-2K/), definition 3.2.1, Pearl defines causal effect as follows:

Let $X$ and $Y$ be two disjoint sets of graph nodes. The **causal effect** of $X$ on $Y$ is the *function* $\\mc{E}$ from the space of node values for $X$ to the space of probability measures on $Y$, 

$$
\\mc{E}(x) = P(Y \\mid \\Do(X=x))\\,,
$$

where $x$ is some chosen vector of values for the nodes $X$.

That is to say, the causal effect of nodes $X$ on nodes $Y$ is characterized by the set of all interventions obtained setting $X$ to every possible value $x$, where each intervention is characterized by a change in probability distribution on $Y$. That is to say, the causal effect of $X$ on $Y$ is characterized by how $P(Y \\mid \\Do(X=x))$ varies for different $x$, and compared to no intervention $P(Y)$.

## When Interventions And Conditionalization Are Equivalent



It should be obvious that when node $X\_i$ has no parents then $P(x\_{1:n} \\mid \\Do(x'\_i)) = P(x\_{1:n} \\mid x'\_i)$ for all node values $x'\_i$, because $PA\_i = \\emptyset$ and so $P(x'\_i \\mid pa\_i) = P(x'\_i)$.

Another case is when we are only considering the marginal distribution on a subset of variables. Then the conditional distribution and intervention distribution on the [Markov blanket](https://en.wikipedia.org/wiki/Markov_blanket) of that subset are equivalent.

To see what I mean, let's consider the Markov chain $X\_1, \\dots, X\_n$ where $P(x\_1, \\dots, x\_n) = P(x\_n \\mid x\_{n-1})P(x\_{n-1} \\mid x\_{n-2})\\dots P(x\_2 \\mid x\_1)P(x\_1)$ and $PA\_i = \\set{X\_{i-1}}$ for all $i > 1$. Then we have



$$
\\begin{aligned}
& P(x\_n, \\dots, x\_{i+1} \\mid \\Do(x'\_i)) \\\\
  &\\quad= \\sum\_{x\_{i-1},\\dots,x\_1} P(x\_n, \\dots, x\_1 \\mid \\Do(x'\_i)) \\\\
 &\\quad= \\begin{cases}
        \\sum\_{x\_{i-1},\\dots,x\_1}\\frac{P(x\_n, \\dots, x\_{i+1}\\mid x\_i)P(x\_i \\mid x\_{i-1})P(x\_{i-1},\\dots,x\_1)}{P(x'\_i \\mid x\_{i-1})} & x\_i=x'\_i \\\\
        0 & x\_i \\neq x'\_i
    \\end{cases} \\\\
 &\\quad= \\sum\_{x\_{i-1},\\dots,x\_1}P(x\_n, \\dots, x\_{i+1} \\mid x'\_i)P(x\_{i-1},\\dots,x\_1) \\\\
 &\\quad= P(x\_n, \\dots, x\_{i+1} \\mid x'\_i)\\,.
\\end{aligned}
$$

![](</Pasted image 20210519122301.png>)

# Causality For Physics
Pearl's causality is based on the idea of the intervention, which is a kind of graph surgery.

To apply Pearl's causality to physics, we'd need to define what an intervention does to physical processes. There are two immediate problems:
1. Pearl defines interventions for causal graphs, where node values are sampled i.i.d., and the nodes represent are stateless and otherwise  isolated processes (aside from their arrows). Physics, on the other hand, allows for arbitrary interactions between systems, to the point where the boundaries between systems may be blurred or destroyed so that it does not even make sense to think about there being any independent components at all (think about a liquid or gas). Physical processes are not i.i.d. (the future depends on the past), and they have internal state which determines their future time evolution.
2. Classical physics is non-probabilistic (non-statistical Newtonian mechanics and relativity). If our notation of causality is to be suitable to all of physics, we need to apply to Newtonian mechanics, which means causality must precede probability. Therefore we need to define interventions on deterministic systems.

Pearl generally considers a graph intervention to represent an intervention that can conceivably be taken, and ideally taken recently so that the causal effect of various interventions can be empirically estimated with histograms (empirically estimate $P(Y \\mid \\Do(X))$ and $P(Y)$).

I don't think physical plausible interventions can generalize to arbitrary physical systems. I will instead consider what I call a **counterfactual intervention**, which is merely a modification to a mathematical model (i.e. representation) of physics. A counterfactual intervention is hypothetical, and produces a different time-line than the "factual" time-evolution of the system. A counterfactual intervention is the answer to the question, "what would have happened if the system were in state $x'$ rather than state $x$ at time $t$?"

If intuition serves right and the logical structure of causality lies within all theories of physics, the purpose of the counterfactual intervention is to probe those theories to make their implicit causal structures mathematically explicit.

My objective here is to define an abstract definition for theories of physics in general, define what it means to take a counterfactual intervention on a physical system (both probabilistic or non-probabilistic), and then to show the equivalence of this type of intervention to Pearl's graph intervention above.


## Abstract Physics
In any theory of physics there is a state space $\\O$. In Newtonian mechanics, state is a vector of various components of the system, such as a [vector of positions and momenta](https://en.wikipedia.org/wiki/Canonical_coordinates#Definition_in_classical_mechanics) given by $\\o = (\\vec{q}, \\vec{p}) \\in \\O$. In general state can include other kinds of [degrees of freedom](https://en.wikipedia.org/wiki/Degrees_of_freedom_(mechanics)) such as the orientation of solid bodies in 3D space. In quantum mechanics there is [quantum state](https://en.wikipedia.org/wiki/Quantum_state), and state spaces are [Hilbert spaces](https://en.wikipedia.org/wiki/Hilbert_space#Quantum_mechanics).

A **theory of physics** specifies both the state space $\\O$ and how to solve for the time-evolution of the system given a particular state $\\o\_t$ at time $t$. The result is a complete description of a system's time evolution through state space given as a state-function of time, $\\s : \\R \\to \\O : t \\mapsto \\s(t)$, which I'll call a **trajectory**. To be clear, a single trajectory $\\s$ is a single possible time-evolution, e.g. where $\\s(t) = \\o\_t$.

The mathematical machinery that converts known information, e.g. the state of the system at time $t$, varies between theories of physics and often makes use of a [Lagrangian](https://en.wikipedia.org/wiki/Analytical_mechanics#Lagrangian_mechanics) or [Hamiltonian](https://en.wikipedia.org/wiki/Analytical_mechanics#Hamiltonian_mechanics). These details can be abstracted away.  In principle, for any theory of physics  there is a family of [time-evolution functions](https://en.wikipedia.org/wiki/Time_evolution#Time_evolution_operators) $\\t\_{\\Dt} : \\O \\to \\O$, for every time interval $\\Dt\\in\\R$ (both positive and negative) which maps any state $\\o\\in\\O$ at time $t$ to the state at time $t+\\Dt$. Typically physics is [time-symmetric](https://en.wikipedia.org/wiki/T-symmetry), which means that $\\t\_{\\Dt}$ is a bijection and thus invertible. Note also that $\\t\_{\\Dt}$ does not depend on the absolute time $t$, and so we are implicitly assuming the given theory of physics is [time-translationally invariant](https://en.wikipedia.org/wiki/Time_translation_symmetry).

The set of all trajectories is $\\R \\to \\O$, [denoting the set of all functions](https://en.wikipedia.org/wiki/Function_space) from $\\R$ to $\\O$. For a given time-evolution family $\\t$, there is a subset of trajectories which are **valid for $\\t$** (or **$\\t$-valid**),

$$
\\Sigma = \\set{\\s : \\R\\to\\O \\mid \\fa t,\\Dt\\in\\R : \\s(t+\\dt) = \\t\_\\dt(\\s(t))}\\,.
$$

### Incorporating Probability
Suppose we want to work with some kind of statistical physics. Perhaps we are uncertain about which state the system is in, or the state is randomly chosen. We can just as easily put a probability measure on the set of trajectories.

Let $M$ be a probability measure on the set of all trajectories $\\R \\to \\O$. Moreover, we want to require $M$ to obey the physics of $\\t$ and assign zero probability to physically impossible trajectories, i.e. $\\t$-invalid trajectories. Specifically, $M$ should assign 0 probability to any set comprised *only* of $\\t$-invalid trajectories, or equivalently, $M(\\Sigma) = 1$ (if $M$ is a normalized measure).

This is not typically how statistical physics is conceived of. Normally, there is a probability measure on states at time $t$, and time evolution time-evolves that measure. Instead, I've put a static global measure $M$ on entire trajectories. However, these two views are equivalent.

Let $\\mu\_t$ be the marginal probability measure on state space $\\O$ of the "system" at time $t$. Specifically, $\\mu\_t$ is the unique marginal distribution of $M$ on time $t$ only, given by

$$
\\mu\_t(\\mc{O}) = M\\set{\\s:\\R\\to\\O \\mid \\s(t) \\in \\mc{O}}\\,,
$$

for (measurable) state subsets $\\mc{O}\\subseteq \\O$. Then $\\mu\_{t+\\Dt}$ is then the time-evolution of measure $\\mu\_t$, given by

$$
\\mu\_{t+\\Dt}(\\mc{O}) = \\mu\_t(\\t^{-1}\_\\Dt(\\mc{O}))\\,.
$$

---

***Proof*** that $\\mu\_t(\\t^{-1}\_\\Dt(\\mc{O})) = M\\set{\\s:\\R\\to\\O \\mid \\s(t+\\Dt) \\in \\mc{O}}$:
$M\\set{\\s:\\R\\to\\O \\mid \\s(t+\\Dt) \\in \\mc{O}}$
$= M\\set{\\s\\in\\Sigma \\mid \\s(t+\\Dt) \\in \\mc{O}} + M\\set{\\s\\in\\overline{\\Sigma} \\mid \\s(t+\\Dt) \\in \\mc{O}}$
$= M\\set{\\s\\in\\Sigma \\mid \\s(t+\\Dt) \\in \\mc{O}} + 0$.
$\\set{\\s\\in\\Sigma \\mid \\s(t+\\Dt) \\in \\mc{O}} = \\set{\\s\\in\\Sigma \\mid \\s(t) \\in \\t^{-1}\_\\Dt(\\mc{O})}$ by the definition of $\\Sigma$.
$M\\set{\\s\\in\\Sigma \\mid \\s(t) \\in \\t^{-1}\_\\Dt(\\mc{O})}$
$= M\\set{\\s:\\R\\to\\O \\mid \\s(t) \\in \\t^{-1}\_\\Dt(\\mc{O})}$
$= \\mu\_t(\\t^{-1}\_\\Dt(\\mc{O}))$ by the definition of $\\mu\_t$. $\\qed$

---

***Proof*** that $M$ is uniquely determined by $\\mu\_t$, so long as $\\t\_\\Dt$ is a bijection and $M(\\Sigma)=1$.

At time $t$, for each $\\o\\in\\O$, there is a unique $\\t$-valid trajectory $\\s$ that passes through $\\o$, given by the mapping $t'\\mapsto\\t\_{t'-t}(\\o)$. Therefore, there is a family of bijections between the $\\t$-valid trajectories $\\Sigma$ and state space $\\O$:

$$
\\Gamma\_t : \\O \\to \\Sigma : \\o \\mapsto(t'\\mapsto\\t\_{t'-t}(\\o))\\,,
$$

for all $t\\in\\R$. So $\\Gamma\_t(\\o) = \\s$ where $\\s(t) = \\o$ and $\\s$ is $\\t$-valid. The inverse is then $\\Gamma^{-1}\_t(\\s)=\\s(t)$. I haven't defined proper measure spaces on trajectories and states, so I will just assume $\\Gamma\_t$ is a measurable function.

We can derive the following relation:
$\\mu\_t(\\mc{O}) = M\\set{\\s:\\R\\to\\O \\mid \\s(t) \\in \\mc{O}}$
$=M\\set{\\s\\in\\Sigma \\mid \\s(t) \\in \\mc{O}}$
$=M\\Gamma\_t\\mc{O}$.

Thus for any (measurable) subset of trajectories $S \\subseteq (\\R\\to\\O)$, there is a corresponding (measurable) subset of states $\\mc{O} = \\Gamma^{-1}\_t(S\\cap\\Sigma)$ so that $M(S) = M(S\\cap\\Sigma) = M(\\Gamma\_t\\Gamma^{-1}\_t(S\\cap\\Sigma)) = M(\\Gamma\_t\\mc{O}) = \\mu\_t(\\mc{O})$. $\\qed$


## Interventions For Physics

Let $I : \\O\\to\\O$ be a **state-replacement function**. Usually we want $I$ to be some kind of state projection function where $I(\\O) \\subset \\O$ is a strict subset.


I will define a "do"-operator on individual trajectories which performs a surgery and outputs a modified trajectory. Specifically, given state-replacement function $I$ and time $T$,

$$
\\do{I}{T}\[\\s\](t) \\df \\begin{cases}\\s(t) & t < T \\\\ \\t\_{t-T}(I(\\s(T))) & t\\geq T\\end{cases}\\,.
$$

The resulting trajectory is identical to $\\s$ prior to time $T$, and discontinuously jumps at time $T$ to the alternative $\\t$-valid trajectory starting from state $I(\\s(T))$. In this way, $I$ determines which trajectory "tail" to attach to the given trajectory "head" $\\s$. The resulting "Frankenstein"-trajectory is usually not globally $\\t$-valid, but its head and tail are guaranteed to be $\\t$-valid, and thus is locally $\\t$-valid everywhere *except* across time $T$.

Let's overload this "do"-operator to apply element-wise to sets, so

$$
\\Sigma' = \\do{I}{T} \\Sigma = \\set{\\do{I}{T}\[\\s\] \\Mid \\s\\in\\Sigma}\\,.
$$

Starting with the measure $M$ from above, applying $\\do{I}{T}$ to the set of all trajectories $\\R\\to\\O$ induces a transformed measure $M'$, where for subsets $S' \\subseteq (\\R\\to\\O)$,

$$
M'(S') = M\\left(\\do{I}{T}^{-1}S'\\right) = M\\set{\\s\\in\\Sigma \\Mid \\do{I}{T}\[\\s\] \\in S'}\\,.
$$

This conception of intervention is different from Pearl's, which is a modification of the functions generating the behavior of the process in question. In my formulation, I am modifying the state of the process at some point in time, but keeping the behavior-generating-functions, i.e. $\\t$, unchanged. That is to say, I am modifying systems, but not the physics, whereas Pearl is modifying the physics, so to speak.


### Proof of Pearl-Equivalence

The question is whether my definition of an intervention is equivalent with Pearl's. To prove this, I need to put my intervention in terms of Pearl's setup.

The measure $M$ on trajectories corresponds to the measure $P$ on graph states, and the transformed measure $M'$ corresponds to the transformed measure $P(\\ldots \\mid \\Do(\\ldots))$ on the modified graph.

Recall that $M'$ is defined by 

$$
M'(S') = M\\set{\\s\\in\\Sigma \\Mid \\do{I}{T}\[\\s\] \\in S'}\\,,
$$

for subsets $S'\\subseteq (\\R\\to\\O)$ of trajectories. I need to show that $M'$ has the same form as Pearl's general intervention. 


It will help to define the following notation on trajectories:
$\\s\\restr{(a,b)}$ is the domain restriction of trajectory $\\s$ to time interval $(a,b)$.


I will use the following short-hands:
- $\\s\_{>T} = \\s\\restr{(T,\\infty)}$
- $\\s\_{<T} = \\s\\restr{(-\\infty,T)}$
- $\\s\_{\\ddT} = \\s\\restr{(T-\\dt,T)}$

where $\\dt > 0$ be an arbitrarily small positive real number.

The goal is to prove that

$$
M'(S') = \\int\_{S'} \\frac{Q(\\s(T) \\mid \\s\_{\\ddT})}{M(\\s(T) \\mid \\s\_{\\ddT})}  \\dd M(\\s)\\,,
$$

for some probability measure $Q$. This is a [Lebesgue integral](https://en.wikipedia.org/wiki/Lebesgue_integration) w.r.t. $\\s$ using measure $M$, which for our purposes is just the expectation of the integrand w.r.t. measure $M$. As a Riemann integral: $\\int\_{S'} M(\\s)\\frac{Q(\\s(T) \\mid \\s\_{\\ddT})}{M(\\s(T) \\mid \\s\_{\\ddT})}  \\dd \\s$.

It turns out that 

$$
Q(\\s(T) \\mid \\s\_{\\ddT}) = M(I^{-1}(\\s(T)) \\mid \\s\_{\\ddT})\\,.
$$

---

***Proof***

We have,
$M(\\s) = M(\\s\_{>T} \\mid \\s(T)) \\cdot M(\\s(T) \\mid \\s\_{\\ddT}) \\cdot M(\\s\_{<T})$,
where $M(\\s(T) \\mid \\s\_{\\ddT}) \\cdot M(\\s\_{<T}) = M(\\s(T) \\mid \\s\_{<T})$ because $M$ is Markov w.r.t. time, which is guaranteed by the construction of $\\Sigma$ from $\\t\_{\\D t}$.

Expanding out the integrand, we have

$$
\\begin{aligned}
& M(\\s)\\frac{Q(\\s(T) \\mid \\s\_{\\ddT})}{M(\\s(T) \\mid \\s\_{\\ddT})} \\\\ \\\\
=\\ & M(\\s\_{>T} \\mid \\s(T)) \\cdot M(\\s(T) \\mid \\s\_{\\ddT}) \\cdot M(\\s\_{<T})\\frac{Q(\\s(T) \\mid \\s\_{\\ddT})}{M(\\s(T) \\mid \\s\_{\\ddT})} \\\\ \\\\
=\\ & M(\\s\_{>T} \\mid \\s(T)) \\cdot Q(\\s(T) \\mid \\s\_{\\ddT}) \\cdot M(\\s\_{<T}) \\\\ \\\\
=\\ & M(\\s\_{>T} \\mid \\s(T)) \\cdot M(I^{-1}(\\s(T)) \\mid \\s\_{\\ddT}) \\cdot M(\\s\_{<T})\\,.
\\end{aligned}
$$

The remainder of this proof consists of showing the following equivalences, which I'll prove below as lemmas:
- $M(\\s\_{>T} \\mid \\s(T)) = M'(\\s\_{>T} \\mid \\s(T))$
- $M(I^{-1}(\\s(T)) \\mid \\s\_{\\ddT}) = M'(\\s(T) \\mid \\s\_{\\ddT})$
- $M(\\s\_{<T}) = M'(\\s\_{<T})$

That allows us to rewrite: 

$$
\\begin{aligned}
& M(\\s\_{>T} \\mid \\s(T)) \\cdot M(I^{-1}(\\s(T)) \\mid \\s\_{\\ddT}) \\cdot M(\\s\_{<T}) \\\\ \\\\
=\\ & M'(\\s\_{>T} \\mid \\s(T)) \\cdot M'(\\s(T) \\mid \\s\_{\\ddT}) \\cdot M'(\\s\_{<T}) \\\\ \\\\
=\\ & M'(\\s)\\,.
\\end{aligned}
$$

Therefore

$$
\\begin{aligned}
& \\int\_{S'} \\frac{Q(\\s(T) \\mid \\s\_{\\ddT})}{M(\\s(T) \\mid \\s\_{\\ddT})}  \\dd M(\\s) \\\\ \\\\
=\\ & \\int\_{S'} \\dd M'(\\s) \\\\ \\\\
=\\ & M'(S')\\,.
\\end{aligned}
$$

$\\qed$

---
***Proof*** of remaining lemmas:

The cases $M(\\s\_{>T} \\mid \\s(T)) = M'(\\s\_{>T} \\mid \\s(T))$ and $M(\\s\_{<T}) = M'(\\s\_{<T})$ are easy:
- Because the trajectory before $T$ is unchanged,
  $M(\\s\_{<T}) = M'(\\s\_{<T})$,
- Because time evolution from $T$ onward is deterministic and obeys $\\t\_\\dt$, there is exactly one trajectory $\\s^\*$ that is valid under $\\t\_\\dt$ s.t. $\\s^\*(T) = \\s(T)$. Thus
   $M(\\s\_{>T} \\mid \\s(T)) = M'(\\s\_{>T} \\mid \\s(T)) = \\begin{cases}1 & \\s\_{\\geq T} = \\s^\*\_{\\geq T} \\\\ 0 & \\mathrm{otherwise}\\end{cases}$.

Now to prove $M(I^{-1}(\\s(T)) \\mid \\s\_{\\ddT}) = M'(\\s(T) \\mid \\s\_{\\ddT})$. Expanding out $M(I^{-1}(\\s(T)) \\mid \\s\_{\\ddT})$, we get

$$
\\begin{aligned}
&M(I^{-1}(\\s(T)) \\mid \\s\_{\\ddT}) \\\\
=\\ & M\\set{\\z \\in \\Sigma \\mid \\z(T) \\in I^{-1}(\\s(T)) \\wedge \\z\\restr{(T-\\dt,T)} = \\s\_{\\ddT}}\\,.
\\end{aligned}
$$

Since

$$
\\do{I}{T}\[\\z\](t) = \\begin{cases}\\z(t) & t < T \\\\ \\t\_{t-T}(I(\\z(T))) & t\\geq T\\end{cases}
$$

then $\\z(T) \\in I^{-1}(\\s(T)) \\iff I(\\z(T)) = \\s(T) \\iff \\do{I}{T}\[\\z\](T) = \\s(T)$,
because $\\t\_0$ is the identity function.

Furthermore, $\\do{I}{T}\[\\z\]\\restr{(-\\infty,T)} = \\z\\restr{(-\\infty,T)}$,
so $\\z\\restr{(T-\\dt,T)} = \\s\_{\\ddT} \\iff \\do{I}{T}\[\\z\]\\restr{(T-\\dt,T)} = \\s\_{\\ddT}$.

Thus we can further expand out $M(I^{-1}(\\s(T)) \\mid \\s\_{\\ddT})$:

$$
\\begin{aligned}
& M(I^{-1}(\\s(T)) \\mid \\s\_{\\ddT}) \\\\
=\\ & M\\set{\\z \\in \\Sigma \\mid \\z(T) \\in I^{-1}(\\s(T)) \\wedge \\z\\restr{(T-\\dt,T)} = \\s\_{\\ddT}} \\\\
=\\ & M\\set{\\z \\in \\Sigma \\,\\middle|\\, \\do{I}{T}\[\\z\](T) = \\s(T) \\wedge \\do{I}{T}\[\\z\]\\restr{(T-\\dt,T)} = \\s\_{\\ddT}} \\\\
=\\ & M'(\\s(T) \\mid \\s\_{\\ddT})\\,.
\\end{aligned}
$$

$\\qed$

---

There is one problematic aspect to this equivalence. Taking another look at the first step in the proof,

$$
\\begin{aligned}
& M(\\s)\\frac{Q(\\s(T) \\mid \\s\_{\\ddT})}{M(\\s(T) \\mid \\s\_{\\ddT})} \\\\ \\\\
=\\ & M(\\s\_{>T} \\mid \\s(T)) \\cdot M(\\s(T) \\mid \\s\_{\\ddT}) \\cdot M(\\s\_{<T})\\frac{Q(\\s(T) \\mid \\s\_{\\ddT})}{M(\\s(T) \\mid \\s\_{\\ddT})} \\\\ \\\\
=\\ & M(\\s\_{>T} \\mid \\s(T)) \\cdot Q(\\s(T) \\mid \\s\_{\\ddT}) \\cdot M(\\s\_{<T})\\,,
\\end{aligned}
$$

we make the assumption that $M(\\s(T) \\mid \\s\_{\\ddT}) \\neq 0$. Given the trajectory slice $\\s\_{\\ddT} = \\s\\restr{(T-\\dt,T)}$, there is only one $\\t$-valid trajectory which shares the same slice, and so there is only one valid state $\\o^\*\_T$ at time $T$ to follow from $\\s\\restr{(T-\\dt,T)}$. Since $M$ obeys $\\t$,

$$
M(\\s(T) \\mid \\s\_{\\ddT}) = \\d\_{\\o^\*\_T}
$$

which is non-zero only if $\\s(T) = \\o^\*\_T$. If $\\s\\restr{(T-\\dt,T)}$ is itself not $\\t$-valid, we can define $M(\\s(T) \\mid \\s\_{\\ddT})$ to be an improper probability measure that is always $0$.

I'd argue that interventions on deterministic trajectories is a limiting case of interventions on probabilistic trajectories where the transition probabilities converge to delta distributions. Then $M(\\s(T) \\mid \\s\_{\\ddT})/M(\\s(T) \\mid \\s\_{\\ddT})\\to 1$ no matter what and the cancellation works.

## Compatibility with modern physics

The generalized formulation of physics, using state space $\\O$ and time-evolution function $\\t\_{\\D t}$, is compatible with classical physics and special relativity (for arbitrary choice of Lorentz frame). Is it compatible with quantum mechanics, general relativity, and beyond?

It is compatible with QM if we are time-evolving quantum state and disregarding measurement. If we wanted to model stochastic measurement outcomes, or stochastic interactions in general, then we could do that using a non-deterministic time-evolution function, i.e. $\\t\_{\\D t}$ is not a proper function and assigns more than one output to a given input. Alternatively, the state $\\O$ could contain algorithmically random data which serves as a source of random inputs for $\\t\_{\\D t}$.

For special relativity, simultaneity is relative, but consistently holding to an arbitrary choice of Lorentz frame will work. Then, there is a $\\t\_{\\D t}$ for every Lorentz frame, and one can transform between these time-evolution functions via Lorentz boosts.

For general relativity, I am not personally clear on whether there exist global reference frames where there is a single simultaneous state of the universe, even if what is regarded as simultaneous is arbitrarily chosen. In that case, my formulation may break down. However, there should still be a causal DAG. Is it possible to topologically sort that DAG and then organize it into something like time slices? Each such slice would then correspond to a state in $\\O$.

