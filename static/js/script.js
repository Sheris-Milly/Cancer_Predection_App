function submitForm() {
    const data = {
        'Clump Thickness': parseInt(document.getElementById('clump_thickness').value),
        'Uniformity of Cell Size': parseInt(document.getElementById('cell_size').value),
        'Uniformity of Cell Shape': parseInt(document.getElementById('cell_shape').value),
        'Marginal Adhesion': parseInt(document.getElementById('marginal_adhesion').value),
        'Single Epithelial Cell Size': parseInt(document.getElementById('epithelial_cell_size').value),
        'Bare Nuclei': parseInt(document.getElementById('bare_nuclei').value),
        'Bland Chromatin': parseInt(document.getElementById('bland_chromatin').value),
        'Normal Nucleoli': parseInt(document.getElementById('normal_nucleoli').value),
        'Mitoses': parseInt(document.getElementById('mitoses').value)
    };

    fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `Prediction: ${data.prediction}`;
    })
    .catch(error => console.error('Error:', error));
}

// Function to check the API status
function checkApiStatus() {
    // Send GET request to status endpoint
    fetch('/status')
    .then(response => {
        if (response.ok) {
            document.getElementById('statusResult').innerText = 'API is Online';
            document.getElementById('statusResult').classList.add("status-box");
        } else {
            document.getElementById('statusResult').innerText = 'API is Offline';
            document.getElementById('statusResult').classList.add("status-box");
        }
    })
    .catch(() => {
        document.getElementById('statusResult').innerText = 'API is Offline';
        document.getElementById('statusResult').classList.add("status-box");
    });
}
