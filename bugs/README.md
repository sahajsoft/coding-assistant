# bugs

A CLI written in bun that helps write higher quality tests. A
bun-ny tool to catch bugs, hence the name (Bugs Bunny, anyone?).

## Getting Started

### Installation

You should be able to install `bugs` using `npm`, or related
package managers.

```sh
npm install -g bugs
```

### Usage

We can use bugs in 2 ways:

#### To collect suggestions for tests based on code

```sh
bugs suggest -c code
```

#### To review existing tests for a piece of code

```sh
bugs review -c code - tests
```

### Building

To build `bugs`, we use `bun` with `typescript` on `node 22`.
