function showLoading() {
    // Clear the previously generated content
    var contentParagraph = document.getElementById("generatedContent");
    contentParagraph.innerHTML = "";

    var loadingDiv = document.getElementById("loading");
    loadingDiv.style.display = "block"; // Display the loading indicator

    // Get the current timestamp before making the API request
    var startTime = new Date().getTime();

    // Make the API request
    // Note: You'll need to modify this part based on how you're making the API request

    // Example using Fetch API
    fetch('YOUR_API_ENDPOINT', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            prompt: document.getElementById("prompt").value,
            // other API parameters
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Handle API response here
        var endTime = new Date().getTime();
        var elapsedTime = endTime - startTime;

        // Adjust the timeout dynamically based on API response time
        var timeout = Math.max(0, 3000 - elapsedTime); // Minimum timeout of 0 milliseconds
        setTimeout(function () {
            loadingDiv.style.display = "none"; // Hide the loading indicator
            // You can add logic here to display the newly generated content
            // For example, update the contentParagraph.innerHTML with the new content
        }, timeout);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}