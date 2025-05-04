import styled from "styled-components"
import telegramIcon from "../assets/telegramIcon.webp"
import gmailIcon from "../assets/gmailIcon.webp"
import whatsappIcon from "../assets/whatsappIcon.png"
import ProcessedCustomer from "./ProcessedCustomer"
import { useState } from "react"


const Container = styled.div`
  &::-webkit-scrollbar {
    display: none; 
  }
`

const customers = [
  {
    id: "1",
    channel: gmailIcon,
    notification: "3",
    detail: "Here is the detail"
  },
  {
    id: "2",
    channel: gmailIcon,
    notification: "1",
    detail: "Here is the detail"
  },
  {
    id: "3",
    channel: telegramIcon,
    notification: "1",
    detail: "Here is the detail"
  },
  {
    id: "4",
    channel: whatsappIcon,
    notification: "1",
    detail: "Here is the detail"
  },
  {
    id: "5",
    channel: whatsappIcon,
    notification: "10",
    detail: "Here is the detail"
  },
  {
    id: "6",
    channel: gmailIcon,
    notification: "2",
    detail: "Here is the detail"
  },
  {
    id: "7",
    channel: gmailIcon,
    notification: "2",
    detail: "Here is the detail"
  },
  {
    id: "8",
    channel: whatsappIcon,
    notification: "10",
    detail: "Here is the detail"
  },
  {
    id: "9",
    channel: gmailIcon,
    notification: "2",
    detail: "Here is the detail"
  },
  {
    id: "10",
    channel: gmailIcon,
    notification: "2",
    detail: "Here is the detail"
  },
  {
    id: "11",
    channel: telegramIcon,
    notification: "1",
    detail: "Here is the detail"
  },
  {
    id: "12",
    channel: whatsappIcon,
    notification: "1",
    detail: "Here is the detail"
  },
  {
    id: "13",
    channel: whatsappIcon,
    notification: "10",
    detail: "Here is the detail"
  },
  {
    id: "14",
    channel: gmailIcon,
    notification: "2",
    detail: "Here is the detail"
  },
  {
    id: "15",
    channel: gmailIcon,
    notification: "2",
    detail: "Here is the detail"
  },
  {
    id: "16",
    channel: whatsappIcon,
    notification: "10",
    detail: "Here is the detail"
  },
  {
    id: "17",
    channel: gmailIcon,
    notification: "2",
    detail: "Here is the detail"
  },
  {
    id: "18",
    channel: gmailIcon,
    notification: "2",
    detail: "Here is the detail"
  },
  {
    id: "19",
    channel: telegramIcon,
    notification: "1",
    detail: "Here is the detail"
  },
  {
    id: "20",
    channel: whatsappIcon,
    notification: "1",
    detail: "Here is the detail"
  },
  {
    id: "21",
    channel: whatsappIcon,
    notification: "10",
    detail: "Here is the detail"
  },
  {
    id: "22",
    channel: gmailIcon,
    notification: "2",
    detail: "Here is the detail"
  },
  {
    id: "23",
    channel: gmailIcon,
    notification: "2",
    detail: "Here is the detail"
  },
  {
    id: "24",
    channel: whatsappIcon,
    notification: "10",
    detail: "Here is the detail"
  },
  {
    id: "25",
    channel: gmailIcon,
    notification: "2",
    detail: "Here is the detail"
  },
  {
    id: "26",
    channel: gmailIcon,
    notification: "2",
    detail: "Here is the detail"
  },
  {
    id: "27",
    channel: gmailIcon,
    notification: "2",
    detail: "Here is the detail"
  }
];


type HighlightType = {
  highlightId: string | null,
  setHighlightId: (id: string) => void
}


const ProcessedQueue = ({highlightId, setHighlightId}: HighlightType) => {

  return (
    <Container className="w-[90px] h-[720px] p-3 space-y-3 bg-white overflow-y-auto hide-scrollbar  mt-[35px]">
       {customers.map((customer) => (
        <ProcessedCustomer
          setHighlightId={setHighlightId}
          isHighlighted={highlightId == customer.id}
          id={customer.id}
          data={customer}
      />
       ))}

    </Container>
  )
}

export default ProcessedQueue
