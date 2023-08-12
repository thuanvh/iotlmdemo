import { Box, Flex, Grid, GridItem } from "@chakra-ui/react";
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
        "Nice to meet you. You can send me message"
    }
  ]);
  const [inputMessage, setInputMessage] = useState("");

  const handleSendMessage = () => {
    if (!inputMessage.trim().length) {
      return;
    }
    const data = inputMessage;

    setMessages((old) => [...old, { from: "me", text: data }]);
    setInputMessage("");
    let url = "http://103.47.195.197:5110/api/chat?q=" + data;
    fetch(url)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      let answer = data.Answer;
      setMessages((old) => [...old, { from: "computer", text: data }]);
      
      
    })
    setTimeout(() => {
      setMessages((old) => [...old, { from: "computer", text: "Time out" }]);
    }, 600000);
  };

  return (
    <>
    
    <Flex h="100vh" justify="center" align="center">
        
       <Flex w={["100%", "100%", "60%"]} h="90%" flexDir="column">
      
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
