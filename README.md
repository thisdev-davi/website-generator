# Static Site Generator - Python

A custom-built static site generator written in Python that converts Markdown content into a fully responsive, Dracula-themed HTML website.


## 1. Prerequisites
*   python 3.x

## 2. Adding Content
Create Markdown files inside the `content/` directory.
*   `content/index.md` becomes `public/index.html` (Home page).
*   `content/about.md` becomes `public/about.html`.

## 3. Building the Site
Run the build script from the root directory:

```bash
./main.sh
```
<br>

This command will:
1. Copy static/ files to public/.
2. Convert all `.md` files in content/ to `.html` in public/.

## Running Tests

To run the unit tests for the Markdown parser:

```bash
cd src
python3 -m unittest discover -s tests
```
