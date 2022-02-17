---
date: 2022-02-17
lastmod: '2022-02-17T15:23:40-08:00'
tags:
- physics
- information
- thermodynamics
title: Szilard Cycle Particle-Piston Interaction Model
---


Admittedly my first-pass interaction model in {{< locallink "Reversible Szilard Cycle Problem" "part-ii-information-is-never-lost" >}} is not physically realistic. By interaction model, I mean how the particle and piston interact over time. Here I explore some alternative interaction models that try to be more realistic. My main question is whether which-side information is still preserved. <!--more-->

$$
\\newcommand{\\0}{\\mathrm{false}}
\\newcommand{\\1}{\\mathrm{true}}
\\newcommand{\\mb}{\\mathbb}
\\newcommand{\\mc}{\\mathcal}
\\newcommand{\\mf}{\\mathfrak}
\\newcommand{\\ms}{\\mathscr}
\\newcommand{\\and}{\\wedge}
\\newcommand{\\or}{\\vee}
\\newcommand{\\es}{\\emptyset}
\\newcommand{\\a}{\\alpha}
\\newcommand{\\t}{\\tau}
\\newcommand{\\T}{\\Theta}
\\newcommand{\\D}{\\Delta}
\\newcommand{\\d}{\\delta}
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
\\newcommand{\\L}{\\Lambda}
\\newcommand{\\G}{\\Gamma}
\\newcommand{\\g}{\\gamma}
\\newcommand{\\B}{\\mb{B}}
\\newcommand{\\m}{\\times}
\\newcommand{\\N}{\\mb{N}}
\\newcommand{\\I}{\\mb{I}}
\\newcommand{\\H}{\\mc{H}}
\\newcommand{\\R}{\\mb{R}}
\\newcommand{\\s}{\\sigma}
\\newcommand{\\e}{\\varepsilon}
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
\\newcommand{\\qed}{\\ \\ \\blacksquare}
\\newcommand{\\c}{\\overline}
\\newcommand{\\dg}{\\dagger}
\\newcommand{\\dd}{\\mathrm{d}}
\\newcommand{\\pd}{\\partial}
$$





The physically realistic thing to do would be to make the piston an inertial body, meaning that it has its own momentum. If the particle is doing work on the piston by pushing it, then the piston must be climbing a potential gradient. Then, as an inertial body, the piston should fall back down the gradient when not being pushed.

