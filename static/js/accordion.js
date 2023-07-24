document.addEventListener('DOMContentLoaded', function () {
    const accordionItems = document.querySelectorAll('.accordion-item');
  
    accordionItems.forEach(item => {
      const button = item.querySelector('.accordion-button');
      const collapse = item.querySelector('.accordion-collapse');
  
      button.addEventListener('click', () => {
        collapse.classList.toggle('show');
      });
    });
  });
  