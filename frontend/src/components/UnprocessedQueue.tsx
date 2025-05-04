import styled from "styled-components";
import UprocessedCustomer from "./UnprocessedCustomer";
import telegramIcon from "../assets/telegramIcon.webp"
import gmailIcon from "../assets/gmailIcon.webp"
import whatsappIcon from "../assets/whatsappIcon.png"

const Wrapper = styled.div`

  &::-webkit-scrollbar {
    display: none; 
  }
`;
const Container = styled.div``;

type HighlightType = {
  highlightId: string | null,
  setHighlightId: (id: string) => void
}


const UnprocessedQueue = ({highlightId, setHighlightId}: HighlightType) => {

  const customers = [
    {
      id: "28",
      channel: gmailIcon,
      notification: "3",
      detail: "Here is the detail"
    },
    {
      id: "29",
      channel: gmailIcon,
      notification: "1",
      detail: "Here is the detail"
    },
    {
      id: "30",
      channel: telegramIcon,
      notification: "1",
      detail: "Here is the detail"
    },
    {
      id: "31",
      channel: whatsappIcon,
      notification: "1",
      detail: "Here is the detail"
    },
    {
      id: "32",
      channel: whatsappIcon,
      notification: "10",
      detail: "Here is the detail"
    },
    {
      id: "33",
      channel: gmailIcon,
      notification: "2",
      detail: "Here is the detail"
    },
    {
      id: "34",
      channel: gmailIcon,
      notification: "2",
      detail: "Here is the detail"
    },
    {
      id: "35",
      channel: whatsappIcon,
      notification: "10",
      detail: "Here is the detail"
    },
    {
      id: "36",
      channel: gmailIcon,
      notification: "2",
      detail: "Here is the detail"
    },
    {
      id: "37",
      channel: gmailIcon,
      notification: "2",
      detail: "Here is the detail"
    },
    {
      id: "38",
      channel: telegramIcon,
      notification: "1",
      detail: "Here is the detail"
    },
    {
      id: "39",
      channel: whatsappIcon,
      notification: "1",
      detail: "Here is the detail"
    },
    {
      id: "40",
      channel: whatsappIcon,
      notification: "10",
      detail: "Here is the detail"
    },
    {
      id: "41",
      channel: gmailIcon,
      notification: "2",
      detail: "Here is the detail"
    },
    {
      id: "42",
      channel: gmailIcon,
      notification: "2",
      detail: "Here is the detail"
    },
    {
      id: "43",
      channel: whatsappIcon,
      notification: "10",
      detail: "Here is the detail"
    },
    {
      id: "44",
      channel: gmailIcon,
      notification: "2",
      detail: "Here is the detail"
    },
    {
      id: "45",
      channel: gmailIcon,
      notification: "2",
      detail: "Here is the detail"
    },
    {
      id: "46",
      channel: telegramIcon,
      notification: "1",
      detail: "Here is the detail"
    },
    {
      id: "47",
      channel: whatsappIcon,
      notification: "1",
      detail: "Here is the detail"
    },
    {
      id: "48",
      channel: whatsappIcon,
      notification: "10",
      detail: "Here is the detail"
    },
    {
      id: "49",
      channel: gmailIcon,
      notification: "2",
      detail: "Here is the detail"
    },
    {
      id: "50",
      channel: gmailIcon,
      notification: "2",
      detail: "Here is the detail"
    },
    {
      id: "51",
      channel: whatsappIcon,
      notification: "10",
      detail: "Here is the detail"
    },
    {
      id: "52",
      channel: gmailIcon,
      notification: "2",
      detail: "Here is the detail"
    },
    {
      id: "53",
      channel: gmailIcon,
      notification: "2",
      detail: "Here is the detail"
    },
    {
      id: "54",
      channel: gmailIcon,
      notification: "2",
      detail: "Here is the detail"
    }
  ];
  

  return (
    <Container className="w-[1360px] h-[60px] bg-white">
      <Wrapper className="w-[90.6%] h-[60px]  overflow-x-auto flex items-center  ml-auto hide-scrollbar">
        {customers.map((customer) => (
        <UprocessedCustomer
          setHighlightId={setHighlightId}
          isHighlighted={highlightId == customer.id}
          id={customer.id}
          data={customer}
        />
        ))}
      </Wrapper>
    </Container>

  );
};

export default UnprocessedQueue;