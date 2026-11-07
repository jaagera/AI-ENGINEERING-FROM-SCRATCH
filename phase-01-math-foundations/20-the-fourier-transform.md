> Every signal is a sum of sine waves. The Fourier transform tells you which ones.

* The DFT(Discrete Fourier Transform) produces N frequency coefficients.

> Windowing:
The DFT assumes the signal is periodic -- it treats the NN samples as one period of an infinitely repeating signal. If the signal does not start and end at the same value, this creates a discontinuity at the boundary, which shows up as spurious high-frequency content. This is called spectral leakage.

Windowing reduces leakage by tapering the signal to zero at both ends before computing the DFT.

> The Short-Time Fourier Transform (STFT) solves this by computing FFTs on overlapping windows of the signal. 

