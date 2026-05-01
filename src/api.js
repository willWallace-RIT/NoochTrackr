export async function simulateTurn(state) {
  const res = await fetch("http://localhost:8000/simulate-turn", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(state)
  });

  return await res.json();
}
