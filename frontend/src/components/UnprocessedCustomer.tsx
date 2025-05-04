import styled from "styled-components"



const Container = styled.div``
const Wrapper = styled.div``
const Notification = styled.div``
const ChannelIcon = styled.img``
const ClickIndication = styled.div``



type CustomerData = {
  id: string,
  channel: string,
  notification: string,
  detail: string
}

type CustomerProps = {
  isHighlighted: boolean,
  setHighlightId: (id: string) => void,
  id: string,
  data: CustomerData
}

const UprocessedCustomer = ({isHighlighted, setHighlightId, id, data}: CustomerProps) => {

  const handleClick = () => {
    setHighlightId(id)
  }


  return (
    <Container 
      onClick={handleClick}
      className="w-auto h-[45px]   flex-shrink-0 flex items-center 
      cursor-pointer hover:scale-110 transition-transform duration-200
      ">

      <Wrapper className="w-[40px] h-[40px] rounded-full border border-[#b3b3b3] 
      flex items-center justify-center z-[20]
      ">
        <ChannelIcon 
          src={data.channel}
          className="h-[20px] w-[20px]"
        />
      </Wrapper>
      <Notification className="relative bg-[#009900] w-[20px] h-[20px] rounded-full text-white
        font-extrabold text-[12px] flex items-center justify-center right-[12px] bottom-[15px] z-[30]
        ">{data.notification}</Notification>
      {isHighlighted &&<ClickIndication 
        className=" w-[41.5px] h-[73px] bg-[#e6e6e6] ml-[-60px]  mt-[30px] z-[10] rounded-t-full 
        mx-[20px] 
        "
      />}
    </Container>
  )
}

export default UprocessedCustomer
