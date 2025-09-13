import React from 'react';

const ProductCard = ({ product, onClickFunc }) => {
    return (
        <div className="col-span-3 md:col-span-1 border border-gray-200 rounded-lg p-3 shadow-md">
            <div className="relative rounded-2xl aspect-[4/3] overflow-hidden mb-3 group">
                <img
                    src={`/static/product/${product.design}/${product.tech1}/top.png`}
                    alt={product.seo_title}
                    className="w-full aspect-[4/3] object-cover hover:scale-105 transition-transform duration-150 ease-in-out"
                />
                <div className="absolute inset-0 bg-black bg-opacity-50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg"></div>
                <div className="absolute inset-0 flex flex-col items-center justify-center space-y-2 opacity-0 group-hover:opacity-100 transition-opacity duration-300 px-16">
                    <a
                        href={`${product.url_demo}`}
                        target="_blank"
                        className="w-full text-center px-4 py-2 bg-white text-gray-900 font-medium rounded"
                    >
                        See offer
                    </a>
                </div>
            </div>

            <div className="flex justify-between items-center mb-2">
                <h4 className="font-bold">
                    <p className='cursor-pointer' onClick={() => onClickFunc(product.id)}>{product.name}</p>
                </h4>
                <h4 className="text-gray-900 dark:text-white font-bold">
                    <span className="text-red-600">${product.price}</span>
                </h4>
            </div>
            <p className="text-gray-500 dark:text-gray-300 text-sm mb-2">{product.card_info}</p>
            <div className="flex items-center justify-between">
                <p className="text-gray-500 dark:text-gray-300 text-sm">
                    <img
                        className="h-8"
                        src={`/static/common/agency/${product.design_by}.png`}
                        alt={`${product.name} designed by ${product.design_by}`}
                    />
                </p>
            </div>
        </div >
    );
};

export default ProductCard;
