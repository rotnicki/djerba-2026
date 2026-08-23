(() => {
  const button = document.querySelector('[data-vcard-share]');
  const status = document.getElementById('vcard-share-status');

  if (!button || !status) return;

  const vcfUrl = button.getAttribute('data-vcf-url');
  let contactFile = null;
  let loadError = null;

  const setStatus = (message) => {
    status.textContent = message;
  };

  const prepareFile = async () => {
    try {
      const response = await fetch(vcfUrl, { cache: 'no-store' });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);

      const vcardText = await response.text();
      contactFile = new File(
        [vcardText],
        'dzerba-2026-kontakty.vcf',
        { type: 'text/vcard;charset=utf-8' }
      );

      if (!navigator.share) {
        throw new Error('Web Share API niedostępne');
      }

      if (navigator.canShare && !navigator.canShare({ files: [contactFile] })) {
        throw new Error('Udostępnianie plików niedostępne');
      }

      button.disabled = false;
    } catch (error) {
      loadError = error;
      button.disabled = true;
      setStatus('Ten sposób przekazania kontaktów nie jest dostępny w tej przeglądarce. Użyj zwykłego linku do pobrania paczki powyżej.');
    }
  };

  button.addEventListener('click', () => {
    if (!contactFile || loadError) {
      setStatus('Plik kontaktów nie jest jeszcze gotowy do przekazania. Użyj zwykłego linku do pobrania paczki powyżej.');
      return;
    }

    setStatus('Otwieram systemowe opcje przekazania paczki 8 kontaktów.');

    navigator.share({
      files: [contactFile],
      title: 'Kontakty Dżerba 2026'
    }).then(() => {
      setStatus('Systemowe okno przekazania pliku zostało zamknięte.');
    }).catch((error) => {
      if (error && error.name === 'AbortError') {
        setStatus('Anulowano przekazanie pliku kontaktów.');
        return;
      }
      setStatus('Nie udało się przekazać pliku kontaktów tym sposobem. Użyj zwykłego linku do pobrania paczki powyżej.');
    });
  });

  prepareFile();
})();
