// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/templates/**/*.html',
    './src/static/js/**/*.js',
  ],
  safelist: [
    'pt-section-vertical', // always generate this class
  ],

  theme: {
    extend: {
      colors: {
        'brand-primary': '#92400e',
        'brand-secondary': '#f59e0b',
        'brand-accent': '#fbbf24',
        'text-primary': '#1e293b',
        'text-secondary': '#4b5563',
        'footer-text': '#fcd34d',
        'border-light': 'rgba(0,0,0,0.05)',
      },
      fontFamily: {
        heading: ['"Inter", sans-serif'],
        body: ['"Inter", sans-serif'],
      },
      fontSize: {
        'hero-xl': ['4rem', '1.1'],
        'hero-lg': ['3rem', '1.2'],
        'heading-xl': ['2rem', '1.2'],
        'heading-lg': ['1.5rem', '1.3'],
      },
      fontWeight: {
        heading: '700',
        body: '500',
      },
      spacing: {
        'container-x': '1.5rem', // px-6
        'container-lg': '2rem',   // px-8
        'gap-sm': '1.5rem',       // gap-6
        'gap-md': '2.5rem',       // gap-10
        'section-vertical': '6rem', // pt-24
      },
      borderRadius: {
        sm: '0.25rem',
        md: '0.5rem',
        lg: '0.75rem',
        full: '9999px',
      },
      boxShadow: {
        sm: '0 1px 2px rgba(0,0,0,0.05)',
        DEFAULT: '0 2px 4px rgba(0,0,0,0.1)',
        md: '0 4px 6px rgba(0,0,0,0.1)',
        lg: '0 10px 15px rgba(0,0,0,0.15)',
      },
      transitionProperty: {
        DEFAULT: 'all',
      },
      transitionDuration: {
        DEFAULT: '300ms',
        fast: '150ms',
        slow: '700ms',
      },
      backgroundColor: theme => ({
        ...theme('colors'),
        'white-80': 'rgba(255,255,255,0.8)',
      })

    },
  },
  plugins: [],
};
