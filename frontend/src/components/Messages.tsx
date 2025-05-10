import styled from "styled-components"
import ReceivedMessage from "./ReceivedMessage"
import SentMessage from "./SentMessage"


const Container = styled.div``

const Messages = () => {
  return (
    <Container
    className="w-full h-[570px] flex flex-col gap-2 overflow-y-auto"
  >
    <ReceivedMessage/>
    <ReceivedMessage/>
    <ReceivedMessage/>

    <SentMessage/>
    <ReceivedMessage/>
    <SentMessage/>
    <SentMessage/>


  </Container>
  )
}

export default Messages
