const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', ws => {
    console.log('Client connected');
    const interval = setInterval(() => {
        const price = (1800 + Math.random() * 50).toFixed(2);
        ws.send(JSON.stringify({ type: 'price_update', symbol: 'XAUUSD', price }));
    }, 5000);

    ws.on('close', () => {
        console.log('Client disconnected');
        clearInterval(interval);
    });

    ws.on('error', err => console.error('WebSocket error:', err));
});

console.log('WebSocket server running on ws://localhost:8080');
