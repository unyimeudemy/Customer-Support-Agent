import styled from "styled-components";
import UprocessedCustomer from "./UnprocessedCustomer";
import ProcessingCustomer from "./ProcessingCustomer";
import {  AnimatePresence } from "framer-motion";



const Wrapper = styled.div`

  &::-webkit-scrollbar {
    display: none; 
  }
`;
const Container = styled.div``;
const ProcessingQueue = styled.div``

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
  customerList: Map<string, customerType>,
  currentlyProcessedCustomers: Map<string, customerType>,
}


const UnprocessedQueue = ({highlightId, setHighlightId, customerList, currentlyProcessedCustomers}: HighlightType) => {


  return (
    <Container className="w-[1310px] h-[60px] bg-white">
      <Wrapper className="w-[90.6%] h-[60px]  overflow-x-auto flex items-center  ml-auto hide-scrollbar">
        <ProcessingQueue className="h-full min-w-[70px] flex items-center pl-2 mr-[-5px]">
          <AnimatePresence mode="popLayout">
              {Array.from(currentlyProcessedCustomers.values()).map((customer) => (
                <ProcessingCustomer
                  key={customer.sender_id}
                  setHighlightId={setHighlightId}
                  isHighlighted={highlightId == customer.sender_id}
                  id={customer.sender_id}
                  data={customer}
                />
              ))}
          </AnimatePresence>

        </ProcessingQueue>
        <AnimatePresence mode="popLayout">
          {Array.from(customerList.values()).map((customer, sender_id) => (
          <UprocessedCustomer
            key={sender_id}
            setHighlightId={setHighlightId}
            isHighlighted={highlightId == customer.sender_id}
            id={customer.sender_id}
            data={customer}
          />
          ))}
        </AnimatePresence>

      </Wrapper>
    </Container>

  );
};

export default UnprocessedQueue;