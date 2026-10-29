> Probability is the language AI uses to express uncertainty.

Probability Mass Functions(PMF): has a specific probability that you can read off directly

Probability Density Functions(PDF): Probability comes from integrating the density over an interval.
(VAE (Variational Autoencoder))
# NOTE: “Probability is the language AI uses to express uncertainty.”

### Sampling

Sampling means drawing random values from a distribution. In ML:
- Dropout randomly samples which neurons to zero out
- Data augmentation samples random transformations
- Language models sample the next token from the predicted distribution
- Diffusion models sample noise and progressively denoise

Sampling from arbitrary distributions requires techniques like inverse transform sampling, rejection sampling, or the reparameterization trick (used in VAEs).
