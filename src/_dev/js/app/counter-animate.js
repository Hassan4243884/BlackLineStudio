import CountUp from 'countup.js';

const test = (entries, observer) => {
    entries.forEach(entry => {
        if (entry.intersectionRatio > 0) {
            observer.unobserve(entry.target);

            const counter = entry.target;
            const start = counter.dataset.start || 0;
            const end = counter.dataset.end || 0;
            const duration = counter.dataset.duration || 2;

            const numAnim = new CountUp(counter, start, end, 0, duration, {
                useEasing: true,
                useGrouping: false,
            });

            numAnim.start();
        }
    });
};

const countAnimObserver = new IntersectionObserver(test);
document.querySelectorAll('.js-counter-animate').forEach(counter => {
    countAnimObserver.observe(counter);
});