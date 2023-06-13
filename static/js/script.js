window.addEventListener('scroll', function() {
  var scrollingImage = document.getElementById('header');
  var scrollAmount = window.pageYOffset;

  // Calculate the scroll ratio based on the window height
  var scrollRatio = scrollAmount / window.innerHeight;

  // Set the translateY value based on the scroll ratio
  scrollingImage.style.transform = 'translateY(' + (-scrollRatio * 100) + '%)';
});
