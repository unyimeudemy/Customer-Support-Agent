// import React from 'react'
import styled from "styled-components"
import SideBar from "../components/SideBar"
import NavBar from "../components/NavBar"
import UnprocessedQueue from "../components/UnprocessedQueue"
import ProcessedQueue from "../components/ProcessedQueue"
import DashBoard from "../components/DashBoard"
import Footer from "../components/Footer"
import {  useEffect, useState } from "react"

const Container = styled.div``
const Wrapper = styled.div``
const Body = styled.div``
const QueueAndDMContainer = styled.div``


type customerType = {
  channel: string,
  sender_id: string,
  sender_name: string,
  timestamp: string,
  content: string,
}


const Home = () => {
  const [highlightId, setHighlightId] = useState<string | null>(null)
  const [customerList, setCustomerList] = useState<customerType[]>([])
  // const [
  //   currentlyProcessedCustomer,
  //   setCurrentlyProcessedCustomer
  // ] = useState<customerType[]>([])


  useEffect(() => {
    const socket = new WebSocket("ws://localhost:8000/ws/unprocessed_customers/");
  
    socket.onopen = () => {
      console.log("unprocessed_customers connected");
    };
  
    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      console.log("unprocessed_customers update:", data);
      setCustomerList((prev) => [...prev, data])
      // e.g. dispatch to Redux or setState to update UI
    };
  
    socket.onclose = () => {
      console.log("unprocessed_customers disconnected");
    };
  
    return () => socket.close();
  }, []);


  useEffect(() => {
    const socket = new WebSocket("ws://localhost:8000/ws/currently_processed_customer/")

    socket.onopen = () => {
      console.log("currently_processed_customer connected")
    }

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      console.log("currently_processed_customer update:", data);
    }

    socket.onclose = () => {
      console.log("currently_processed_customer closed")
    }

    return () => socket.close()
  },[])

  return (
    <Container className="h-full flex flex-col w-screen " >
      <NavBar/>
      <Wrapper className="w-full h-full flex flex-row ">
        <SideBar/>
        <Body className="w-full h-full  bg-white ">
          <UnprocessedQueue
            highlightId={highlightId}
            setHighlightId={setHighlightId}
            customerList={customerList}
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
