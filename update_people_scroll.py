with open('people.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = """document.addEventListener('DOMContentLoaded', () => {
  const urlParams = new URLSearchParams(window.location.search);
  const panelParam = urlParams.get('panel');
  if (panelParam) {
    filterByPanel(panelParam);
  } else {
    renderDirectory();
  }
});"""

replacement = """document.addEventListener('DOMContentLoaded', () => {
  const urlParams = new URLSearchParams(window.location.search);
  const panelParam = urlParams.get('panel');
  if (panelParam) {
    filterByPanel(panelParam);
    setTimeout(() => {
      const dirEl = document.getElementById('directory');
      if (dirEl) {
        dirEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }, 150);
  } else {
    renderDirectory();
  }
});"""

if target in text:
    text = text.replace(target, replacement, 1)
    with open('people.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("people.html updated with smooth scroll to directory!")
else:
    print("target not found in people.html")
