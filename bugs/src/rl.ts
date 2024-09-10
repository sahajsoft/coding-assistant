
import { createInterface } from "node:readline";

const rl = createInterface(process.stdin);
export const lines = new Promise<string[]>((resolve, reject) => {
  let buffer: string[] = [];
  rl.on("line", (line) => buffer.push(line));
  rl.on("close", () => resolve(buffer));
  process.stdin.on("error", () => reject());
});
