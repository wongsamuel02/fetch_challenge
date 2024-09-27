## Fetch Backend Internship Coding Challenge

This project is a simple REST API that allows users to manage points from different payers. It supports adding points, spending points, and fetching the balance of points per payer.

### Prerequisites

- Python 3.7 or higher
- Flask (Python web framework)

You can install Flask using pip:

```bash
pip install Flask

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-repo/fetch-backend-challenge.git
cd fetch-backend-challenge

### Running the Application

After setting up the project, you can start the Flask server by running:

```bash
python app.py

### Testing the API

You can test the API with `curl` or a tool like Postman. Below is an example of a curl command to do a POST request for the add endpoint

#### Add Points:

```bash
curl -X POST http://localhost:8000/add -H "Content-Type: application/json" -d '{"payer": "DANNON", "points": 5000, "timestamp": "2020-11-02T14:00:00Z"}'



