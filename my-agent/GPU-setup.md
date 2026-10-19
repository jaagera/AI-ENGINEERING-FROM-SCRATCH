NOTE: Training on CPU is fine for learning. Training for real needs a GPU(Graphic Processing Unit)

Think of this lesson as answering one question: where will my heavy computing run? Everything else follows from that.

# The four objectives, explained
1. Verify your local GPU (nvidia-smi and PyTorch)

You need to know two separate things:

nvidia-smi (terminal command) asks the driver: “Is there a GPU, and what is it?” It shows the GPU name, memory, driver version, and the highest CUDA version the driver supports.
torch.cuda.is_available() (Python) asks PyTorch: “Can you actually use that GPU?”

Why both? They can disagree. If nvidia-smi works but PyTorch prints False, you probably installed a CPU-only PyTorch build. You learned this earlier in the quiz.

You should be able to: read the output of nvidia-smi and say the GPU name and how much VRAM it has.

2. Configure Colab with a T4(Technology and AI)

In Colab: Runtime > Change runtime type > T4 GPU. Then run !nvidia-smi to confirm. The ! runs a terminal command inside a notebook cell.

The key habit: always confirm the GPU is really attached before running anything. If you forget to switch the runtime, your code silently runs on CPU and your benchmark means nothing.

A T4 has about 15 GB of VRAM. Free Colab has limits, so sessions can disconnect, and anything stored on the runtime can disappear. Save your work to Drive or download it.

3. Benchmark CPU vs GPU

This is the hands-on proof of everything above. You multiply two big matrices on CPU, then on GPU, time both, and compute:

speedup = cpu_time / gpu_time

# Three concepts you’re expected to understand here:
1. Warm-up: the first GPU operation pays a one-time start-up cost (loading CUDA, allocating memory). That’s why the lesson says to run it twice and compare the second numbers.
2. Synchronization(Making two or more things act at the same time): GPU work is asynchronous(Allows other tasks to execute without waiting for the first task). Python sends the job and moves on immediately. Without torch.cuda.synchronize(), your timer stops before the GPU is done, giving a fake speedup.
3. Fair comparison: same matrix size, same operation, same number of repetitions on both devices.

A normal result is roughly 10x to 100x or more. A very small speedup usually means you timed it wrong, the matrices are too small, or the code is secretly running on CPU.

4. Estimate the largest model that fits in VRAM

# The rule of thumb:
Model size	fp16 weights	Fits on a 15 GB T4?
1B	        ~2 GB	        Yes, easily
3B	        ~6 GB	        Yes, comfortably
7B	        ~14 GB	        Barely, no room to spare
13B	        ~26 GB	        No

# Two extensions worth knowing:
Quantization shrinks models: 8-bit uses 1 byte per parameter, 4-bit about 0.5. A 7B model in 4-bit needs only ~4 GB.
Training needs much more than inference, roughly 16 bytes per parameter with the Adam optimizer, so training is limited to far smaller models than running them.