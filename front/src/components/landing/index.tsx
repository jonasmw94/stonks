import React, { useState, useEffect } from "react";
import styled from "styled-components";
import { Header, SubHeaderText, NavHeader } from "../text";
import { FaArrowRight } from 'react-icons/fa'

type LoginProps = {
  login: (username: string, password: string) => void;
};

export default function Login(props: LoginProps) {
  const [loginActive, setLoginActive] = useState("");

  useEffect(() => {
    setTimeout(() => setLoginActive("active"), 1500);
  }, []);

  return (
    <Frame>
      <ContentFrame className={loginActive}>
        <LeftContent style={{ marginRight: 10 }}>
          <Header>STONKS</Header>
          <SubHeaderText>- Betting the left way</SubHeaderText>
        </LeftContent>
        <LeftContent
          style={{
            borderLeft: "1px solid #fff",
            justifyContent: "center",
            paddingLeft: 25,
            paddingRight: 25,
            backgroundColor: '#00000040'
          }}
        >
            <SubHeaderText style={{fontSize: 16, fontWeight: 500 }} >Login to dashboard</SubHeaderText>
          <Input style={{ marginTop: 10 }} placeholder="Username" />
          <Input
            style={{ marginBottom: 0 }}
            type="password"
            placeholder="Password"
          />
          <Button onClick={() => props.login("", "")}><FaArrowRight size={18} /></Button>
        </LeftContent>
      </ContentFrame>
    </Frame>
  );
}

const Input = styled.input`
  width: 140px;
  border: none;
  background: transparent;
  outline: none;
  color: #fff;
  height: 20px;
  padding: 10px;
  padding-bottom: 10px;
  margin-bottom: 25px;
  margin-top: 5px; 
  font-size: 14px;
  text-align: center;
  border-bottom: 1px solid #fff;
`;

const Button = styled.button`
  background: transparent;
  border: 1px solid #fff;
  color: #fff;

  width: 40px;
  height: 40px;
  border-radius: 20px;
  font-size: 14px;
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
  width: 420px;
  display: flex;
  flex-direction: row;
  overflow: hidden;
  transition: 0.5s all;

  &.active {
    width: 680px;
  }
`;
