# AptitudeForAll – Interactive Quiz Dashboard

A static, client‑side dashboard to browse all aptitude‑quiz PDFs, mark them as *Done*, and see progress per category and overall. Works fully on **GitHub Pages** – no server required.

## 🌐 Live Demo
Once GitHub Pages is enabled, the site will be available at:

**https://harshu114.github.io/AptitudeForAll/**

*(Replace the URL if you publish under a different username / repository name.)*

## ✨ Features
- **Category buttons** – click a category to expand/collapse its PDF list.  
- **Checkbox per PDF** – marks a quiz as completed; state is saved in `localStorage` (persists across visits on the same browser).  
- **Progress bars** – each category shows *X / Y completed* and a percentage; an overall bar at the bottom aggregates everything.  
- **Zero‑dependency** – single `index.html` with embedded CSS & vanilla JS.  
- **GitHub Pages ready** – just push to `main`/`master` and enable Pages on the `root` folder.

## 📂 Repository Structure
```
├─ index.html          # Dashboard (HTML + CSS + JS)
├─ Arguments/          # PDF folders (one per topic)
├─ Average/
├─ Blood/
├─ … (all other topic folders)
└─ README.md
```

## 🚀 Deploy to GitHub Pages
1. Push this repo to GitHub (already done).  
2. In the repository **Settings → Pages** → *Build and deployment* → **Source**: `Deploy from a branch`.  
3. Choose branch **`master`** (or `main`) and folder **`/ (root)`**.  
4. Save – GitHub will publish the site at the URL shown above (may take a minute).

## 🛠 Local Development
Just open `index.html` in a browser – no build step, no server needed.

## 📝 License
MIT – feel free to reuse, adapt, and share.