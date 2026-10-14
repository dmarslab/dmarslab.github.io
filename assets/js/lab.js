(function () {
  'use strict';
  const menuButton = document.querySelector('.menu-toggle');
  const navigation = document.querySelector('#navigation');
  function closeMenu() {
    navigation.classList.remove('is-open');
    menuButton.setAttribute('aria-expanded', 'false');
  }
  menuButton.addEventListener('click', () => {
    const expanded = menuButton.getAttribute('aria-expanded') === 'true';
    navigation.classList.toggle('is-open', !expanded);
    menuButton.setAttribute('aria-expanded', String(!expanded));
  });
  navigation.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && navigation.classList.contains('is-open')) {
      closeMenu();
      menuButton.focus();
    }
  });
  document.querySelectorAll('.publication-disclosure').forEach(button => {
    button.addEventListener('click', () => {
      const panel = document.getElementById(button.getAttribute('aria-controls'));
      const expanded = button.getAttribute('aria-expanded') === 'true';
      panel.hidden = expanded;
      button.setAttribute('aria-expanded', String(!expanded));
    });
  });
  const filters = ['year', 'type', 'topic'].map(name => document.querySelector('#filter-' + name));
  if (filters.some(filter => !filter)) return;
  const records = Array.from(document.querySelectorAll('.publication'));
  const count = document.querySelector('#publication-count');
  const empty = document.querySelector('#publication-empty');
  const list = document.querySelector('#publication-list');
  function filterPublications() {
    const [year, type, topic] = filters.map(filter => filter.value);
    let shown = 0;
    records.forEach(record => {
      const matches = (year === 'all' || record.dataset.year === year)
        && (type === 'all' || record.dataset.type === type)
        && (topic === 'all' || record.dataset.topics.split('|').includes(topic));
      record.hidden = !matches;
      if (!record.hidden) shown += 1;
    });
    count.textContent = shown + (shown === 1 ? ' publication shown' : ' publications shown');
    empty.hidden = shown > 0;
  }
  function resetPublicationView() {
    list.scrollTop = 0;
    filterPublications();
  }
  filters.forEach(filter => filter.addEventListener('change', resetPublicationView));
  document.querySelector('#reset-filters').addEventListener('click', () => {
    filters.forEach(filter => { filter.value = 'all'; });
    resetPublicationView();
  });
  document.querySelectorAll('.publication-tag').forEach(button => {
    button.addEventListener('click', () => {
      filters[2].value = button.dataset.topic;
      resetPublicationView();
    });
  });
  filterPublications();
})();
