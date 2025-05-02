// import React from 'react'
import styled from "styled-components"
import { useNavigate } from "react-router-dom"

const Container = styled.div`
`

const Home = () => {
    const navigate = useNavigate()



  return (
    <Container >
        <div className=" text-yellow font-bold text-[60px]">Home</div>
        <button 
            className=" h-[50px] w-[200px] bg-red text-black border border-blue-200"
            onClick={() => navigate("/setting")}
        >Click here</button>
    </Container>
  )
}

export default Home
