> The square root of -1 is not imaginary. It is the key to rotations, frequencies, and half of signal processing.

* Without understanding complex numbers, you cannot understand the Discrete Fourier Transform. You cannot understand FFT. You cannot understand how RoPE (Rotary Position Embedding) works in modern language models. You cannot understand why sinusoidal positional encodings in the original Transformer paper use the frequencies they do.

> What is a complex number?

A complex number has two parts: a real part and an imaginary part.

* Why Euler's formula matters for ML

Euler's formula says that eiθeiθ traces the unit circle as θθ varies. At θ=0θ=0, you are at (1,0)(1,0). At θ=π/2θ=π/2, you are at (0,1)(0,1). 
This means complex exponentials ARE rotations. And rotations are everywhere in signal processing and ML.

> Discrete Fourier Transform. The DFT decomposes a signal into components at these NN equally-spaced frequencies.

* RoPE (Rotary Position Embedding) takes this further. It explicitly multiplies query and key vectors by complex rotation matrices.

