import os
import requests
from flask import Flask, render_template, request

# Create a Flask web application
app = Flask(__name__, static_url_path='/static')

# Read the OpenAI API key from a file named 'api_key.txt'
api_key_file_path = 'api_key.txt'
if os.path.exists(api_key_file_path):
    with open(api_key_file_path, 'r') as key_file:
        api_key = key_file.read().strip()
else:
    # Print an error message and exit if the API key file is not found
    print("API key file not found. Please create a file named 'api_key.txt' with your OpenAI API key.")
    exit()

# Function to generate content using GPT-3
def generate_content(prompt, length=100, temperature=0.7):
    endpoint = "https://api.openai.com/v1/engines/text-davinci-003/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "prompt": prompt,
        "max_tokens": length,
        "temperature": temperature #Here, temperature is a value between 0 and 1. Higher values (e.g., 0.8) will result in more diverse 
                                   #and creative output, while lower values (e.g., 0.2) will make the output more deterministic and focused. 
    }

    # Send a POST request to the OpenAI API to generate content
    response = requests.post(endpoint, headers=headers, json=data)
    response.raise_for_status()

    # Extract and return the generated text from the API response
    return response.json()["choices"][0]["text"].strip()

# Define the route for the main page ('/')
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # If a form is submitted via POST, retrieve the user input
        prompt = request.form['prompt']
        length = int(request.form['length'])
        temperature = float(request.form['temperature'])

        # Generate content using GPT-3 based on user input
        generated_content = generate_content(prompt, length, temperature)

        # Print the generated content to the console for debugging
        print(f"Generated Content: {generated_content}")

        # Render the 'index.html' template with the generated content
        return render_template('index.html', content=generated_content)

    # Render the 'index.html' template without generated content for the initial load
    return render_template('index.html', content=None)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
