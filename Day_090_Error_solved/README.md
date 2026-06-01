## Day 90: Troubleshooting VS Code Jupyter Notebook Kernels
Today, I faced and resolved a frustrating issue involving Jupyter Notebook (.ipynb) execution within a VS Code virtual environment.
### Key Learnings
 * **The Problem**: Running notebooks inside a newly created isolated virtual environment often fails silently or throws kernel connection errors because required execution dependencies are missing.
 * **The Root Cause**: VS Code requires the ipykernel package to be explicitly installed inside the active virtual environment to register it as a valid Jupyter kernel and bridge notebook cells with the environment's Python interpreter.
 * **The Solution**:
   1. Selected the correct interpreter path matching the virtual environment in VS Code.
   2. Opened the terminal, activated the environment, and ran: pip install ipykernel
   3. Refreshed and selected the local environment kernel in the top-right notebook UI.
Day 90 complete—debugging the development environment like a pro! 🚀
