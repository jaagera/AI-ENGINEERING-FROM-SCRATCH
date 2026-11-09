> Randomness with structure. The math behind random walks, Markov chains, and diffusion models.

* NOTE: The forward process is a Markov chain. The reverse process is a learned Markov chain running backward.

> Markov Chains

A Markov chain is a system that transitions between states according to fixed probabilities. The key property: the next state depends only on the current state, not on the history.

> MCMC: Markov Chain Monte Carlo


> The Libraries (The Tools)

• PyMC. A popular Python library used for Bayesian statistical modeling. It lets you write probability models using clean, readable Python code.
• NumPyro. A faster, lightweight alternative to PyMC built on top of Google's JAX framework. It does the exact same kind of statistical modeling as PyMC, but runs much faster on GPUs and large datasets.

The Algorithms (The Engines)

• MCMC (Markov Chain Monte Carlo). A family of algorithms used to map out complex probability distributions. Imagine walking blindfolded through a hilly landscape and taking notes on your elevation at every step to build a map of the terrain. MCMC "walks" through possible parameter values, spending more time in areas that are most likely to be true based on your data.
• NUTS (No-U-Turn Sampler). A specific, high-speed type of MCMC algorithm. Older MCMC methods often wander around randomly and waste time doubling back on themselves. NUTS uses calculus (gradients) to slide smoothly toward high-probability areas and automatically stops before making a "U-turn," making it the gold standard for modern statistical modeling.

> How They Work Together

When you build a model in PyMC or NumPyro, you define your data and your initial guesses (priors). You then hit "run," and the library uses NUTS (an MCMC engine) under the hood to generate thousands of realistic samples. You can look at those samples to see the most likely outcome along with a reliable range of uncertainty.

* SGLD (Stochastic Gradient Langevin Dynamics) combines mini-batch gradient descent with Langevin noise. 