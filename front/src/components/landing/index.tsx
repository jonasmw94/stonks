import React,{ useState, useEffect } from "react";
import styled from "styled-components";
import { Header, SubHeaderText } from "../text";

export default function Login() {
    const [loginActive, setLoginActive] = useState("");
    
    useEffect(() => {
        setTimeout(() => setLoginActive("active"),1500)
    },[]);
    
  return (
    <Frame>
      <ContentFrame className={loginActive} >
        <LeftContent style={{ marginRight: 10 }}>
          <Header>Stonks</Header>
          <SubHeaderText>- Betting the right way</SubHeaderText>
        </LeftContent>
        <LeftContent style={{ borderLeft: "1px solid #fff", justifyContent: 'center', paddingLeft: 25 }} >
            <Input style={{ marginTop: 10 }} placeholder="Username" />
            <Input style={{ marginBottom: 0 }} type="password" placeholder="Password" />
            <Button >Login</Button>
        </LeftContent>
      </ContentFrame>
    </Frame>
  );
}

const Input = styled.input`
    width: 180px;
    background: white;
    border: none;
    height: 20px;
    padding: 10px;
    margin-bottom: 20px;
    font-size: 14px;
    text-align: center;
    border-radius: 4px;
`;

const Button = styled.button`
  background: transparent;
  border: 1px solid #fff;
  color: #fff;

  width: 150px;
  height: 50px;
  border-radius: 4px;
  font-size: 16px;
  font-weight: 500;
  margin-top: 30px;

  transition: 0.3s all;

  &:hover {
    cursor: pointer;
    background: limegreen;
    border: none;
  }

  &.active {
      opacity: 0;
      pointer-events: none;
  }
`;

const Frame = styled.div`
  height: 100vh;
  width: 100vw;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
`;

const LeftContent = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const ContentFrame = styled.div`
  height: 250px;
  width: 340px;
  display: flex;
  flex-direction: row;
  overflow: hidden;
  transition: 0.5s all;

  &.active {
      width: 650px;
  }
`;
