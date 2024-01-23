const roomName = document.getElementById('room-id').textContent

const chatSocket = new WebSocket(
    `ws://${window.location.host}/ws/chat/${roomName}/`
)
chatSocket.onmessage = (e) =>{
    const data = JSON.parse(e.data)
    console.log(data)
}
chatSocket.onclose = (e) =>{
    console.error('Chat socket closed unexpectedly.')
}

document.querySelector(".message-input").onkeyup = (e) =>{
    if(e.key=== 'Enter'){
        document.querySelector(".send-button").click()
    }
} 

document.querySelector(".send-button").onclick = (e) => {
    const messageInputDom = document.querySelector(".message-input")
    const message = messageInputDom.value
    chatSocket.send(JSON.stringify({
            'message': message
    }))
    messageInputDom.value = ''
}
