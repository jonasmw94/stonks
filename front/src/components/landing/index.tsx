import React from 'react';
import styled from 'styled-components';
import { Header, SubHeaderText } from '../text';

export default function Login() {
    return (
        <Frame>
            <ContentFrame>
                <Header>Stonks</Header>
                <SubHeaderText >- Betting the right way</SubHeaderText>
                <Button>Get started</Button>
            </ContentFrame>
        </Frame>
    )
}

const Button = styled.button`
    background: transparent;
    outline: none;
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

`;

const Frame = styled.div`
    height: 100vh;
    width: 100vw;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
`;

const ContentFrame = styled.div`
    height: 300px;
    z-index: 100000;
    display: flex;
    flex-direction: column;
    align-items: center;
`;