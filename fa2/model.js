document.getElementById('prediction_form').addEventListener('submit', async function(event) {
    event.preventDefault();

    // Gather form input values
    const data = {
        gender: document.getElementById('gender').value,
        ethnicity: document.getElementById('ethnicity').value,
        parent_education: document.getElementById('parent_education').value,
        lunch: document.getElementById('lunch').value,
        test_preparation: document.getElementById('test_preparation').value,
        reading_score: parseInt(document.getElementById('reading_score').value),
        writing_score: parseInt(document.getElementById('writing_score').value)
    };

    try {
        // Send POST request to backend API
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        });

        // Parse JSON response
        const result = await response.json();
        console.log('Prediction API response:', result);

        // Display prediction or error message
        if (result.prediction !== undefined) {
            document.getElementById('prediction_result').innerText = "Prediction is : " + result.prediction;
        } else if (result.error) {
            document.getElementById('prediction_result').innerText = "Error: " + result.error;
        } else {
            document.getElementById('prediction_result').innerText = "Unexpected response from server.";
        }
    } catch (error) {
        // Display network or other fetch errors
        document.getElementById('prediction_result').innerText = "Error occurred while predicting.";
        console.error("Fetch error:", error);
    }
});
