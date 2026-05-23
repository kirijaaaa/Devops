(function () {
  'use strict';

  // Loader
  const loader = document.getElementById('loader');
  window.addEventListener('load', () => {
    setTimeout(() => loader?.classList.add('hidden'), 1200);
  });

  // Mobile nav
  const navToggle = document.getElementById('nav-toggle');
  const mobileMenu = document.getElementById('mobile-menu');

  navToggle?.addEventListener('click', () => {
    const open = mobileMenu.hasAttribute('hidden');
    if (open) {
      mobileMenu.removeAttribute('hidden');
    } else {
      mobileMenu.setAttribute('hidden', '');
    }
  });

  document.querySelectorAll('.mobile-link, .nav-link, .nav-cta, .hero-actions a, .scroll-down').forEach((link) => {
    link.addEventListener('click', () => {
      mobileMenu?.setAttribute('hidden', '');
    });
  });

  // Scroll spy
  const sections = ['home', 'about', 'skills', 'education', 'projects', 'resume', 'contact'];
  const navLinks = document.querySelectorAll('.nav-link, .mobile-link');

  function updateActiveNav() {
    let current = 'home';
    const offset = 120;

    sections.forEach((id) => {
      const el = document.getElementById(id);
      if (el && window.scrollY >= el.offsetTop - offset) {
        current = id;
      }
    });

    navLinks.forEach((link) => {
      const section = link.getAttribute('data-section');
      link.classList.toggle('active', section === current);
    });
  }

  window.addEventListener('scroll', updateActiveNav, { passive: true });
  updateActiveNav();

  // Skill bar animation
  const skillBars = document.querySelectorAll('.skill-bar');

  const skillObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const bar = entry.target;
          const level = bar.getAttribute('data-level');
          const fill = bar.querySelector('.skill-fill');
          if (fill) fill.style.width = level + '%';
          skillObserver.unobserve(bar);
        }
      });
    },
    { threshold: 0.3 }
  );

  skillBars.forEach((bar) => skillObserver.observe(bar));

  // Contact form
  const form = document.getElementById('contact-form');
  const formError = document.getElementById('form-error');
  const formSuccess = document.getElementById('form-success');
  const submitBtn = document.getElementById('submit-btn');

  form?.addEventListener('submit', (e) => {
    e.preventDefault();
    formError.hidden = true;
    formSuccess.hidden = true;

    const name = form.name.value.trim();
    const email = form.email.value.trim();
    const message = form.message.value.trim();

    if (!name || !email || !message) {
      formError.hidden = false;
      return;
    }

    submitBtn.disabled = true;
    submitBtn.textContent = 'Sending…';

    setTimeout(() => {
      formSuccess.hidden = false;
      form.reset();
      submitBtn.disabled = false;
      submitBtn.textContent = 'Send Message';
      setTimeout(() => {
        formSuccess.hidden = true;
      }, 4000);
    }, 1500);
  });

  // Resume download feedback
  const resumeBtn = document.getElementById('resume-download');
  resumeBtn?.addEventListener('click', () => {
    const original = resumeBtn.textContent;
    resumeBtn.textContent = 'Downloading…';
    setTimeout(() => {
      resumeBtn.textContent = original;
    }, 1200);
  });
})();
