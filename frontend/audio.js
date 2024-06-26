const socket = io.connect('http://localhost:5000');

socket.on('connect', () => {
    console.log('Connected to server');
});

socket.on('response', (data) => {
    console.log('Transcript:', data.transcript);
});

let mediaRecorder;
const recordButton = document.getElementById('recordButton');

recordButton.addEventListener('click', async () => {
    if (mediaRecorder && mediaRecorder.state === 'recording') {
        mediaRecorder.stop();
        recordButton.textContent = 'Start Recording';
    } else {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.start(250); // Collect 250ms of audio data

        mediaRecorder.ondataavailable = (event) => {
            if (event.data.size > 0) {
                const reader = new FileReader();
                reader.onload = function() {
                    socket.emit('audio', reader.result);
                };
                reader.readAsArrayBuffer(event.data);
            }
        };

        mediaRecorder.onstop = () => {
            socket.emit('audio_end');
        };

        recordButton.textContent = 'Stop Recording';
    }
});