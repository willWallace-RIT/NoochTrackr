import { useState } from "react";
import { simulateTurn } from "../api";

export default function Dashboard() {
  const [state, setState] = useState({ inventory: [] });
  const [output, setOutput] = useState(null);

  async function runTurn() {
    const result = await simulateTurn(state);
    setOutput(result);
  }

  return (
    <div>
      <button onClick={runTurn}>Simulate Turn</button>
      <pre>{JSON.stringify(output, null, 2)}</pre>
    </div>
  );
}
