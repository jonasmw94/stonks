import React from "react";
import styled from "styled-components";
import { FaTachometerAlt, FaUserAlt, FaFutbol } from "react-icons/fa";
import { NavHeader } from '../text';
import { NavLink } from 'react-router-dom';

export default function Dashboard() {
  return (
    <Frame>
      <Header><NavHeader>STONKS</NavHeader></Header>
      <InnerFrame>
        <Navbar>
          <IconFrame to="/dashboard" className={"active"}>
            <FaTachometerAlt size={24} />
          </IconFrame>
          <IconFrame to="/bets">
            <FaFutbol size={24} />
          </IconFrame>
          <IconFrame to="/profile">
            <FaUserAlt size={24} />
          </IconFrame>
        </Navbar>
        <Content>DASHBOARD</Content>
      </InnerFrame>
    </Frame>
  );
}

const Content = styled.div`
    padding: 20px;
    color: #fff;
`;

const IconFrame = styled(NavLink)`
  padding-top: 20px;
  padding-bottom: 20px;
  transition: 0.3s all;
  text-decoration: none;
  color: limegreen;

  &:hover {
    color: #fff;
    opacity: 0.7;
    cursor: pointer;
  }

  &.active {
      color: #fff;
      pointer-events: none;
  }
`;

const Header = styled.div`
  height: 80px;
  width: calc(100% - 36px);
  border-bottom: 1px solid #463565;

  display: flex;
  flex-direction: row;
  align-items: center;
  padding-left: 18px;
  padding-right: 18px;
`;

const InnerFrame = styled.div`
  display: flex;
  flex-direction: row;
  flex-grow: 1;
`;

const Navbar = styled.div`
  height: calc(100% - 21px);
  width: 120px;
  border-right: 1px solid #463565;
  padding-top: 20px;

  display: flex;
  flex-direction: column;
  align-items: center;
`;

const Frame = styled.div`
  height: 100vh;
  width: 100vw;
  display: flex;
  flex-direction: column;

  color: #c1214f;
`;
