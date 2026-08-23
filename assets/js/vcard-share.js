(() => {
  const headings = Array.from(document.querySelectorAll('h3'));
  const heading = headings.find((item) => item.textContent.trim() === 'Kontakty do zapisania w telefonie');

  if (!heading) return;

  let node = heading.nextElementSibling;
  const toRemove = [];

  while (
    node &&
    node.tagName !== 'H3' &&
    node.textContent.trim() !== 'Źródła:'
  ) {
    toRemove.push(node);
    node = node.nextElementSibling;
  }

  toRemove.forEach((item) => item.remove());

  const intro = document.createElement('p');
  intro.textContent = 'Test pojedynczego kontaktu na iPhonie:';

  const linkParagraph = document.createElement('p');
  const link = document.createElement('a');
  link.href = 'assets/kontakty/djerba-pogotowie-190.vcf';
  link.textContent = 'Dodaj pogotowie 190 do kontaktów';
  linkParagraph.appendChild(link);

  heading.insertAdjacentElement('afterend', linkParagraph);
  heading.insertAdjacentElement('afterend', intro);
})();
