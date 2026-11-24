const feedback = document.querySelector('#copy-feedback');

for (const button of document.querySelectorAll('[data-copy]')) {
  button.addEventListener('click', async () => {
    const field = document.getElementById(button.dataset.copy);
    const label = field.labels[0].textContent;
    try {
      await navigator.clipboard.writeText(field.value);
      feedback.textContent = label + ' copied.';
    } catch {
      field.focus();
      field.select();
      feedback.textContent = label + ' selected. Use your device’s copy command.';
    }
  });
}
