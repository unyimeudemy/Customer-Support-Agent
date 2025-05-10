import styled from "styled-components"
import rihana from "../assets/rihana2.png"

const Container = styled.div``
const Body = styled.div``
const Profile = styled.img``
const Time = styled.div``

const ReceivedMessage = () => {
  return (
    <Container className="w-full h-auto 
    flex justify-start 
    ">
        <div className="w-auto h-full">

            <Body
                className="w-auto h-auto bg-white rounded-[5px] p-2"
            >
                Hi there
            </Body>
            <div className="h-[45px] w-full 
            flex flex-row mt-2 
            ">
                <Profile 
                    className="w-[30px] h-[30px] bg-black rounded-[6px] "
                    src={rihana}
                />
                <Time className="w-auto h-2 text-[#595959] font-bold text-[12px]
                ml-2
                "> Today at 10:30pm</Time>
            </div>
        </div>

    </Container>
  )
}

export default ReceivedMessage
