{
  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    poetry2nix = {
      url = "github:nix-community/poetry2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, flake-utils, poetry2nix }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        nativeBuildInputs = with pkgs; [ stdenv python3 python312Packages.setuptools poetry tesseract nodejs_22 ];
        buildInputs = with pkgs; [ ollama bun little_boxes];

        # see https://github.com/nix-community/poetry2nix/tree/master#api for more functions and examples.
        pkgs = nixpkgs.legacyPackages.${system};
        inherit (poetry2nix.lib.mkPoetry2Nix { inherit pkgs; })
          mkPoetryApplication defaultPoetryOverrides;
        default = pkgs.mkShell {
            packages = nativeBuildInputs ++ buildInputs;
            LD_LIBRARY_PATH = if pkgs.stdenv.isLinux then
              "${pkgs.stdenv.cc.cc.lib}/lib:/run/opengl-driver/lib:/run/opengl-driver-32/lib"
            else
              "$LD_LIBRARY_PATH";
          };
      in {
          devShells.default = default;
          packages.default = default;
      });
}
