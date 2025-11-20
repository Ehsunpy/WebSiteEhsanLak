const observer = new IntersectionObserver(
  entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("animate-in");
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.15 }
);

document.querySelectorAll("[data-animate]").forEach(el => observer.observe(el));

const navToggle = document.querySelector(".nav-toggle");
const nav = document.querySelector(".main-nav");

if (navToggle) {
  navToggle.addEventListener("click", () => {
    nav.classList.toggle("open");
  });
}

// انیمیشن ستاره‌ای ونگوگ - متحرک
function createStarryNight() {
  const container = document.getElementById('starryNight');
  if (!container) return;

  // تعداد ستاره‌ها
  const starCount = 50;

  for (let i = 0; i < starCount; i++) {
    const star = document.createElement('div');
    star.className = 'star';
    
    // اندازه تصادفی
    const size = Math.random() * 3 + 1;
    star.style.width = size + 'px';
    star.style.height = size + 'px';
    
    // موقعیت تصادفی
    star.style.left = Math.random() * 100 + '%';
    star.style.top = Math.random() * 100 + '%';
    
    // تاخیر انیمیشن تصادفی
    star.style.animationDelay = Math.random() * 3 + 's';
    star.style.animationDuration = (Math.random() * 2 + 2) + 's';
    
    container.appendChild(star);
  }

  // اضافه کردن براش‌های ونگوگ
  for (let i = 0; i < 15; i++) {
    const brush = document.createElement('div');
    brush.className = 'van-gogh-brush';
    
    brush.style.left = Math.random() * 100 + '%';
    brush.style.top = Math.random() * 100 + '%';
    brush.style.animationDelay = Math.random() * 4 + 's';
    brush.style.animationDuration = (Math.random() * 3 + 3) + 's';
    brush.style.transform = `rotate(${Math.random() * 360}deg)`;
    
    container.appendChild(brush);
  }
}

// اجرا بعد از لود شدن صفحه
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', createStarryNight);
} else {
  createStarryNight();
}

// اضافه کردن انیمیشن به کارت‌ها
document.querySelectorAll('.course-card, .blog-card, .contact-card').forEach((card, index) => {
  card.style.animationDelay = (index * 0.1) + 's';
  card.classList.add('card-animate');
});

// اضافه کردن انیمیشن float به المان‌های خاص
document.querySelectorAll('.hero-card, .page-hero').forEach(el => {
  el.classList.add('animated-element');
});

