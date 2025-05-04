// import React from 'react'
import styled from "styled-components"
import { useNavigate } from "react-router-dom"
import SideBar from "../components/SideBar"
import NavBar from "../components/NavBar"
import IncomingQueue from "../components/IncomingQueue"
import ProcessedQueue from "../components/ProcessedQueue"
import DashBoard from "../components/DashBoard"
import Footer from "../components/Footer"

const Container = styled.div``
const Wrapper = styled.div``
const Body = styled.div``
const QueueAndDMContainer = styled.div``


const Home = () => {
    const navigate = useNavigate()

  return (
    <Container className="h-full flex flex-col w-screen " >
      <NavBar/>
      <Wrapper className="w-full h-full flex flex-row ">
        <SideBar/>
        <Body className="w-full h-full bg-[#e6e6e6] ">
          <IncomingQueue/>
          <QueueAndDMContainer className=" flex flex-row  h-full bg-white">
            <ProcessedQueue />
            <DashBoard/>
          </QueueAndDMContainer>
        </Body>
      </Wrapper>
      <Footer/>
    </Container>
  )
}

export default Home
