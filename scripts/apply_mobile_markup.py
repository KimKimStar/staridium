import sys, re
sys.stdout.reconfigure(encoding='utf-8')

file_path = r"3_바이럴분석_SaaS_ViralScope\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add Mobile Backdrop right after <body>
if '<div class="sidebar-backdrop"' not in content:
    content = content.replace('<body>', '<body>\n  <!-- Mobile Sidebar Backdrop Overlay -->\n  <div class="sidebar-backdrop" id="sidebarBackdrop" onclick="closeMobileSidebar()"></div>')
    print("Added #sidebarBackdrop overlay to <body>")

# 2. Add Mobile Close Button inside <aside class="sidebar"> -> .sidebar-header
if 'mobile-sidebar-close' not in content:
    sidebar_header_target = '<div class="sidebar-header" onclick="location.reload()">'
    sidebar_header_replace = '<div class="sidebar-header">\n        <button type="button" class="mobile-sidebar-close" id="mobileSidebarClose" onclick="event.stopPropagation(); closeMobileSidebar();" aria-label="메뉴 닫기">✕</button>'
    content = content.replace(sidebar_header_target, sidebar_header_replace)
    print("Added mobile-sidebar-close button inside sidebar-header")

# 3. Add Mobile Menu Hamburger Button inside <header>
if 'mobileMenuBtn' not in content:
    header_left_target = '<div class="header-left">'
    header_left_replace = '''<div class="header-left">
          <!-- Mobile Hamburger Menu Button -->
          <button type="button" class="mobile-menu-btn" id="mobileMenuBtn" onclick="toggleMobileSidebar()" aria-label="전체 카테고리 메뉴 열기">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="3" y1="12" x2="21" y2="12"></line>
              <line x1="3" y1="6" x2="21" y2="6"></line>
              <line x1="3" y1="18" x2="21" y2="18"></line>
            </svg>
          </button>'''
    content = content.replace(header_left_target, header_left_replace)
    print("Added mobileMenuBtn hamburger button inside header-left")

