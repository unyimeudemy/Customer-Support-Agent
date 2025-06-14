import styled from "styled-components"
import addIcon from "../assets/add_icon.png"
import sendMessageIcon from "../assets/send_message_icon.png"

const Container = styled.div``
const InputField = styled.textarea`
  border: none;
  outline: none;

  &:focus {
    outline: none;
    box-shadow: none;
  }
`
const Buttons = styled.div``
const AddIcon = styled.img``
const SendMessageIcon = styled.img``


const ChatInput = () => {
  return (
    <Container
        className="w-[100%] h-[120px]  mt-auto
        bg-white rounded-[10px] border-[1px] border-[#b3b3b3]
        p-2 flex flex-col 
        "
    style={{
      boxShadow: '3px 8px 7px rgba(0, 0, 0, 0.1)'
    }}
  >
    <InputField
        className="w-full h-[70%]  resize-none
        font-bold text-[#737373]
        "
    />
    
    <Buttons
    className="w-full h-[40px] 
    flex flex-row items-center justify-between
    "
    >
        <AddIcon
            src={addIcon}
            className="h-[30px] w-[30px] hover:scale-150 transition-transform duration-300 cursor-pointer"
        />
        <SendMessageIcon
            src={sendMessageIcon}
            className="h-[19px] w-[19px] mr-2  hover:scale-150 transition-transform duration-300 cursor-pointer"
        />

    </Buttons>

  </Container>
  )
}

export default ChatInput
