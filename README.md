# SGPA & CGPA Calculator

This repository contains:

- `index.html` — a single-file web UI for calculating SGPA (semester grade point average) and CGPA (cumulative GPA). Works in any modern browser. Saves semesters in browser localStorage.
- `sgpa_cgpa.py` — simple command-line calculator (Python 3).
- `.gitignore` and `LICENSE` (MIT).

Grade scale
- Default 10-point mapping is used in both files (A+ = 10, A = 9, B+ = 8, B = 7, C = 6, D = 5, F = 0). Edit the mapping in the code if your institution uses a different scale.

How to use (web)
1. Download or clone the repo.
2. Open `index.html` in your browser.
3. Add courses (name optional), enter credits and select grade.
4. Click "Calculate SGPA" and then "Add semester" to save.
5. Use "Calculate CGPA" to compute cumulative GPA across saved semesters.
6. To publish, enable GitHub Pages for the repository (see below).

How to use (CLI)
1. Ensure Python 3 is installed.
2. Run: `python3 sgpa_cgpa.py`
3. Follow the prompts.

Publish with GitHub Pages
1. Push these files to a GitHub repository (example name: `sgpa-cgpa-calculator`).
2. On GitHub: Settings → Pages → Source: select `main` branch and `/ (root)`.
3. Visit: `https://<your-github-username>.github.io/<repo-name>/` after a minute or two.

Quick git commands (local -> new remote)
```bash
mkdir sgpa-cgpa-calculator
cd sgpa-cgpa-calculator
# copy files into this folder
git init
git add .
git commit -m "Initial commit: SGPA & CGPA calculator"
# create a repo on GitHub (web) and then add the remote, for example:
git remote add origin git@github.com:<your-username>/sgpa-cgpa-calculator.git
git branch -M main
git push -u origin main
```

License
- This project is provided under the MIT License (see LICENSE).
