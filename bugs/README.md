# bugs

A CLI written in bun that helps write higher quality tests. A
bun-ny tool to catch bugs, hence the name (Bugs Bunny, anyone?).

## Getting Started

### Installation

You need [bun](https://bun.sh) to run `bugs` at this time. Clone this repo, and
then run at repo root:

```sh
cd bugs
bun link
bun link @artfuldev/bugs
```

### Usage

We can use bugs in 2 ways:

#### To collect suggestions for tests based on code

We use `bugs extract` which reads a `git diff` from `stdin` and outputs
extracted code and tests related to it via `stdout`.

```sh
git diff main..pr-71 | bugs extract
```

#### To review existing tests for a piece of code

We use `bugs review` with a diff directly via `stdin` and outputs recommendations
via `stdout`.

```sh
git diff main..pr-71 | bugs review
git diff main..pr-71 | bugs extract | bugs review
```

### Building

To build `bugs`, we use `bun` with `typescript` on `node 22`.
