import styled from "styled-components"
import stopButton from "../assets/stopbutton.png"

const Container = styled.div``
const Title = styled.div``
const Body = styled.div``
const ControlButton = styled.div``
const Hr = styled.hr``
const Summary = styled.div``
const Subtitle = styled.div``
const StopButton = styled.img``







const Processes = () => {
  return (
    <Container
    className="h-full w-[40%] bg-white rounded-[10px] border-[1px] border-[#008040]
      flex flex-col  
    "
  >
    <Title
    className="h-[50px] w-full font-bold bg-[#e6ffee] rounded-t-[10px]"
    >
      <div className="text-[#00802b] font-bold text-[24px]
       pt-2
      ">Monitor Agent Processes</div>
    </Title>
    <Hr className="border-t-1 border-[#00802b] " />
    <Body
      className="h-[90%] w-full flex flex-col items-center"
    >
      <Subtitle 
        className="text-start w-full ml-5 text-[20px] text-[#595959] font-bold mt-[20px]"
      >Intent Summary</Subtitle>
      <Summary
        className=" w-[90%] h-auto bg-[#f2f2f2] rounded-[5px] p-1 
        font-semibold text-[14px]
        "
      >
        the user wants to get a mail for an order he place a week 
        back
      </Summary>

      <Subtitle 
        className="text-start w-full ml-5 text-[20px] text-[#595959] font-bold mt-[20px]"
      >Action steps</Subtitle>
      <Summary
        className=" w-[90%] h-auto bg-[#f2f2f2] rounded-[5px] p-1 
        font-semibold text-[14px]
        "
      >
        the user wants to get a mail for an order he place a week 
        back
      </Summary>

      <Subtitle 
        className="text-start w-full ml-5 text-[20px] text-[#595959] font-bold mt-[20px]"
      >Conclusion</Subtitle>
      <Summary
        className=" w-[90%] h-auto bg-[#f2f2f2] rounded-[5px] p-1 
        font-semibold text-[14px]
        "
      >
        the user wants to get a mail for an order he place a week 
        back
      </Summary>      
    </Body>
    <ControlButton 
      className="absolute bottom-[80px] right-[50px] hover:cursor-pointer
      hover:scale-110 transition-transform duration-300
      "
    >
      <StopButton
        src={stopButton}
        className="w-[50px] h-[50px]"
      />

    </ControlButton>

  </Container>
  )
}

export default Processes
