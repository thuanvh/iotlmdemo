import { Box, Flex, Grid, GridItem,Stack } from "@chakra-ui/react";
import { RadioGroup,Radio } from "@chakra-ui/radio";
import React, { useState } from "react";
import Divider from "@/components/chat/divider";
import Footer from "@/components/chat/footer";
import Header from "@/components/chat/header";
import Messages from "@/components/chat/messages";
const Chat = () => {
  const [messages, setMessages] = useState([
    { from: "computer", text: "Hi, My Name is HoneyChat" },
    { from: "me", text: "Hey there" },
    { from: "me", text: "Myself Ferin Patel" },
    {
      from: "computer",
      text:
        "Nice to meet you.\nYou can send me message"
    }
  ]);
  const [inputMessage, setInputMessage] = useState("");
  const [chatMode, setChatMode] = useState("1");

  const handleSendMessage = () => {
    if (!inputMessage.trim().length) {
      return;
    }
    const data = inputMessage;

    setMessages((old) => [...old, { from: "me", text: data }]);
    setInputMessage("");
    let host = chatMode == "1" ? "http://103.47.195.197:5110/api/chat?q=" : "http://103.47.195.197:5110/api/prompt_route?user_prompt=";
    let url =  host + data;
    fetch(url)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      let answer = data.Answer;
      setMessages((old) => [...old, { from: "computer", text: answer }]);
      
      
    })
    // setTimeout(() => {
    //   setMessages((old) => [...old, { from: "computer", text: "Sorry. Time out" }]);
    // }, 600000);
  };

  return (
    <>
    
    <Flex h="100vh" justify="center" align="center">
        
       <Flex w={["100%", "100%", "60%"]} h="90%" flexDir="column">
       <RadioGroup defaultValue='1' value={chatMode} onChange={setChatMode}>
        <Stack spacing={5} direction='row'>
          <Radio colorScheme='red' value="1">
            General Chat
          </Radio>
          <Radio colorScheme='green' value="2">
            Document Chat
          </Radio>
        </Stack>
      </RadioGroup>
      <Divider />

        <Header />
        <Divider />
        <Messages messages={messages} />
        <Divider />
        <Footer
          inputMessage={inputMessage}
          setInputMessage={setInputMessage}
          handleSendMessage={handleSendMessage}
        />
      </Flex>
    </Flex>
  
    
    </>
  );
};

export default Chat;
