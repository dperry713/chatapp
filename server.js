const WebSocket = require('ws');
const http = require('http');
const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());

const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

// Store chat rooms and their participants
const chatRooms = new Map();

// Function to join a chat room
function joinRoom(ws, roomName) {
    if (!chatRooms.has(roomName)) {
        chatRooms.set(roomName, new Set());
    }
    chatRooms.get(roomName).add(ws);
    ws.roomName = roomName;
    console.log(`User joined room: ${roomName}`);
}

// Function to broadcast messages to all users in a room
function broadcastMessage(roomName, message) {
    const clients = chatRooms.get(roomName);
    if (clients) {
        clients.forEach(client => {
            if (client.readyState === WebSocket.OPEN) {
                client.send(message);
            }
        });
    }
}

// Function to delete a message
function deleteMessage(ws, messageId) {
    // Logic to delete a message
    console.log(`Message with ID ${messageId} deleted`);
    // Notify all clients in the room about the deletion
    broadcastMessage(ws.roomName, JSON.stringify({ type: 'delete', messageId }));
}

// Function to edit a message
function editMessage(ws, messageId, newContent) {
    // Logic to edit a message
    console.log(`Message with ID ${messageId} edited to: ${newContent}`);
    // Notify all clients in the room about the edit
    broadcastMessage(ws.roomName, JSON.stringify({ type: 'edit', messageId, newContent }));
}

wss.on('connection', (ws) => {
    console.log('New client connected');

    ws.on('message', (message) => {
        console.log(`Received: ${message}`);
        const data = JSON.parse(message);
        switch (data.type) {
            case 'join':
                joinRoom(ws, data.room);
                break;
            case 'message':
                broadcastMessage(ws.roomName, JSON.stringify({ type: 'message', content: data.message }));
                break;
            case 'delete':
                deleteMessage(ws, data.messageId);
                break;
            case 'edit':
                editMessage(ws, data.messageId, data.newContent);
                break;
            // Implement additional message handling cases here
        }
    });

    ws.on('close', () => {
        console.log('Client disconnected');
        if (ws.roomName) {
            chatRooms.get(ws.roomName).delete(ws);
        }
    });
});

server.listen(8080, () => {
    console.log('Server is listening on port 8080');
});