# 4. Insert Comprehensive Mobile Responsive CSS before </style>
mobile_css = """
    /* ==============================================================
       COMPREHENSIVE MOBILE RESPONSIVE ENGINE (Smartphones & Tablets)
       ============================================================== */
    .mobile-menu-btn {
      display: none;
      align-items: center;
      justify-content: center;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--surface-border);
      border-radius: 9px;
      color: #e2e8f0;
      width: 40px;
      height: 40px;
      cursor: pointer;
      flex-shrink: 0;
      transition: all 0.2s ease;
    }
    .mobile-menu-btn:hover, .mobile-menu-btn:active {
      background: rgba(139, 92, 246, 0.2);
      border-color: var(--accent);
      color: white;
    }

    .mobile-sidebar-close {
      display: none;
      position: absolute;
      top: 14px;
      right: 14px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--surface-border);
      color: #cbd5e1;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      cursor: pointer;
      align-items: center;
      justify-content: center;
      font-size: 15px;
      font-weight: 700;
      transition: all 0.2s ease;
      z-index: 10;
    }
    .mobile-sidebar-close:hover {
      background: rgba(239, 68, 68, 0.2);
      color: #ef4444;
      border-color: rgba(239, 68, 68, 0.4);
    }

    .sidebar-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(6px);
      -webkit-backdrop-filter: blur(6px);
      z-index: 999;
      display: none;
      opacity: 0;
      transition: opacity 0.28s ease;
    }
    .sidebar-backdrop.active {
      display: block;
      opacity: 1;
    }

    @media (max-width: 860px) {
      body {
        overflow-x: hidden;
      }
      .app-layout {
        display: block;
        width: 100%;
        min-height: 100vh;
        overflow-x: hidden;
      }

      /* Mobile Off-Canvas Drawer Sidebar */
      .sidebar {
        position: fixed;
        top: 0;
        left: 0;
        bottom: 0;
        width: 290px;
        max-width: 86vw;
        height: 100vh;
        z-index: 1000;
        transform: translateX(-100%);
        transition: transform 0.28s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 12px 0 35px rgba(0, 0, 0, 0.85);
        background: #080d1a;
      }
      .sidebar.mobile-open {
        transform: translateX(0);
      }
      .sidebar-header {
        position: relative;
        padding-right: 48px;
      }
      .mobile-menu-btn {
        display: inline-flex !important;
      }
      .mobile-sidebar-close {
        display: inline-flex !important;
      }

      /* Main Wrap & Layout Containers */
      .main-wrap {
        width: 100%;
        min-width: 0;
        overflow-x: hidden;
      }
      .content-container {
        padding: 12px 14px;
        width: 100%;
        max-width: 100%;
        box-sizing: border-box;
      }

      /* Header Layout on Mobile */
      header {
        padding: 12px 14px;
        flex-wrap: wrap;
        gap: 10px;
      }
      .header-left {
        width: 100%;
        display: flex;
        align-items: center;
        gap: 10px;
      }
      .header-left #currentTopicLabel {
        font-size: 14.5px !important;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        flex: 1;
      }
      .header-center {
        width: 100% !important;
        max-width: 100% !important;
        order: 2;
      }
      .search-input-wrap {
        width: 100% !important;
      }
      .search-input {
        width: 100% !important;
        font-size: 13.5px;
        padding: 10px 42px 10px 14px;
        height: 42px;
      }
      .header-actions {
        width: 100%;
        order: 3;
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 8px;
        padding-top: 6px;
        border-top: 1px solid rgba(255, 255, 255, 0.05);
      }
      .refresh-widget {
        font-size: 11px;
        padding: 4px 8px;
      }
      .btn-manual-refresh {
        display: none !important;
      }
      .btn-api-key, .btn-upgrade {
        padding: 6px 10px;
        font-size: 11px;
      }

      /* Minimal Control Bar on Mobile */
      .minimal-control-bar {
        flex-direction: column;
        align-items: stretch;
        gap: 12px;
        padding: 10px 0 16px;
      }
      .control-bar-left {
        width: 100%;
        display: flex;
        flex-direction: column;
        gap: 8px;
      }
      .control-bar-right {
        width: 100%;
      }
      .minimal-select-container {
        width: 100%;
      }
      .minimal-select {
        width: 100%;
        padding: 10px 32px 10px 12px;
        font-size: 13px;
      }

      /* Video Grid: 1 Column on Mobile for Maximum Readability */
      .video-grid {
        grid-template-columns: 1fr !important;
        gap: 18px;
      }
      .video-card {
        width: 100%;
        max-width: 100%;
        padding: 14px;
        border-radius: 16px;
        box-sizing: border-box;
      }
      .thumbnail-wrap {
        max-height: 480px;
        margin-bottom: 12px;
        border-radius: 12px;
      }
      .card-title {
        font-size: 15px;
        line-height: 1.45;
        margin-bottom: 8px;
      }
      .btn-card-hook-primary {
        width: 100%;
        height: 44px;
        font-size: 13px;
        justify-content: center;
      }

      /* Full Screen / Bottom Sheet Modal on Mobile */
      .modal-overlay {
        padding: 0;
        align-items: flex-end;
      }
      .modal-container {
        width: 100%;
        height: 95vh;
        max-height: 95vh;
        border-radius: 20px 20px 0 0;
        border: none;
        border-top: 1px solid rgba(255, 255, 255, 0.15);
      }
      .modal-header {
        padding: 12px 16px;
      }
      #modalVideoTitle {
        font-size: 13.5px !important;
        max-width: 78%;
      }
      .modal-tabs-bar {
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        padding: 6px 12px;
        gap: 6px;
        white-space: nowrap;
      }
      .m-tab-btn {
        padding: 8px 12px;
        font-size: 12px;
        flex-shrink: 0;
      }
      .modal-body-split {
        flex-direction: column !important;
        padding: 14px 12px;
        gap: 16px;
      }
      .video-player-pane {
        width: 100% !important;
        max-width: 100% !important;
      }
      .video-iframe-wrap {
        width: 100%;
        aspect-ratio: 9/16;
        max-height: 42vh;
        border-radius: 12px;
        margin: 0 auto;
      }
      .analysis-pane {
        width: 100% !important;
        min-width: 0 !important;
      }

      /* Secondary Modals on Mobile */
      .api-modal-box, .pricing-modal-box {
        width: 92%;
        max-width: 95vw;
        padding: 20px 16px;
        margin: auto;
      }

      /* Tab 7 Motion Swap UI on Mobile */
      .motion-grid {
        grid-template-columns: 1fr !important;
        gap: 14px;
      }
      .dropzone-box {
        padding: 16px;
      }
      .vertical-player-frame {
        width: 100% !important;
        max-width: 280px;
        margin: 0 auto;
      }
    }

    @media (max-width: 480px) {
      .header-left #currentTopicLabel {
        font-size: 13px !important;
      }
      .thumbnail-wrap {
        max-height: 420px;
      }
      .video-card {
        padding: 12px;
      }
      .card-title {
        font-size: 14px;
      }
      .card-meta {
        font-size: 11px;
      }
    }
"""

if 'COMPREHENSIVE MOBILE RESPONSIVE ENGINE' not in content:
    content = content.replace('</style>', mobile_css + '\n  </style>')
    print("Inserted Mobile Responsive CSS into <style>")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated HTML structure and responsive CSS successfully!")
