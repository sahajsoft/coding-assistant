#! /usr/bin/env bun
import yargs from "yargs";
import { hideBin } from "yargs/helpers";

// Fix process name in commands
process.argv = process.argv.map((x, i) => (i === 0 ? "bugs" : x));

yargs(hideBin(process.argv))
  .option("verbose", {
    alias: "v",
    type: "boolean",
    description: "Run with verbose logging",
  })
  .command(
    "extract",
    "extract code and relevant tests from a git diff",
    () => {},
    (args) => {
      if (args.verbose) console.log("diff provided:", args.diff);
      console.log("Nothing extracted for now.");
    }
  )
  .command(
    "review",
    "review relevant tests based on the code",
    () => {},
    (args) => {
      console.log("No suggestions at the moment");
    }
  )
  .strict()
  .demandCommand(1)
  .parse();
