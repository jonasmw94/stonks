import React, { useState, useEffect, useRef } from "react";
import "./App.css";
import Login from './components/landing';

interface Vanta {
  NET: (arg: object) => { destroy: () => void };
}

declare global {
  interface Window { VANTA: Vanta; }
}

window.VANTA = window.VANTA || {};

type User = {
  
}

export default () => {
  const element = useRef<HTMLDivElement>(null);
  const user = useState<null | User>(null);

  useEffect(() => {
    const effect = window.VANTA.NET({
      el: element.current
    })

    setTimeout(() => {
      effect.destroy();
    },10000);
  }, [])

  if(!user) {
    return (
      <div ref={element}>
        <Login />
      </div>
    );
  }

  return (
    <div ref={element}>
      <Login />
    </div>
  )
}
