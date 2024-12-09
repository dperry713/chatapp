# Chat Application

This is a simple chat application built using Flask and Flask-SocketIO. It stores messages in a HashMap where each user is a key, and their messages are stored as a list of values.

## Features
- Send messages via HTTP POST requests.
- Retrieve all messages sent by a specific user.

## Setup

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd chatapp
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
To start the server, run:
```bash
python app.py
```

The server will be running at `http://localhost:5000/`.

### Testing
To run the tests, execute:
```bash
python -m unittest test_app.py
```

## Usage
- **Send a Message**: Use the `/send_message` endpoint with a JSON body containing `user` and `message`.
- **Retrieve Messages**: Use the `/get_all_messages` endpoint with a query parameter `user` to get all messages sent by that user.

## License
This project is licensed under the MIT License.
