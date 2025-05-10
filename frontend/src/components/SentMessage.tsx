import styled from "styled-components"
import rihana from "../assets/rihana.jpeg"


const Container = styled.div``
const Body = styled.div``
const Profile = styled.img``
const Time = styled.div``

const SentMessage = () => {
  return (
    <Container className="w-full h-[140px] 
    flex justify-end
    ">
        <div className="w-[90%] h-full">
            <Body
                className="w-full h-[100px] bg-white rounded-[10px]"
            >
            </Body>
            <div className="h-[45px] w-full 
            flex flex-row mt-2 justify-end
            ">
                <Time className="w-auto h-2 text-[#595959] font-bold text-[12px]
                mr-2
                "> Today at 10:30pm</Time>
                <Profile 
                    className="w-[30px] h-[30px] bg-black rounded-[6px] "
                    src={rihana}
                />

            </div>
        </div>
    </Container>
  )
}

export default SentMessage
