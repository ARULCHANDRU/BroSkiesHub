from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# This is the main route that displays the portfolio page
@app.route('/')
def home():
    # The render_template function finds and serves the index.html file from the 'templates' folder.
    return render_template('index.html')

# This route handles the form submission
@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Check if the request method is POST, which is what our form uses
    if request.method == 'POST':
        try:
            # Get data from the form using the 'name' attributes of the input fields
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']
            
            # For this example, we'll just print the submitted data to the console.
            # In a real-world application, you would save this to a database,
            # send an email, or integrate with a CRM.
            print(f"--- New Contact Form Submission ---")
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Message: {message}")
            print(f"------------------------------------")
            
            # Return a simple confirmation message to the user
            return "Thank you for your message! I will get back to you soon."
        except Exception as e:
            # Basic error handling
            return f"An error occurred: {e}"
            
    # If someone tries to access this URL directly via a GET request
    return "This page is for form submissions only."

# This line allows you to run the app directly using 'python app.py'
if __name__ == '__main__':
    # debug=True enables auto-reload, so you don't have to restart the server after every change.
    app.run(debug=True)