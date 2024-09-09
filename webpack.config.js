const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");
const { SourceMapDevToolPlugin } = require("webpack");
const path = require('path');
const BundleTracker = require("webpack-bundle-tracker");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");

module.exports = [
    {
        entry: './static/assets/index.js',  // path to your input file
        output: {
            filename: '[name].bundle.js',  // output bundle file name
            path: path.resolve(__dirname, './static/dist'),  // path to your Django static directory
        },

        module: {
            rules: [
                {
                    test: /\.css$/,
                    use: [MiniCssExtractPlugin.loader, 'css-loader', 'postcss-loader'],
                },
                {
                    test: /\.(png|jpg|gif|svg)$/,
                    loader: 'file-loader',
                    options: {
                        outputPath: 'static/images/'
                    }
                },
                {
                    test: /\.(ttf|eot|svg|gif|woff|woff2)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                    use: [{
                        loader: 'file-loader',
                    }]
                },
            ],
        },
        resolve: {
            extensions: ['', '.js', '.jsx', '.css']
        },
        plugins: [
            new MiniCssExtractPlugin(),
            new SourceMapDevToolPlugin({
                filename: "[file].map"
            }),
        ],
        optimization: {
            minimizer: [
                new CssMinimizerPlugin()
            ]
        },
    },
    {
        entry: {
            frontend: "./frontend/src/index.js",
        },
        output: {
            path: path.resolve("./frontend/static/frontend/"),
            filename: "[name]-[fullhash].js",
            publicPath: "static/frontend/",
        },
        plugins: [
            new CleanWebpackPlugin(),
            new BundleTracker({
                path: __dirname,
                filename: "./webpack-stats.json",
            }),
        ],
        module: {
            rules: [
                {
                    test: /\.js$/,
                    exclude: /node_modules/,
                    use: ["babel-loader"],
                },
                {
                    test: /\.css$/,
                    use: ["style-loader", "css-loader"],
                },
            ],
        },
    },
];
