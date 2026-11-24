// ASCI Unified Site Header & Megamenu Scripts
document.addEventListener('DOMContentLoaded', () => {
  // Megamenu interaction for all top navigation dropdown items (hover + click)
  const navItemsWithMenu = document.querySelectorAll('.nav-item-dropdown');
  const allMegamenuPanels = document.querySelectorAll('.megamenu-panel');
  let menuTimeout;

  function closeAllMegamenus() {
    navItemsWithMenu.forEach(i => i.classList.remove('open'));
    allMegamenuPanels.forEach(p => p.classList.remove('active'));
  }

  navItemsWithMenu.forEach(item => {
    const targetMenuId = item.getAttribute('data-menu');
    const targetPanel = document.getElementById(targetMenuId);

    function showCurrentMenu() {
      clearTimeout(menuTimeout);
      navItemsWithMenu.forEach(i => i.classList.remove('open'));
      allMegamenuPanels.forEach(p => p.classList.remove('active'));
      item.classList.add('open');
      if (targetPanel) targetPanel.classList.add('active');
    }

    function hideCurrentMenu() {
      menuTimeout = setTimeout(() => {
        if (!targetPanel || !targetPanel.matches(':hover')) {
          item.classList.remove('open');
          if (targetPanel) targetPanel.classList.remove('active');
        }
      }, 150);
    }

    item.addEventListener('mouseenter', showCurrentMenu);
    item.addEventListener('mouseleave', hideCurrentMenu);

    if (targetPanel) {
      targetPanel.addEventListener('mouseenter', () => clearTimeout(menuTimeout));
      targetPanel.addEventListener('mouseleave', hideCurrentMenu);
    }

    const link = item.querySelector('.nav-link') || item;
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      if (!href || href === '#' || href === 'javascript:void(0)') {
        e.preventDefault();
        const isOpen = item.classList.contains('open');
        closeAllMegamenus();
        if (!isOpen) {
          showCurrentMenu();
        }
      }
    });
  });

  // Close megamenu when clicking outside
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.nav-item-dropdown') && !e.target.closest('.megamenu-panel')) {
      closeAllMegamenus();
    }
  });

  // Mobile Accordion Drawer Toggle
  document.querySelectorAll('.mobile-accordion-header').forEach(header => {
    header.addEventListener('click', () => {
      const parent = header.closest('.mobile-accordion-item');
      const isAlreadyOpen = parent.classList.contains('active');

      // Close all accordion items
      document.querySelectorAll('.mobile-accordion-item').forEach(item => {
        item.classList.remove('active');
      });

      // Toggle clicked item
      if (!isAlreadyOpen) {
        parent.classList.add('active');
      }
    });
  });
});

// Mobile Drawer Toggle
function toggleMobileNav() {
  const overlay = document.getElementById('mobileNavOverlay');
  if (!overlay) return;
  const isActive = overlay.classList.contains('active');
  if (isActive) {
    overlay.classList.remove('active');
    document.body.style.overflow = '';
  } else {
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }
}

// Search Modal Toggle
function openSearch() {
  const overlay = document.getElementById('searchOverlay');
  if (overlay) {
    overlay.classList.add('active');
    const input = document.getElementById('siteSearchInput');
    if (input) setTimeout(() => input.focus(), 100);
    document.body.style.overflow = 'hidden';
  }
}

function closeSearch() {
  const overlay = document.getElementById('searchOverlay');
  if (overlay) {
    overlay.classList.remove('active');
    document.body.style.overflow = '';
  }
}

function quickSearch(query) {
  const input = document.getElementById('siteSearchInput');
  if (input) {
    input.value = query;
    siteSearch();
  }
}

function siteSearch() {
  const input = document.getElementById('siteSearchInput');
  if (!input) return;
  const q = input.value.trim().toLowerCase();
  if (!q) return;
  if (q.includes('complaint') || q.includes('lodge') || q.includes('report ad')) {
    window.location.href = 'https://tara.ascionline.in/auth/';
  } else if (q.includes('code') || q.includes('guideline') || q.includes('rule')) {
    window.location.href = 'https://www.ascionline.in/the-asci-code/';
  } else if (q.includes('academy') || q.includes('course') || q.includes('learn')) {
    window.location.href = 'academy.html';
  } else if (q.includes('people') || q.includes('board') || q.includes('leader')) {
    window.location.href = 'people.html';
  } else {
    window.location.href = 'about-us.html';
  }
}

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    closeSearch();
    const overlay = document.getElementById('mobileNavOverlay');
    if (overlay && overlay.classList.contains('active')) {
      toggleMobileNav();
    }
  }
});
