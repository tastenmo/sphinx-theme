const { resolve } = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");

module.exports = {
  devtool: "source-map",
  entry: {
    "sphinx-theme": [
      "./src/sphinx_theme/assets/scripts/sphinx-theme.js",
      "./src/sphinx_theme/assets/styles/sphinx-theme.sass",
    ],
    "sphinx-theme-extensions": ["./src/sphinx_theme/assets/styles/sphinx-theme-extensions.sass"],
  },
  output: {
    filename: "scripts/[name].js",
    path: resolve(__dirname, "src/sphinx_theme/theme/sphinx-theme/static"),
  },
  plugins: [new MiniCssExtractPlugin({ filename: "styles/[name].css" })],
  optimization: { minimizer: [`...`, new CssMinimizerPlugin()] },
  module: {
    rules: [
      {
        test: /\.s[ac]ss$/i,
        use: [
          MiniCssExtractPlugin.loader,
          { loader: "css-loader", options: { sourceMap: true } },
          { loader: "postcss-loader", options: { sourceMap: true } },
          { loader: "sass-loader", options: { sourceMap: true } },
        ],
      },
      {
        test: /\.(png|svg|jpg|jpeg|gif)$/i,
        type: 'asset/resource',
      },
    ],
  },
};
