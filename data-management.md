Data is the fuel. How you manage it determines how fast you go.

# HOW TO BUILD DATASETS
1. Install the datasets library
2. Load a dataset
3. Stream larage datasets
4. dataset formats: i.e the library use Apache Arrow under the hood.
5. Data splits: Every ML projects needs three splits which include: 
TRAIN: The model learns from this (typically 80%)
VALIDATION: You check progress during training (typically 10%)
TEST: Final evaluation after training is done (typically 10%)
6. DOWNLOAD AND CACHE MODELS: Modesl are large files. The "huggingface_hub" library handles downloading and caching. 
7. HANDLE LARGE FILES: Model weights and large datasetes should not go into git. Three options: (a). .gitignore(simplest)
(b). Git LFS(track large files in git)
(c). DVC (data version control)

Approach	Complexity	        Best For
.gitignore	Low	                Personal projects, downloaded data you can re-fetch
Git LFS	    Medium	            Teams sharing model weights via git
DVC	        High	            Reproducible experiments, large datasets, teams

For this course, .gitignore is enough. Use DVC when you need to reproduce exact experiments across machines.
8. STORAGE PATTERNS: Local storage works for datasets under ~10 GB. The HF cache handles this automatically.

Cloud storage is for anything larger or shared across machines

# Format comparison:
Format	Size	Read Speed	Best For
CSV	    Large	Slow	    Human readability, spreadsheets
JSON	Large	Slow	    APIs, nested data
Parquet	Small	Fast	    Analytics, columnar queries
Arrow	Small	Fastest	    In-memory processing (what datasets uses internally)

For AI work, Parquet is the best storage format. Arrow is what you work with in memory. CSV and JSON are for interchange.

# The five steps as a loop
 Find → Download → Convert → Split → Version
  ↑                                    |
  └──────── rerun when data changes ───┘
Find: Hugging Face Hub, Kaggle, or your own data. Check the license.
Download: with code (load_dataset("imdb")), never by clicking, so anyone can repeat it.
Convert: raw CSV/JSON to a better format like Parquet (fast, typed, compressed) or JSONL (standard for LLM data).
Split: train / validation / test, with a fixed random seed, and no overlap between them (data leakage).
Version: git stores a tiny pointer, DVC stores the real data in cloud storage, so every commit maps to an exact dataset.