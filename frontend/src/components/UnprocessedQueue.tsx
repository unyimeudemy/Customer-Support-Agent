import styled from "styled-components";
import UprocessedCustomer from "./UnprocessedCustomer";


const Wrapper = styled.div`

  &::-webkit-scrollbar {
    display: none; 
  }
`;
const Container = styled.div``;

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
  customerList: customerType[]
}


const UnprocessedQueue = ({highlightId, setHighlightId, customerList}: HighlightType) => {
  console.log("customer list: ", customerList)


  return (
    <Container className="w-[1310px] h-[60px] bg-white">
      <Wrapper className="w-[90.6%] h-[60px]  overflow-x-auto flex items-center  ml-auto hide-scrollbar">
        {customerList.map((customer, sender_id) => (
        <UprocessedCustomer
          key={sender_id}
          setHighlightId={setHighlightId}
          isHighlighted={highlightId == customer.sender_id}
          id={customer.sender_id}
          data={customer}
        />
        ))}
      </Wrapper>
    </Container>

  );
};

export default UnprocessedQueue;