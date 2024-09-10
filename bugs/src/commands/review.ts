import type { CommandModule } from "yargs";
import { lines } from "../rl";

export const review: CommandModule<{ verbose?: boolean }, { verbose: boolean }> = {
  command: "review",
  describe: "review relevant tests based on the code",
  handler: async (args) => {
    const _lines = await lines;
    if (args.verbose) console.log("read lines:", _lines);
    console.log("No suggestions at the moment");
  },
};
