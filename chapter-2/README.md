# Chapter 2 reading companion

Open `index.html` in a browser. Begin with **Start here: math & English** (`00-start.html`).

There are 13 pages: an overview, a math/English warm-up, 10 lessons, and a practice page with a guide to Exercises 2.1–2.20. The lessons use simple English, explain new words, show small calculation steps, and separate first-reading ideas from second-reading detail.

Everything runs locally and offline. No installation or server is required. Keep this folder next to `mml-book.pdf` so the book links work. Progress is stored in the browser when local storage is permitted. The text and expandable hints work without JavaScript; diagrams, quiz, and saved progress use JavaScript.

The source PDF is the January 15, 2024 draft of *Mathematics for Machine Learning*, Chapter 2, printed pp. 17–69 (PDF pages 23–75). The practice guide contains hints and selected answers, not complete solutions for every exercise.

## Editing and checks

- Edit `build.py` for lesson content and `beginner.py` for the warm-up and reading support.
- Run `python3 chapter-2/build.py` from the workspace root to regenerate the HTML.
- Run `python3 chapter-2/verify.py` for local links and selected exact mathematical checks.
- Run `node --check chapter-2/assets/app.js` to check JavaScript syntax.
- Run `node chapter-2/check-browser.cjs` for browser checks, if Google Chrome and Node 22+ are installed. It uses a fresh temporary browser profile and saves review screenshots under `/tmp`.
