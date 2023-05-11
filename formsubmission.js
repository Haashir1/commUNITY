document.getElementById('form').addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent the default form submission behavior

  const form = event.target;
  const formData = new FormData(form);

  fetch('http://10.69.158.186:9999/save-form-data', {
    method: 'POST',
    body: formData
  })
  .then(response => response.text())
  .then(data => {
    console.log(data); // You can customize this based on your requirements
    // Add any additional actions you want to perform after the form submission
  })
  .catch(error => {
    console.error('Error:', error);
    // Handle any errors that occur during the form submission
  });
});
