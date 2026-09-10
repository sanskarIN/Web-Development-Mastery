const fs = require('fs');

const filePath = 'index.html';
const cssPath = 'style.css';
const jsPath = 'script.js';

console.log("Reading index.html...");
const content = fs.readFileSync(filePath, 'utf8');
const lines = content.split(/\r?\n/);

let outHtml = [];
let outCss = [];
let outJs = [];

let state = 'HTML';

for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    if (state === 'HTML' && /^\s*<style id="baseStyles">\s*$/.test(line)) {
        state = 'CSS';
        outHtml.push('  <link rel="stylesheet" href="style.css">');
        continue;
    } else if (state === 'CSS' && /^\s*<\/style>\s*$/.test(line)) {
        state = 'HTML';
        continue;
    } else if (state === 'HTML' && /^\s*<script>\s*$/.test(line) && i + 1 < lines.length && /THEME DATA/.test(lines[i + 1])) {
        state = 'JS';
        outHtml.push('  <script src="script.js"></script>');
        continue;
    } else if (state === 'JS' && /^\s*<\/script>\s*$/.test(line)) {
        state = 'HTML';
        continue;
    }

    if (state === 'CSS') {
        outCss.push(line);
    } else if (state === 'JS') {
        outJs.push(line);
    } else {
        outHtml.push(line);
    }
}

console.log("Writing CSS file...");
fs.writeFileSync(cssPath, outCss.join('\n'), 'utf8');

console.log("Writing JS file...");
fs.writeFileSync(jsPath, outJs.join('\n'), 'utf8');

console.log("Updating HTML file...");
fs.writeFileSync(filePath, outHtml.join('\n'), 'utf8');

console.log("✅ Success! The CSS and JS have been perfectly separated.");

// Code optimized and documented by Sanskar Developer
