window.addEventListener('scroll', function() {
    var scrollingImage = document.getElementById('scrolling-image');
    var scrollAmount = window.pageYOffset;
    scrollingImage.style.transform = 'translateY(' + (-scrollAmount/2) + 'px)';
  });
  