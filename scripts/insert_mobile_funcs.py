import sys
sys.stdout.reconfigure(encoding='utf-8')

file_path = r"3_바이럴분석_SaaS_ViralScope\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

funcs = """
    // Mobile Sidebar Drawer Navigation Controls
    function toggleMobileSidebar() {
      var sb = document.querySelector(".sidebar");
      var backdrop = document.getElementById("sidebarBackdrop");
      if (sb) sb.classList.toggle("mobile-open");
      if (backdrop) backdrop.classList.toggle("active");
    }

    function closeMobileSidebar() {
      var sb = document.querySelector(".sidebar");
      var backdrop = document.getElementById("sidebarBackdrop");
      if (sb) sb.classList.remove("mobile-open");
      if (backdrop) backdrop.classList.remove("active");
    }
"""

if "function toggleMobileSidebar()" not in text:
    text = text.replace("function selectCategory(key) {", funcs + "\n    function selectCategory(key) {\n      closeMobileSidebar();")
    print("Successfully inserted function toggleMobileSidebar() and function closeMobileSidebar()!")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)
