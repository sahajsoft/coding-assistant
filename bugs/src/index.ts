#! /usr/bin/env bun
import yargs from "yargs";
import { hideBin } from "yargs/helpers";
import { extract, review } from "./commands";

process.argv = ["bugs", ""].concat(process.argv.slice(2));

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
