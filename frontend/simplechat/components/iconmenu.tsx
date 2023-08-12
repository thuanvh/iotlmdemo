import { IconButton,Flex,Menu,MenuButton,HStack, Avatar,VStack,Text,Box,MenuList,MenuItem,MenuDivider,useColorModeValue,
     Button,Modal, ModalOverlay, ModalContent, ModalHeader, ModalCloseButton, ModalBody, ModalFooter } from "@chakra-ui/react"
import { useDisclosure } from "@chakra-ui/react"
import { useState } from "react"
import {
    FiHome,
    FiTrendingUp,
    FiCompass,
    FiStar,
    FiSettings,
    FiMenu,
    FiBell,
    FiChevronDown,
  } from 'react-icons/fi';

export default function IconMenu() {
    const { isOpen, onOpen, onClose } = useDisclosure()
    const [userLoaded, setUserLoaded] = useState(false)
    
    return (
    <><IconButton
          size="lg"
          variant="ghost"
          aria-label="open menu"
          icon={<FiBell />}
        />
        <Flex alignItems={'center'}>
          <Menu>
            <MenuButton
              py={2}
              transition="all 0.3s"
              _focus={{ boxShadow: 'none' }}>
              <HStack>
                <Avatar
                  size={'sm'}
                  src={
                    'https://images.unsplash.com/photo-1619946794135-5bc917a27793?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&fit=crop&h=200&w=200&s=b616b2c5b373a80ffc9636ba24f7a4a9'
                  }
                />
                <VStack
                  display={{ base: 'none', md: 'flex' }}
                  alignItems="flex-start"
                  spacing="1px"
                  ml="2">
                  <Text fontSize="sm">Justina Clark</Text>
                  <Text fontSize="xs" color="gray.600">
                    Admin
                  </Text>
                </VStack>
                <Box display={{ base: 'none', md: 'flex' }}>
                  <FiChevronDown />
                </Box>
              </HStack>
            </MenuButton>
            <MenuList
              bg={useColorModeValue('white', 'gray.900')}
              borderColor={useColorModeValue('gray.200', 'gray.700')}>
              <MenuItem>Ranking</MenuItem>
              <MenuItem>Chat</MenuItem>
              <MenuItem>Copy trade</MenuItem>

              <MenuItem>Your Account</MenuItem>
              <MenuDivider />
              <MenuItem>Settings</MenuItem>
              <MenuItem>About us</MenuItem>

            </MenuList>
          </Menu>
        </Flex>
        </>
    );
}