async function RtoD() {
    const word = document.querySelector('#RtoD')?.value;
    const response = await fetch('/convert-to-decimal', {
        method: 'post',
        body: JSON.stringify({ word: word }),
        headers: {
          'Content-type': 'application/json; charset=UTF-8',
        },
      });
    if (response.ok) {
        const decimalContainer = document.getElementById('decimalResult');
        let decimal = await response.json();
        decimalContainer.innerHTML = '';
        const decimalElement = document.createElement('div');
        decimalElement.textContent = decimal;
        decimalContainer.appendChild(decimalElement);
    }
}

async function DtoR() {
  const word = document.querySelector('#DtoR')?.value;
  const response = await fetch('/convert-to-roman', {
      method: 'post',
      body: JSON.stringify({ word: word }),
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
      },
    });
  if (response.ok) {
      const decimalContainer = document.getElementById('romanResult');
      let decimal = await response.json();
      decimalContainer.innerHTML = '';
      const decimalElement = document.createElement('div');
      decimalElement.textContent = decimal.toString();
      decimalContainer.appendChild(decimalElement);

  }
}

function uploadImage() {
  const fileInput = document.getElementById('fileInput');
  const file = fileInput.files[0];
  const formData = new FormData();
  formData.append('file', file);

  fetch('/upload-image', {
      method: 'POST',
      body: formData
  })
  .then(response => response.json())
  .then(data => {
      const resultDiv = document.getElementById('result');
      resultDiv.innerHTML = '';
      data.forEach(item => {
          const p = document.createElement('p');
          p.textContent = item;
          resultDiv.appendChild(p);
      });
  })
  .catch(error => console.error('Error:', error));
}