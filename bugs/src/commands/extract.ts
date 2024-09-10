import type { CommandModule } from "yargs";

export const extract: CommandModule = {
  command: "extract",
  describe: "extract code and relevant tests from a git diff",
  handler: async (args) => {
    if (args.verbose) console.log("diff provided:", args.diff);
    console.log("Nothing extracted for now.");
  }
};
