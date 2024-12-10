# Chat Application

## Project Overview
This is a web-based real-time chat application built using Flask and WebSocket technology. The application allows users to join chat rooms and communicate in real-time.

## Features
- **WebSocket Integration**: Full-duplex communication for real-time messaging.
- **Chat Room Functionality**: Users can create and join chat rooms.
- **Message Sending and Receiving**: Users can send messages that are broadcast to all participants in the room.
- **User Connection Management**: Logs user connections and disconnections.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd chatapp
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to `http://localhost:5000` to access the chat application.

## Testing Instructions
To run the tests, execute the following command:
```bash
python -m unittest test_app.py
```

## Technologies Used
- Flask
- WebSocket
- CORS

## License
This project is licensed under the MIT License.
