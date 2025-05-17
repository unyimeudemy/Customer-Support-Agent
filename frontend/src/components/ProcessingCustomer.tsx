import styled, { keyframes } from "styled-components"

import telegramIcon from "../assets/telegramIcon.webp"
import gmailIcon from "../assets/gmailIcon.webp"
import whatsappIcon from "../assets/whatsappIcon.png"
import { motion } from "framer-motion";



const Container = styled(motion.div)``
const Wrapper = styled.div``
const Notification = styled.div``
const fade = keyframes`
  0% { opacity: 0.2; }
  50% { opacity: 1; }
  100% { opacity: 0.2; }
`;

const ChannelIcon = styled.img`
  animation: ${fade} 1.5s infinite ease-in-out;
`;const ClickIndication = styled.div``



type CustomerData = {
  channel: string,
  sender_id: string,
  sender_name: string,
  timestamp: string,
  content: string,
}

type CustomerProps = {
  isHighlighted: boolean,
  setHighlightId: (id: string) => void,
  id: string,
  data: CustomerData
}


const ProcessingCustomer = ({isHighlighted, setHighlightId, id, data}: CustomerProps) => {

  const handleClick = () => {
    setHighlightId(id)
  }


  return (
    <Container 
      layout
      initial={{ scale: 0, opacity: 0 }}
      animate={{ scale: 1, opacity: 1 }}
      exit={{
        scale: 0,
        opacity: 1,
        transition: { duration: 0.3, ease: "easeOut" }  
      }}      
      transition={{ duration: 0.2, ease: "easeInOut" }}
      onClick={handleClick}
      className="w-auto h-[45px]   flex-shrink-0 flex items-center 
      cursor-pointer hover:scale-110 transition-transform duration-200
      ">

      <Wrapper className="w-[40px] h-[40px] rounded-full border border-[#b3b3b3] 
      flex items-center justify-center z-[20] 
      ">
        <ChannelIcon 
          src={(data.channel === "telegram") ? telegramIcon : (
            data.channel === "gmail" ? gmailIcon : whatsappIcon
          )}
          className="h-[20px] w-[20px]"
        />
      </Wrapper>
      <Notification className="relative bg-[#009900] w-[20px] h-[20px] rounded-full text-white
        font-extrabold text-[12px] flex items-center justify-center right-[12px] bottom-[15px] z-[30]
        ">{"3"}</Notification>
      {isHighlighted &&<ClickIndication 
        className=" w-[41.5px] h-[73px] bg-[#e6e6e6] ml-[-60px]  mt-[30px] z-[10] rounded-t-full 
        mx-[20px] 
        "
      />}
    </Container>
  )
}

export default ProcessingCustomer
