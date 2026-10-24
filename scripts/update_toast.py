import os

script_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(script_dir, '..', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

text_norm = text.replace('\r\n', '\n')

old_part = """    function showToast(msg, type) {
      var banner = document.getElementById("toastBanner");
      banner.className = "toast-banner " + (type || "success");
      document.getElementById("toastMsg").innerText = msg;
    }
    function hideToast() {
      document.getElementById("toastBanner").style.display = "none";
    }"""

new_part = """    var toastTimer = null;
    function showToast(msg, type) {
      var banner = document.getElementById("toastBanner");
      if (!banner) return;
      banner.className = "toast-banner " + (type || "success");
      banner.style.display = "flex";
      var msgEl = document.getElementById("toastMsg");
      if (msgEl) msgEl.innerText = msg;
      if (toastTimer) clearTimeout(toastTimer);
      toastTimer = setTimeout(function() {
        hideToast();
      }, 4500);
    }
    function hideToast() {
      var banner = document.getElementById("toastBanner");
      if (banner) banner.style.display = "none";
    }"""

if old_part in text_norm:
    text_norm = text_norm.replace(old_part, new_part)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(text_norm)
    print("showToast updated successfully!")
else:
    print("old_part not found!")
