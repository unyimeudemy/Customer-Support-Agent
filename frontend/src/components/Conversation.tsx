import styled from "styled-components"
import Messages from "./Messages"
import ChatInput from "./ChatInput"


const Container = styled.div``

const Conversation = () => {
  return (
    <Container
    className="h-full w-[60%] p-2 
    "
  >
    <Messages/>
    <ChatInput/>
  </Container>
  )
}

export default Conversation
