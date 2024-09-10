import type { CommandModule } from "yargs";
import { lines } from "../rl";

export const extract: CommandModule<{ verbose?: boolean }, { verbose: boolean }> = {
  command: "extract",
  describe: "extract code and relevant tests from a git diff",
  handler: async (args) => {
    const _lines = await lines;
    if (args.verbose) console.log("diff provided:", _lines);
    console.log("Nothing extracted for now.");
  }
};
