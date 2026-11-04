> Sampling is how AI explores the space of possibilities

Main aim:
To learn how a computer turns plain random numbers into samples from any distribution, and how language models use this to pick the next word.

* Monte Carlo Estimation

Monte Carlo estimation approximates integrals by averaging random samples. The law of large numbers guarantees convergence.

* Gibbs Sampling

Gibbs sampling is a special case of MCMC for multivariate distributions. Instead of proposing a move in all dimensions at once, it updates one variable at a time from its conditional distribution.

* Top-k Sampling

Top-k sampling restricts the candidate set to the kk tokens with the highest probabilities, then renormalizes and samples from that restricted set.

> Reparameterization Trick (Used in VAEs)

Variational autoencoders (VAEs) learn by encoding inputs into a distribution in latent space, sampling from that distribution, and decoding the sample back. The problem: you cannot backpropagate through a sampling operation.

* Gumbel-Softmax produces a continuous relaxation of a discrete sample. The output is a probability vector (soft one-hot) instead of a hard one-hot. Gradients flow through the softmax. During the forward pass in training, you can use the "straight-through" estimator: use the hard argmax for the forward pass but the soft Gumbel-Softmax gradients for the backward pass.

Applications:

    Discrete latent variables in VAEs
    Neural architecture search (choosing discrete operations)
    Hard attention mechanisms
    Reinforcement learning with discrete actions

### Gibbs Sampling

Gibbs sampling is a special case of MCMC for multivariate distributions. Instead of proposing a move in all dimensions at once, it updates one variable at a time from its conditional distribution.

* NeRF (Neural Radiance Fields) uses stratified sampling along camera rays
