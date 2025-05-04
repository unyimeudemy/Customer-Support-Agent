import styled from "styled-components";
import Customer from "./Customer";

const Wrapper = styled.div`

  &::-webkit-scrollbar {
    display: none; 
  }
`;
const Container = styled.div``;


const IncomingQueue = () => {
  return (
    <Container className="w-[1360px] h-[60px] bg-white">
      <Wrapper className="w-[90.6%] h-[60px]  overflow-x-auto flex items-center  ml-auto hide-scrollbar">
        <Customer/>
        <Customer/>
        <Customer/>
        <Customer/>
        <Customer/>
        <Customer/>
        <Customer/>

      </Wrapper>
    </Container>

  );
};

export default IncomingQueue;