import { useNavigate } from "react-router-dom"
import styled from "styled-components"
import Conversation from "./Conversation"
import Processes from "./Processes"

const Wrapper = styled.div``




const DashBoard = () => {
    const navigate = useNavigate()


  return (
    <div className="h-[91.5%] w-[92.6%]  rounded-[10px] bg-[#e6e6e6] "
    style={{
      boxShadow: '8px 8px 7px rgba(0, 0, 0, 0.3)'
    }}
    >
        <Wrapper
          className="w-full h-full p-5  rounded-[10px]
          flex flex-row 
          "
        >
          <Conversation/>
          <Processes/>
        </Wrapper>
    </div>
  )
}

export default DashBoard
