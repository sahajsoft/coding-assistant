#! /usr/bin/env bun
import yargs from "yargs";
import { hideBin } from "yargs/helpers";
import { extract, review } from "./commands";

// Fix process name in commands
process.argv = process.argv.map((x, i) => (i === 0 ? "bugs" : x));

yargs(hideBin(process.argv))
  .option("verbose", {
    alias: "v",
    type: "boolean",
    description: "Run with verbose logging",
  })
  .command(extract)
  .command(review)
  .strict()
  .demandCommand(1)
  .parse();
