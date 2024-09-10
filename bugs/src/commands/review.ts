import type { CommandModule } from "yargs";

export const review: CommandModule = {
  command: "review",
  describe: "review relevant tests based on the code",
  handler: (args) => {
    console.log("No suggestions at the moment");
  },
};
