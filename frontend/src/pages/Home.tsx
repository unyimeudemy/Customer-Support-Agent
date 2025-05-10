// import React from 'react'
import styled from "styled-components"
import SideBar from "../components/SideBar"
import NavBar from "../components/NavBar"
import UnprocessedQueue from "../components/UnprocessedQueue"
import ProcessedQueue from "../components/ProcessedQueue"
import DashBoard from "../components/DashBoard"
import Footer from "../components/Footer"
import { useState } from "react"

const Container = styled.div``
const Wrapper = styled.div``
const Body = styled.div``
const QueueAndDMContainer = styled.div``


const Home = () => {
  const [highlightId, setHighlightId] = useState<string | null>(null)

  return (
    <Container className="h-full flex flex-col w-screen " >
      <NavBar/>
      <Wrapper className="w-full h-full flex flex-row ">
        <SideBar/>
        <Body className="w-full h-full  bg-white ">
          <UnprocessedQueue
            highlightId={highlightId}
            setHighlightId={setHighlightId}
          />
          <QueueAndDMContainer className=" flex flex-row  h-full bg-white">
            <ProcessedQueue
              highlightId={highlightId}
              setHighlightId={setHighlightId}
            />
            <DashBoard/>
          </QueueAndDMContainer>
        </Body>
      </Wrapper>
      <Footer/>
    </Container>
  )
}

export default Home
