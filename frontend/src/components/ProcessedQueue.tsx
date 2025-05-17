import styled from "styled-components"
import ProcessedCustomer from "./ProcessedCustomer"
import {  AnimatePresence } from "framer-motion";


const Container = styled.div`
  &::-webkit-scrollbar {
    display: none; 
  }
`

type customerType = {
  channel: string,
  sender_id: string,
  sender_name: string,
  timestamp: string,
  content: string,
}


type HighlightType = {
  highlightId: string | null,
  setHighlightId: (id: string) => void,
  processedCustomers: Map<string, customerType>
}


const ProcessedQueue = ({highlightId, setHighlightId, processedCustomers}: HighlightType) => {

  return (
    <Container 
      className="w-[90px] h-[680px] p-3 space-y-3 bg-white 
      overflow-y-auto hide-scrollbar  mt-[35px]"
    >
      <AnimatePresence mode="popLayout">
        {Array.from(processedCustomers.values()).map((customer, sender_id) => (
          <ProcessedCustomer
            key={sender_id}
            setHighlightId={setHighlightId}
            isHighlighted={highlightId == customer.sender_id}
            id={customer.sender_id}
            data={customer}
        />
        ))}
    </AnimatePresence>
    </Container>
  )
}

export default ProcessedQueue
