import React, { useState, useEffect, useRef } from "react";
import "./App.css";
import Landing from "./components/landing";

interface Vanta {
  NET: (arg: object) => { destroy: () => void };
}

declare global {
  interface Window {
    VANTA: Vanta;
  }
}

window.VANTA = window.VANTA || {};

type User = {};

export default () => {
  const element = useRef<HTMLDivElement>(null);
  const [user, setUser] = useState<null | User>(null);
  const [net, setNet] = useState<null | { destroy: () => void }>(null);

  useEffect(() => {
    const effect = window.VANTA.NET({
      el: element.current
    });

    setNet(effect);
  }, []);

  if (!user) {
    return (
      <div ref={element}>
        <Landing />
      </div>
    );
  }

  return (
    <div ref={element}>
      <Landing />
    </div>
  );
};
