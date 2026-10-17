Virtual environments They isolate project dependencies so different projects can use different package versions

A file that pins every package to an exact version for reproducible installs


N.B: UV is the fastest Python package manager(10-100x faster than pip). it handles virtual environments, python versions, and dependency resolution in one tool.

Lockfiles:
A lockfile pins every dependency (including transitive ones) to exact versions. This guarantees reproducibility: anyone who installs from the lockfile gets exactly the same packages.


1. Run which python and confirm it shows .venv/bin/python, not /usr/bin/python
2. Pip installs can break conda’s dependency tracking, causing hard-to-debug conflicts
3. PyTorch was installed with a CUDA version incompatible with your GPU driver

**Key Terms**
Term	                What people say	            What it actually means
Virtual environment	    "A venv"	                An isolated directory containing a Python interpreter and packages, separate from the system Python
Lockfile	            "Pinned dependencies"	       A file listing every package and its exact version, guaranteeing identical installs across machines
pyproject.toml      	"The new setup.py"	            The standard Python project configuration file, replacing setup.py/setup.cfg/requirements.txt
Transitive dependency	"A dependency of a dependency"	    Package B depends on C; if you install A which depends on B, C is a transitive dependency of A
CUDA mismatch	        "My GPU isn't working"              	PyTorch was compiled for a different CUDA version than what your GPU driver supports