I also tried settling this matter by going to the source: [Szilard's original paper](http://fab.cba.mit.edu/classes/863.18/notes/computation/Szilard-1929.pdf). Szilard specifies that the piston is forcibly moved by an operator. This can be modeled as a wall that moves in a predefined way, regardless of its interaction with the particle. That is certainly easier to model on a computer.

Szilard specifies that the expansion is [isothermal](https://en.wikipedia.org/wiki/Isothermal_process), which means the particle regains lost KE (on average) by interacting with oscillating particles in the walls of the container. However, I am modeling the expansion as [isentropic](https://en.wikipedia.org/wiki/Isentropic_process) to avoid the issue of environmental noise (see {{< locallink "Why Doesn't Uncopying Defeat The 2nd Law" "defining-environmental-noise" >}}). That means the particle does not exchange KE with the walls of the container, and so the particle loses net KE over time.


# Inertial Piston Model

Like last time I am modeling this in one spatial dimension. The piston and particle each have one position coordinate. The container has a length, with "caps" on each end.

If the piston is pushing a mass $M$ up against gravity, then the potential field has a constant slope $g$. Then the motion of the piston is described by $M \\ddot{x}=-g$, which gives us a parabola (think ball thrown in the air).

The particle experiences no forces, except for elastic collisions with the walls of the container and the piston. We can use the [1D elastic collision formula](https://en.wikipedia.org/wiki/Elastic_collision#One-dimensional_Newtonian):

$$
\\pmatrix{u\_f\\\\v\_f}=\\frac{1}{M+m}\\pmatrix{M-m & 2m \\\\ 2M & m-M}\\pmatrix{u\_i\\\\v\_i}
$$

where $M$ is the mass of the piston (i.e. the mass it is pushing), $m$ is the mass of the particle, $v\_i,v\_f$ are the initial and final velocities of the particle before and after the collision, and $u\_i,u\_f$ are the initial and final velocities of the piston before and after collision.

When the particle collides with a fixed wall, its velocity sign changes, i.e. $v\_f = -v\_i$.

To have the particle push the piston slowly over the course of many back-and-forth bounces, the piston's mass should be greater than the particle's, and the particle's velocity should be greater than piston.

For example, here is a simulation with the following settings
piston: (mass) $M=1$ and (initial velocity) $u\_0 = 0$
particle: (mass) $m = 1/10$ and (initial velocity) $v\_0=5$
![](</Pasted image 20220215093814.png> "Blue is the particle's trajectory, and orange is the piston's trajectory. The particle bounces off both the piston and the fixed wall at position -1. The behavior of the combined system is locally chaotic, and globally seems to oscillate.")

With a much lower particle mass and much higher initial particle velocity, we see less chaotic behavior and a more stable oscillation:
piston: (mass) $M=1$ and (initial velocity) $u\_0 = 0$
particle: (mass) $m = 1/100$ and (initial velocity) $v\_0=20$
![](</Pasted image 20220215093846.png>)

To avoid this sort of oscillation, I should have the piston mass decrease as it is pushed up, corresponding to [adiabatic (isentropic) expansion](https://en.wikipedia.org/wiki/Isentropic_process), where the entropy of the gas remains fixed as it expands. The gas does not absorb thermal energy from its container, and so it cools as it transfers KE to the piston. In order to maintain approximate equilibrium through out the change (making it a [quasistatic process](https://en.wikipedia.org/wiki/Quasistatic_process)), the piston mass is slowly decreased so that the gas pressure and piston force opposing it always in balance.

I tried running the same simulation where the piston mass is the following function of the container length: $M(L)=M\_0\\cdot\\par{\\frac{L\_0}{L}}^\\gamma$ where $\\gamma=1$. I got this formula from the [ideal gas isentropic relation](https://en.wikipedia.org/wiki/Isentropic_process#Table_of_isentropic_relations_for_an_ideal_gas) between pressure and volume: $\\frac{P\_f}{P\_i}=\\par{\\frac{V\_i}{V\_f}}^\\gamma$. Pressure of a single particle applied to a point (end of the 1D container) is just its force, and the volume of the 1D container is its length. This resulted in very similar looking particle-piston trajectories as before, with oscillatory behavior. I suspect I would need to have the piston mass decrease as it is pushed up the potential slope, but not increase as it falls down the potential slope.

At any rate, a quick workaround is to fix the piston in place once it reaches its maximally expanded position. Like this:

![](</Pasted image 20220215103320.png>)
Like in {{< locallink "Reversible Szilard Cycle Problem" "part-ii-information-is-never-lost" >}}, I sampled a thousand initial particle states on each side of the container - left side as red and right side as blue.

<video controls autoplay loop src="../../szilard_inertial_piston.mp4" caption="" width="100%"></video>
It seems that this too results in disjoint state regions, and so the which-side information is again preserved. What's also apparent is that the state regions are shrinking. [Liouville's theorem](https://en.wikipedia.org/wiki/Liouville%27s_theorem_(Hamiltonian)) guarantees that state volume will be conserved in a closed system. However, here there is energy being lost to the piston. If we plotted the joint state space of the particle and piston we would see that the total state region does not shrink. 

Since the particle's state region is shrinking, that implies there is state uncertainty being moved into the piston dimension. What does that imply about the reversibility of this process? A process is thermodynamically reversible if both the system undergoing the process and its environment can be reset to their joint initial state. If uncertainty is transferred from the particle to the piston (piston's state region has increased in volume), is that reversible? Since all of the transferred uncertainty is accumulating in a single degree of freedom (the total energy absorbed from the particle), it should be possible in principle to transfer that uncertainty back to the particle. It is only when uncertainty becomes spread out among many degrees of freedom (like heat transfer from many particles to many particles) that this transfer becomes irreversible (why? - An exercise left to the reader).




# Controlled Piston Model

## Particles colliding with moving walls


When you forcibly move a wall into particles, you transfer KE to them. This is why compressing a gas adds heat energy (average KE) to the gas.
The time reversal of this process is forcibly expanding a gas by pulling the wall away from the particles. This must result in KE extraction from the particles.

We see this bear out in the low-level Newtonian mechanics of collision with the formula $v\_f = 2u-v\_i$, where $v\_i$ is the incoming (initial) velocity of the particle before wall collision, $v\_f$ is the outgoing (final) velocity of the particle after wall collision, and $u$ is the fixed velocity of the wall.

This formula can be derived from the [one-dimensional elastic collision formula](https://en.wikipedia.org/wiki/Elastic_collision#One-dimensional_Newtonian) (see [#Inertial Piston Model](#inertial-piston-model)) by taking the mass of the wall to infinity ([reference](https://www.physicsforums.com/threads/elastic-collision-against-a-moving-wall.236652/#post-2347189)):


Taking the limit as $m\_u \\to \\infty$, we get

$$
\\lim\_{M\\to\\infty}\\frac{1}{M+m}\\pmatrix{M-m & 2m \\\\ 2M & m-M} = \\pmatrix{1 & 0 \\\\ 2 & -1}
$$

giving us 
$$
\\pmatrix{u\_f\\\\v\_f}=\\pmatrix{1 & 0 \\\\ 2 & -1}\\pmatrix{u\_i\\\\v\_i} = \\pmatrix{u\_i\\\\2u\_i-v\_i}
$$

where $u=u\_i=u\_v$.

## Simulation

In this simulation the piston has infinite mass and moves along a predefined path, representing an external operator controlling the movement of the piston. The particle collides elastically with the piston using the formula $v\_f = 2u-v\_i$, where $u$ is the velocity of the piston. If the piston is moving away from the particle (in the same direction as $v\_i$), we see that $\\abs{v\_f}<\\abs{v\_i}$ and so the particle loses KE.

![](</Pasted image 20220217150254.png> "An example particle trajectory (blue) with a piston (orange) moving along a predefined path. When the particle collides with the moving piston it loses KE.")

Here I sample an ensemble of initial particles. The blue particles bounce off the blue piston and the red particles bounce off the red piston. Since the blue and red pistons follow the same path for all particles (of the same color), I can visualize the pistons superimposed on the ensemble. Since the piston's predefined movement depends on which side (which color) the particle is on, this controll "program" requires the which-side bit stored in memory.
<video controls autoplay loop src="../../szilard_piston_fixed_movement.mp4" caption="" width="100%"></video>
Clearly the state regions overlap over time, and so the which-side information is no longer present in the particle system at the end of the piston expansion.

Question: Why do some interaction models preserve which-side information, while other interaction models do not?