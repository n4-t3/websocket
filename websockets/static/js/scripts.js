const roomName = document.getElementById('room-id').textContent
const route = window.location.href
const route_kwargs = route.split("/")
const chatMessageParent = document.querySelector(".chat-messages")
chatMessageParent.scrollTop = chatMessageParent.scrollHeight;

const chatSocket = new WebSocket(
    `ws://${window.location.host}/ws/chat/${roomName}/`
)

chatSocket.onmessage = (e) =>{
    const data = JSON.parse(e.data)
    const currentIsSender = data.sender === route_kwargs[5]
    const newDiv = document.createElement("div")
    newDiv.className = currentIsSender ? "message sent" : "message received"
    newDiv.textContent = data.message
    const chatMessageParent = document.querySelector(".chat-messages")
    chatMessageParent.appendChild(newDiv)
    chatMessageParent.scrollTop = chatMessageParent.scrollHeight;
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
            'message': message,
            'user': route_kwargs[5]
    }))
    messageInputDom.value = ''
}
